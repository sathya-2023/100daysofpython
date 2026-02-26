import pandas as pd
import yfinance as yf
from datetime import datetime, timedelta
from typing import List, Dict, Optional


def get_dividend_info(symbol: str) -> Optional[Dict]:
    """Fetch dividend information for a given stock symbol."""
    try:
        ticker = yf.Ticker(symbol)
        info = ticker.info
        
        # Get dividend history
        dividends = ticker.dividends
        
        if dividends.empty:
            return None
        
        # Get the most recent dividend
        last_dividend = dividends.iloc[-1]
        last_dividend_date = dividends.index[-1]
        
        # Calculate dividend yield and other metrics
        current_price = info.get('currentPrice', info.get('regularMarketPrice', 0))
        dividend_yield = info.get('dividendYield', 0)
        dividend_rate = info.get('dividendRate', 0)
        
        # Get ex-dividend date
        ex_dividend_date = info.get('exDividendDate')
        if ex_dividend_date:
            ex_dividend_date = datetime.fromtimestamp(ex_dividend_date)
        
        return {
            'Symbol': symbol,
            'Company': info.get('longName', symbol),
            'Current Price': f"${current_price:.2f}" if current_price else "N/A",
            'Dividend Rate (Annual)': f"${dividend_rate:.2f}" if dividend_rate else "N/A",
            'Dividend Yield': f"{dividend_yield * 100:.2f}%" if dividend_yield else "N/A",
            'Last Dividend': f"${last_dividend:.2f}",
            'Last Dividend Date': last_dividend_date.strftime('%Y-%m-%d'),
            'Ex-Dividend Date': ex_dividend_date.strftime('%Y-%m-%d') if ex_dividend_date else "N/A",
            'Payout Ratio': f"{info.get('payoutRatio', 0) * 100:.2f}%" if info.get('payoutRatio') else "N/A",
        }
    except Exception as e:
        print(f"Error fetching data for {symbol}: {e}")
        return None


def get_dividends_for_month(symbol: str, year: int, month: int) -> pd.DataFrame:
    """Get all dividend payments for a specific month."""
    try:
        ticker = yf.Ticker(symbol)
        dividends = ticker.dividends
        
        if dividends.empty:
            return pd.DataFrame()
        
        # Filter dividends for the specific month
        dividends_df = dividends.to_frame(name='Dividend')
        dividends_df['Year'] = dividends_df.index.year
        dividends_df['Month'] = dividends_df.index.month
        
        monthly_dividends = dividends_df[
            (dividends_df['Year'] == year) & 
            (dividends_df['Month'] == month)
        ].copy()
        
        return monthly_dividends[['Dividend']]
    except Exception as e:
        print(f"Error fetching monthly dividends for {symbol}: {e}")
        return pd.DataFrame()


def get_dividend_calendar(symbols: List[str], start_date: datetime, end_date: datetime) -> pd.DataFrame:
    """Get dividend calendar for multiple stocks within a date range."""
    calendar_data = []
    
    for symbol in symbols:
        try:
            ticker = yf.Ticker(symbol)
            dividends = ticker.dividends
            
            if dividends.empty:
                continue
            
            # Filter dividends within the date range
            mask = (dividends.index >= start_date) & (dividends.index <= end_date)
            filtered_dividends = dividends[mask]
            
            for date, amount in filtered_dividends.items():
                calendar_data.append({
                    'Symbol': symbol,
                    'Date': date.strftime('%Y-%m-%d'),
                    'Dividend': f"${amount:.2f}",
                    'Amount': amount
                })
        except Exception as e:
            print(f"Error processing {symbol}: {e}")
            continue
    
    if calendar_data:
        df = pd.DataFrame(calendar_data)
        df = df.sort_values('Date', ascending=False)
        return df[['Date', 'Symbol', 'Dividend']]
    
    return pd.DataFrame()


