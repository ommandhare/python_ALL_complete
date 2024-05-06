path=r"C:\Philomath\pocPSec\wordCnt0405.txt"
pathOut=r"C:\Philomath\pocPSec\size2Comb.csv"
class wordSet:
    def __init__(self, wd, cnt,id):
        self.ws = wd
        self.freq = cnt
        self.id = id

cntRangeDict = {}
wList = []
def getCntRange(n):
    if(n <= 50):
        return 50
    elif(n<=100):
        return 100
    elif(n<=500):
        return 500
    elif(n<=1000):
        return 1000
    elif(n<=3000):
        return 3000
    else:
        return 3001

def addToDict(v,dct):
    if(v in dct):
        dct[v] +=1
    else:
        dct[v] = 1
for line in open(path):
    wd,cnt = line.strip().split("~")
    cnt = int(cnt)
    if(len(wd)<3):
        continue
    if(cnt>=100):
        tempWs = wordSet(wd,cnt,0)
        wList.append(tempWs)
    #print("WORD: ",wd)
    #print("CNT: ",cnt)
    rng = getCntRange(cnt)
    addToDict(rng,cntRangeDict)

print(cntRangeDict)
#print(wList)
wSList = sorted(wList,key=lambda obj:obj.freq,reverse=True)
size = len(wSList)
for i in range(size):
    w = wSList[i]
    w.id = i+1
    print("WORD ID: ",w.id," WORD: ",w.ws," FREQ: ",w.freq)