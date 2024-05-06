path=r"C:\Philomath\pocPSec\wordCnt0405.txt"
pathOut=r"C:\Philomath\pocPSec\lengthAnalysis.csv"
class wordSet:
    def __init__(self, wd, cnt,id):
        self.ws = wd
        self.freq = cnt
        self.id = id

wordLengthDict = {}
wList = []
def addToDict(v,dct):
    if(v in dct):
        dct[v] +=1
    else:
        dct[v] = 1
for line in open(path):
    wd,cnt = line.strip().split("~")
    #print("WORD: ",wd," CNT: ",cnt)
    s = len(wd)
    if(s>25):
        print("#$#$#$#$#$###$##")
        print(wd)
        print("#$#$#$#$##$#$#$#$#")
    addToDict(s,wordLengthDict)

print(wordLengthDict)
f = open(pathOut,"a")
for l,cn in wordLengthDict.items():
    lnStr = str(l) + "," + str(cn) + "\n"
    f.write(lnStr)
f.close()