from nsepython import nse_eq
import pandas as pd
from datetime import datetime, timedelta

# Define the date range for the last three years
end_date = datetime.now()
start_date = end_date - timedelta(days=3*365)

# Example symbols from the 2000s
symbols_2000s = ['INFY', 'TCS', 'WIPRO', 'RELIANCE', 'HDFCBANK']

# Fetch historical data for each symbol
historical_data = {}

for symbol in symbols_2000s:
    try:
        data = nse_eq(symbol, start_date.strftime('%d-%m-%Y'), end_date.strftime('%d-%m-%Y'))
        historical_data[symbol] = data
    except Exception as e:
        print(f"Error fetching data for {symbol}: {e}")

# Convert to DataFrame for easier manipulation
df_historical = pd.concat(historical_data)
print(df_historical.head())

# Save the data to a CSV file
df_historical.to_csv('historical_data_2000s.csv')
