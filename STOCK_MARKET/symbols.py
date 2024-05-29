

path=r"C:\Users\om\PycharmProjects\python_All\STOCK_MARKET\preopen.csv"
cnt=0
symbolList=[]
for line in open(path):
    if cnt==0:
        cnt+=1
        continue
    desc=line.strip().split(",")
    desc=desc[0]
    symbolList.append(desc)


print(symbolList)
print(len(symbolList))