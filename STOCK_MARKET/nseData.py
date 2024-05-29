from nsetools import Nse
from datetime import datetime, timedelta

nse = Nse()

# Get list of all symbols
all_symbols = nse.get_stock_codes()

# Assuming you want data for the last 3 years
end_date = datetime.now()
start_date = end_date - timedelta(days=3*365)

for symbol in all_symbols.keys():
    data = nse.get_historical_data(symbol, start_date, end_date)


print(data)