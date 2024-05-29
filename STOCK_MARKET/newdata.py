import pandas as pd
from nsepy import get_history
from datetime import date, timedelta


# Define the date range
end_date = date.today()
start_date = end_date - timedelta(days=3*365)  # 3 years back

# List of symbols (replace with your actual list of 2000 symbols)
symbols = ["RELIANCE", "TCS", "INFY", "HDFCBANK"]  # Add your 2000 symbols here

def fetch_data(symbol):
    return get_history(symbol=symbol, start=start_date, end=end_date)

for symbol in symbols:
    try:
        data = fetch_data(symbol)
        data.to_csv(f"{symbol}_3yrs.csv")
        print(f"Data for {symbol} saved successfully.")
    except Exception as e:
        print(f"Failed to fetch data for {symbol}: {e}")