def find_dividend_companies_for_month(symbols: List[str], year: int, month: int) -> List[Dict]:
    """Find companies that pay dividends in a specific month."""
    companies_paying = []
    
    # Create date range for the month
    start_date = datetime(year, month, 1)
    if month == 12:
        end_date = datetime(year + 1, 1, 1) - timedelta(days=1)
    else:
        end_date = datetime(year, month + 1, 1) - timedelta(days=1)
    
    print(f"\nSearching for dividend payments in {start_date.strftime('%B %Y')}...")
    print("This may take a moment...\n")
    
    for symbol in symbols:
        try:
            ticker = yf.Ticker(symbol)
            info = ticker.info
            dividends = ticker.dividends
            
            if dividends.empty:
                continue
            
            # Filter dividends within the date range
            mask = (dividends.index >= start_date) & (dividends.index <= end_date)
            filtered_dividends = dividends[mask]
            
            if not filtered_dividends.empty:
                company_name = info.get('longName', symbol)
                current_price = info.get('currentPrice', info.get('regularMarketPrice', 0))
                dividend_yield = info.get('dividendYield', 0)
                
                for date, amount in filtered_dividends.items():
                    companies_paying.append({
                        'Symbol': symbol,
                        'Company': company_name,
                        'Payment Date': date.strftime('%Y-%m-%d'),
                        'Dividend Amount': f"₹{amount:.2f}",
                        'Current Price': f"₹{current_price:.2f}" if current_price else "N/A",
                        'Yield': f"{dividend_yield * 100:.2f}%" if dividend_yield else "N/A",
                    })
        except Exception as e:
            # Silently skip errors during search
            continue
    
    return companies_paying


def main() -> None:
    print("=== Indian Dividend Companies Finder ===\n")
    
    # Popular Indian dividend-paying stocks (NSE symbols)
    # .NS suffix for NSE (National Stock Exchange) or .BO for BSE (Bombay Stock Exchange)
    INDIAN_DIVIDEND_STOCKS = [
        # IT & Tech
        'TCS.NS', 'INFY.NS', 'WIPRO.NS', 'HCLTECH.NS', 'TECHM.NS',
        # Banking & Finance
        'HDFCBANK.NS', 'ICICIBANK.NS', 'SBIN.NS', 'KOTAKBANK.NS', 'AXISBANK.NS',
        'BAJFINANCE.NS', 'HDFC.NS', 'BAJAJFINSV.NS',
        # FMCG
        'HINDUNILVR.NS', 'ITC.NS', 'NESTLEIND.NS', 'BRITANNIA.NS', 'DABUR.NS',
        # Energy & Oil
        'RELIANCE.NS', 'ONGC.NS', 'BPCL.NS', 'IOC.NS', 'NTPC.NS', 'POWERGRID.NS',
        # Pharma
        'SUNPHARMA.NS', 'DRREDDY.NS', 'CIPLA.NS', 'DIVISLAB.NS', 'AUROPHARMA.NS',
        # Auto
        'MARUTI.NS', 'M&M.NS', 'TATAMOTORS.NS', 'BAJAJ-AUTO.NS', 'HEROMOTOCO.NS',
        # Metals & Mining
        'TATASTEEL.NS', 'HINDALCO.NS', 'COALINDIA.NS', 'VEDL.NS',
        # Telecom
        'BHARTIARTL.NS',
        # Cement
        'ULTRACEMCO.NS', 'GRASIM.NS', 'SHREECEM.NS',
        # Consumer Durables
        'TITAN.NS', 'ASIANPAINT.NS',
        # Conglomerate
        'LT.NS', 'ADANIENT.NS',
        # Infrastructure
        'ADANIPORTS.NS',
    ]
    
    # Offer custom stock list option
    custom_stocks = input("Enter custom Indian stock symbols with .NS or .BO suffix (comma-separated) or press Enter to search popular dividend stocks: ").strip()
    
    if custom_stocks:
        symbols = [s.strip().upper() for s in custom_stocks.split(',')]
    else:
        symbols = INDIAN_DIVIDEND_STOCKS
        print(f"Searching {len(symbols)} popular Indian dividend stocks...")
    
    # Get month and year
    current_date = datetime.now()
    month_input = input(f"\nEnter month (1-12, default: {current_date.month}): ").strip()
    month = int(month_input) if month_input else current_date.month
    
    year_input = input(f"Enter year (default: {current_date.year}): ").strip()
    year = int(year_input) if year_input else current_date.year
    
    # Validate month
    if month < 1 or month > 12:
        print("Invalid month. Please enter a value between 1 and 12.")
        return
    
    # Find companies paying dividends
    companies = find_dividend_companies_for_month(symbols, year, month)
    
    # Display results
    month_name = datetime(year, month, 1).strftime('%B %Y')
    print(f"\n{'='*100}")
    print(f"INDIAN COMPANIES PAYING DIVIDENDS IN {month_name.upper()}")
    print(f"{'='*100}\n")
    
    if companies:
        df = pd.DataFrame(companies)
        df = df.sort_values('Payment Date')
        print(df.to_string(index=False))
        print(f"\n\nTotal: {len(companies)} dividend payment(s) found from {df['Symbol'].nunique()} companies")
    else:
        print(f"No dividend payments found in {month_name} for the searched stocks.")
        print("\nTip: Some companies may have historical data only. Try different months or add more symbols.")
    
    print(f"\n{'='*100}")


if __name__ == '__main__':
    main()
