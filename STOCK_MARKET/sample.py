import yfinance as yf
import pandas as pd

# Load symbols from CSV file
symbols_df = pd.read_csv(r'C:\Users\om\PycharmProjects\python_All\STOCK_MARKET\symboltry.csv')

# Extract symbols
symbols = symbols_df['Symbol']

for symbol in symbols:
    ticker = yf.Ticker(symbol + ".NS")
    print(ticker)