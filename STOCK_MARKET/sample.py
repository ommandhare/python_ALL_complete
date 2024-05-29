from nsepy import get_history
from datetime import date
import pandas as pd

symbols = ['RELIANCE', 'TCS', 'INFY']  # Add up to 2000 symbols here
start_date = date(2020, 1, 1)
end_date = date(2020, 12, 31)

for symbol in symbols:
    data = get_history(symbol=symbol, start=start_date, end=end_date)
    data.to_csv(f"{symbol}.csv")

# To combine all data into a single CSV file:
all_data = pd.concat([pd.read_csv(f"{symbol}.csv") for symbol in symbols])
all_data.to_csv("all_symbols_data.csv", index=False)
