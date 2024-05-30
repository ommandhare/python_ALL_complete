import pandas as pd
from nsepy import get_history
from datetime import date, timedelta

# Define the date range
end_date = date.today()
start_date = end_date - timedelta(days=3*365)


symbols = ["RELIANCE", "TCS", "INFY", "HDFCBANK"]  # Add your 2000 symbols here

symbols = ["RELIANCE", "TCS", "INFY", "HDFCBANK"]  # Add your 2000 symbols here

#
# data=get_history(symbols[0],start_date,end_date)
# print(data)
# Fetch data for each symbol and save to CSV
for symbol in symbols:
    try:
        data = get_history(symbol=symbol, start=start_date, end=end_date)
        data.to_csv(f"{symbol}_3yrs.csv")
        print(f"Data for {symbol} saved successfully.")
    except Exception as e:
        print(f"Failed to fetch data for {symbol}: {e}")
