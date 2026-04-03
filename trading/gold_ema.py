import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta

def calculate_ema(data, period):
    """Calculate Exponential Moving Average"""
    return data.ewm(span=period, adjust=False).mean()

def get_gold_ema():
    """Fetch gold data and calculate 20 and 50 day EMAs"""
    # Gold ticker symbol (GC=F for Gold Futures or GLD for Gold ETF)
    ticker = "GC=F"  # Gold Futures
    
    # Fetch data for the last 100 days to ensure we have enough data for 50-day EMA
    end_date = datetime.now()
    start_date = end_date - timedelta(days=150)
    
    print(f"Fetching Gold data from {start_date.date()} to {end_date.date()}...")
    
    # Download gold data
    gold = yf.download(ticker, start=start_date, end=end_date, progress=False)
    
    if gold.empty:
        print("No data retrieved. Trying GLD ETF instead...")
        ticker = "GLD"
        gold = yf.download(ticker, start=start_date, end=end_date, progress=False)
    
    if gold.empty:
        print("Failed to retrieve gold data.")
        return
    
    # Calculate EMAs
    gold['EMA_20'] = calculate_ema(gold['Close'], 20)
    gold['EMA_50'] = calculate_ema(gold['Close'], 50)
    
    # Get the latest values
    latest_data = gold.iloc[-1]
    latest_date = gold.index[-1]
    
    # Convert to scalar values to avoid Series formatting errors
    current_price = latest_data['Close'].item() if hasattr(latest_data['Close'], 'item') else float(latest_data['Close'])
    ema_20 = latest_data['EMA_20'].item() if hasattr(latest_data['EMA_20'], 'item') else float(latest_data['EMA_20'])
    ema_50 = latest_data['EMA_50'].item() if hasattr(latest_data['EMA_50'], 'item') else float(latest_data['EMA_50'])
    
    # Display results
    print("\n" + "="*60)
    print(f"Gold ({ticker}) - EMA Analysis")
    print("="*60)
    print(f"Date: {latest_date.strftime('%Y-%m-%d')}")
    print(f"Current Price: ${current_price:.2f}")
    print(f"20-Day EMA: ${ema_20:.2f}")
    print(f"50-Day EMA: ${ema_50:.2f}")
    print("-"*60)
    
    # Analysis
    if current_price > ema_20 and current_price > ema_50:
        print("📈 Trend: BULLISH (Price above both EMAs)")
    elif current_price < ema_20 and current_price < ema_50:
        print("📉 Trend: BEARISH (Price below both EMAs)")
    else:
        print("➡️  Trend: NEUTRAL (Mixed signals)")
    
    if ema_20 > ema_50:
        print("✓ 20 EMA > 50 EMA: Short-term uptrend")
    else:
        print("✗ 20 EMA < 50 EMA: Short-term downtrend")
    
    print("="*60)
    
    # Show recent history
    print("\nRecent 5-Day History:")
    print("-"*60)
    recent = gold[['Close', 'EMA_20', 'EMA_50']].tail(5)
    for date, row in recent.iterrows():
        close_val = row['Close'].item() if hasattr(row['Close'], 'item') else float(row['Close'])
        ema20_val = row['EMA_20'].item() if hasattr(row['EMA_20'], 'item') else float(row['EMA_20'])
        ema50_val = row['EMA_50'].item() if hasattr(row['EMA_50'], 'item') else float(row['EMA_50'])
        print(f"{date.strftime('%Y-%m-%d')}: Price=${close_val:.2f}, "
              f"EMA20=${ema20_val:.2f}, EMA50=${ema50_val:.2f}")
    
    return gold

if __name__ == "__main__":
    try:
        get_gold_ema()
    except Exception as e:
        print(f"Error: {e}")
        print("\nMake sure you have yfinance installed:")
        print("pip install yfinance")
