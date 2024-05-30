

path = r"C:\Users\om\PycharmProjects\python_All\STOCK_MARKET\2000sym.csv"
cnt = 0
symbolList = []

for line in open(path):
    if cnt == 0:
        cnt += 1
        continue
    else:
        desc = line.strip().split(",")
        symbol = desc[1]
        symbolList.append(symbol+".NS")
        # print(symbol)

# Now symbolList contains all your symbols
print(symbolList)
print(f"Total symbols: {len(symbolList)}")



