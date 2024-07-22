import requests
from nsepy import get_history
import pandas as pd
from datetime import date

# Function to get NSE symbols
def get_nse_symbols():
    url = 'https://www1.nseindia.com/content/equities/EQUITY_L.csv'
    response = requests.get(url)
    data = response.content.decode('utf-8')
    df = pd.read_csv(pd.compat.StringIO(data))
    symbols = df['SYMBOL'].tolist()
    return symbols

# Function to fetch historical data using nsepy
def fetch_historical_data_nsepy(symbols, start_date, end_date):
    all_data = pd.DataFrame()

    for symbol in symbols:
        try:
            print(f"Fetching data for {symbol}...")
            data = get_history(symbol=symbol, start=start_date, end=end_date)
            if not data.empty:
                data['Symbol'] = symbol
                all_data = pd.concat([all_data, data])
        except Exception as e:
            print(f"Error fetching data for {symbol}: {e}")

    return all_data

# Main function
def main():
    # Get the list of NSE symbols
    symbols = get_nse_symbols()

    # Define the date range
    start_date = date(2022, 1, 1)
    end_date = date(2024, 12, 31)

    # Fetch historical data using nsepy
    historical_data = fetch_historical_data_nsepy(symbols, start_date, end_date)

    # Save the data to a CSV file
    historical_data.to_csv('nse_symbols_data_2022_2024.csv')
    print("Data fetching complete. Saved to 'nse_symbols_data_2022_2024.csv'")

if __name__ == "__main__":
    main()
