import yfinance as yf
import pandas as pd

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
cnt=0

# Fetch data for each symbol
for symbol in symbols:
    try:
        ticker = yf.Ticker(symbol + ".NS")  # Adding ".NS" to indicate NSE
        info = ticker.history(period="1d")
        prev_close = info['Close'].iloc[0]
        iep = info['Close'].iloc[0]
        chng = info['Close'].iloc[0] - info['Open'].iloc[0]
        pchng = (chng / info['Open'].iloc[0]) * 100
        final = info['Close'].iloc[0]
        final_quantity = info['Volume'].iloc[0]
        value_crores = (info['Close'].iloc[0] * info['Volume'].iloc[0]) / 10**7  # Approximate Value in ₹ Crores
        ffm_cap = 'N/A'  # Free Float Market Cap not available from yfinance
        nm_52w_h = ticker.info.get('fiftyTwoWeekHigh', 'N/A')
        nm_52w_l = ticker.info.get('fiftyTwoWeekLow', 'N/A')

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
    except Exception as e:
        print(f"Failed to fetch data for {symbol}: {e}")
        cnt+=1
        continue

# Convert data to DataFrame
data_df = pd.DataFrame.from_dict(data, orient='index', columns=headers)



# Print or do further processing with data_df
print(data_df)
print(f"{cnt} are dilisted and ignore")


data_df.to_csv(r"C:\Users\om\PycharmProjects\python_All\STOCK_MARKET\sampletry11.csv")