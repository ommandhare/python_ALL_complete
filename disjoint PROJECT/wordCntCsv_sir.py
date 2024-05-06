path=r"C:\Philomath\pocPSec\item_o.csv"
pathD=r"C:\Philomath\pocPSec\wordCnt0405.txt"
countLines = 0
wordDict = {}
def addToWordDict(w,wDict):
    if(w in wDict):
        cnt = wDict[w]
        cnt +=1
        wDict[w] = cnt
    else:
        wDict[w] = 1

def getLastIndex(l,pt):
    size = len(l)
    li = size-1
    for i in range(size):
        if(line[li-i] == pt):
            return (li-i)

for line in open(path):
    cols = line.strip().split(",")
    if(len(cols) > 3):
        idx = line.find(",")
        rIdx = line.rfind(",")
        wd = line[idx+1:rIdx]
    else:
        wd = cols[1]
    words = wd.split(" ")
    for word in words:
       addToWordDict(word,wordDict)

print(wordDict)
f = open(pathD,"a")
for k,v in wordDict.items():
    lStr = k + "~" + str(v) + "\n"
    f.write(lStr)
f.close()


#print(countLines)
    #print(line,end="")