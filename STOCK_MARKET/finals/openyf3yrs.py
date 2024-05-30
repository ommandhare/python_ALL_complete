import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta


symbols_df = pd.read_csv(r'/STOCK_MARKET/symboltry.csv')


symbols = symbols_df['Symbol']

# Define headers
headers = [
    "DATE",
    "SYMBOL",
    "OPEN",
    "HIGH",
    "LOW",
    "CLOSE",
    "SHARES TRADED",
    "TURNOVER (₹ Cr)"
]


all_data = []


end_date = datetime.today().strftime('%Y-%m-%d')
start_date = (datetime.today() - timedelta(days=3*365)).strftime('%Y-%m-%d')

for symbol in symbols:
    try:
        ticker = yf.Ticker(symbol + ".NS")  # Adding ".NS" to indicate NSE
        hist = ticker.history(start=start_date, end=end_date)


        if not hist.empty:
            for date, row in hist.iterrows():
                open_price = row['Open']
                high_price = row['High']
                low_price = row['Low']
                close_price = row['Close']
                shares_traded = row['Volume']
                turnover = (close_price * shares_traded) / 10**7  # Turnover in ₹ Crores

                all_data.append([
                    date.strftime('%Y-%m-%d'),
                    symbol,
                    open_price,
                    high_price,
                    low_price,
                    close_price,
                    shares_traded,
                    turnover
                ])
        else:
            print(f"No historical data found for {symbol}")
    except Exception as e:
        print(f"Failed to fetch data for {symbol}: {e}")


data_df = pd.DataFrame(all_data, columns=headers)


data_df.to_csv('historical_stock_data.csv', index=False)


print(data_df)
