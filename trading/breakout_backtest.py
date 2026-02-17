# breakout_backtest.py
# pip: pip install pandas numpy yfinance

import pandas as pd
import numpy as np
import yfinance as yf


def fetch_data(symbol='TATSILV.NS', period='2y', interval='1d'):
    df = yf.download(
        symbol,
        period=period,
        interval=interval,
        auto_adjust=False,
        progress=False,
    )
    if isinstance(df.columns, pd.MultiIndex):
        df.columns = df.columns.get_level_values(0)
    df = df[['Open', 'High', 'Low', 'Close', 'Volume']].dropna()
    return df


def backtest_breakout(
    df,
    lookback=20,
    initial_capital=10000,
    risk_per_trade=0.01,
):
    df = df.copy()
    df['rolling_high'] = df['High'].rolling(lookback).max()
    df['rolling_low'] = df['Low'].rolling(lookback).min()
    df.dropna(inplace=True)

    position = 0
    cash = initial_capital
    shares = 0
    equity_curve = []

    for idx in range(len(df)):
        row = df.iloc[idx]
        price = row['Close']
        prev_high = df.iloc[idx - 1]['rolling_high'] if idx > 0 else np.nan

        if position == 0 and price > prev_high:
            # Enter on breakout; size position using rolling low as stop.
            stop_price = row['rolling_low']
            if stop_price >= price:
                continue
            risk_amount = cash * risk_per_trade
            stop_risk_per_share = price - stop_price
            if stop_risk_per_share <= 0:
                continue
            shares = int(risk_amount / stop_risk_per_share)
            if shares <= 0:
                continue
            cash -= shares * price
            position = 1
        elif position == 1 and price < row['rolling_low']:
            # Exit on breakdown below rolling low.
            cash += shares * price
            shares = 0
            position = 0

        total_equity = cash + shares * price
        equity_curve.append(total_equity)

    if shares > 0:
        cash += shares * df.iloc[-1]['Close']
        shares = 0

    returns = pd.Series(equity_curve)
    result = {
        'initial_capital': initial_capital,
        'final_capital': cash,
        'net_return_pct': (cash - initial_capital) / initial_capital * 100,
        'max_drawdown_pct': (returns.cummax() - returns).max() / initial_capital * 100 if len(returns) > 0 else 0,
    }
    return result

def buy_and_hold_result(df, initial_capital=10000):
    if df.empty:
        return {
            'initial_capital': initial_capital,
            'final_capital': initial_capital,
            'net_return_pct': 0.0,
            'max_drawdown_pct': 0.0,
        }

    first_close = df['Close'].iloc[0]
    last_close = df['Close'].iloc[-1]

    equity_curve = initial_capital * (df['Close'] / first_close)
    drawdown = (equity_curve.cummax() - equity_curve).max()

    final_capital = initial_capital * (last_close / first_close)
    return {
        'initial_capital': initial_capital,
        'final_capital': final_capital,
        'net_return_pct': (final_capital - initial_capital) / initial_capital * 100,
        'max_drawdown_pct': (drawdown / initial_capital) * 100,
    }


if __name__ == '__main__':
    df = fetch_data('TATSILV.NS', period='3y', interval='1d')
    initial_capital = 10000

    res = backtest_breakout(df, lookback=20, initial_capital=initial_capital, risk_per_trade=0.01)
    bh = buy_and_hold_result(df, initial_capital=initial_capital)

    print('Breakout backtest result')
    print(f"Initial capital: ${res['initial_capital']:,.2f}")
    print(f"Final capital:   ${res['final_capital']:,.2f}")
    print(f"Net return:      {res['net_return_pct']:.2f}%")
    print(f"Max drawdown:    {res['max_drawdown_pct']:.2f}%")

    print('\nBuy and hold result')
    print(f"Initial capital: ${bh['initial_capital']:,.2f}")
    print(f"Final capital:   ${bh['final_capital']:,.2f}")
    print(f"Net return:      {bh['net_return_pct']:.2f}%")
    print(f"Max drawdown:    {bh['max_drawdown_pct']:.2f}%")
