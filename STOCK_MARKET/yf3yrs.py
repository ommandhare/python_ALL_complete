import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta

# Load symbols from CSV file
symbols_df = pd.read_csv(r'C:\Users\om\PycharmProjects\python_All\STOCK_MARKET\symboltry.csv')

# Extract symbols
symbols = symbols_df['Symbol']

# Define headers
headers = [
    "PREV. CLOSE",
    "IEP",
    "CHNG",
    "%CHNG",
    "FINAL",
    "FINAL QUANTITY",
    "VALUE (₹ Crores)",
    "FFM CAP (₹ Crores)",
    "NM 52W H",
    "NM 52W L"
]

# Create a dictionary to hold the data
data = {}

# Calculate date range for the past 3 years
end_date = datetime.today().strftime('%Y-%m-%d')
start_date = (datetime.today() - timedelta(days=3*365)).strftime('%Y-%m-%d')

# Fetch data for each symbol
for symbol in symbols:
    try:
        ticker = yf.Ticker(symbol + ".NS")  # Adding ".NS" to indicate NSE
        hist = ticker.history(start=start_date, end=end_date)

        # Ensure there's at least some historical data
        if not hist.empty:
            prev_close = hist['Close'].iloc[-1]
            iep = hist['Close'].iloc[-1]
            chng = hist['Close'].iloc[-1] - hist['Open'].iloc[-1]
            pchng = (chng / hist['Open'].iloc[-1]) * 100
            final = hist['Close'].iloc[-1]
            final_quantity = hist['Volume'].iloc[-1]
            value_crores = (hist['Close'].iloc[-1] * hist['Volume'].iloc[-1]) / 10**7  # Approximate Value in ₹ Crores

            # Calculate the 52-week high and low
            nm_52w_h = hist['Close'][-252:].max()  # last 252 trading days
            nm_52w_l = hist['Close'][-252:].min()  # last 252 trading days

            # Free Float Market Cap not available from yfinance, set as 'N/A'
            ffm_cap = 'N/A'

            data[symbol] = [
                prev_close,
                iep,
                chng,
                pchng,
                final,
                final_quantity,
                value_crores,
                ffm_cap,
                nm_52w_h,
                nm_52w_l
            ]
        else:
            print(f"No historical data found for {symbol}")
    except Exception as e:
        print(f"Failed to fetch data for {symbol}: {e}")

# Convert data to DataFrame
data_df = pd.DataFrame.from_dict(data, orient='index', columns=headers)

# Print or do further processing with data_df
print(data_df)

data_df.to_csv(r"C:\Users\om\PycharmProjects\python_All\STOCK_MARKET\sample3yrs.csv")
