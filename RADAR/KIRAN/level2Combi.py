
indexPath = r'C:\Users\om\PycharmProjects\python_All\RADAR\KIRAN\transposed2.csv'
dataPath = r'C:\Users\om\PycharmProjects\python_All\RADAR\KIRAN\data2.csv'

file = []
with open(dataPath) as fp:
    next(fp)
    for line in fp:
        file.append(set(line.strip().split()))

print("file Buffered...")

index =[]
with open(indexPath) as fp:
    next(fp)
    for line in fp:
        line = line.strip().split(',')
        index.append(line[0])
print("index Buffered...")

comboList = []
for i in range(len(index)-1):
    for j in range(i+1,len(index)):
        cnt =0
        for wdSet in file:
            if index[i] in wdSet and index[j] in wdSet:
                cnt+=1
        if cnt > 0:
            comboList.append((index[i],index[j],cnt))
print("Great Combo Comput Done!!!!")

path =r'lvl2Index_om.csv'
header = 'Item1,Item2,Freq,Size\n'
with open(path,'w') as fp:
    fp.write(header)
    for wd1,wd2,cnt in comboList:
        fp.write(f"{wd1},{wd2},{cnt},{2}\n")

print("Done")
