# backtest_ma.py
# pip: pip install pandas numpy yfinance

import pandas as pd
import numpy as np
import yfinance as yf

def fetch_data(symbol='AAPL', period='2y', interval='1d'):
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

def backtest_ma(df, fast=20, slow=50, initial_capital=10000, risk_per_trade=0.01):
    df = df.copy()
    df['fast'] = df['Close'].rolling(fast).mean()
    df['slow'] = df['Close'].rolling(slow).mean()
    df.dropna(inplace=True)

    position = 0  # 0 or 1 (long only)
    entry_price = 0.0
    cash = initial_capital
    shares = 0
    equity_curve = []

    for idx in range(len(df)):
        row = df.iloc[idx]
        price = row['Close']
        if position == 0 and row['fast'] > row['slow']:
            # enter long: calculate trade size by risk_per_trade using simple stop loss (slow SMA as stop)
            stop_price = row['slow']
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
            entry_price = price
            position = 1
        elif position == 1 and row['fast'] < row['slow']:
            # exit
            cash += shares * price
            shares = 0
            position = 0

        total_equity = cash + shares * price
        equity_curve.append(total_equity)

    # close remaining position at last price
    if shares > 0:
        cash += shares * df.iloc[-1]['Close']
        shares = 0

    returns = pd.Series(equity_curve)
    result = {
        'initial_capital': initial_capital,
        'final_capital': cash,
        'net_return_pct': (cash - initial_capital) / initial_capital * 100,
        'max_drawdown_pct': (returns.cummax() - returns).max() / initial_capital * 100 if len(returns)>0 else 0,
    }
    return result

if __name__ == '__main__':
    df = fetch_data('AAPL', period='3y', interval='1d')
    res = backtest_ma(df, fast=20, slow=50, initial_capital=10000, risk_per_trade=0.01)
    print("Backtest result:", res)
