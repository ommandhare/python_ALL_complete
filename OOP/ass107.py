"""
read nse_daily_stock file (create class that stores symbol, date, closing price as attributes).
Store objects in a list, implement algorithm to find peaks in the list (peak price) and
print objects that are on the peak

"""

class StockData:
    def __init__(self, symbol, date, closing_price):
        self.symbol = symbol
        self.date = date
        self.closing_price = closing_price

def read_stock_data(file_name):
    stock_data_list = []
    with open(file_name, 'r') as file:
        for line in file:
            symbol, date, closing_price = line.strip().split(',')
            stock_data = StockData(symbol, date, float(closing_price))
            stock_data_list.append(stock_data)
    return stock_data_list

def find_peaks(stock_data_list):
    peaks = []
    n = len(stock_data_list)
    for i in range(1, n - 1):
        if stock_data_list[i].closing_price > stock_data_list[i - 1].closing_price and stock_data_list[i].closing_price > stock_data_list[i + 1].closing_price:
            peaks.append(stock_data_list[i])
    return peaks


file_name = r'C:\Users\HP\PycharmProjects\pythonProject.py\venv\Assignments\OOP\nseSample'
stock_data_list = read_stock_data(file_name)
peaks = find_peaks(stock_data_list)
print("Peaks in closing prices:")
for peak in peaks:
    print(f"Symbol: {peak.symbol}, Date: {peak.date}, Closing Price: {peak.closing_price}")
