path=r"C:\Philomath\pocPSec\wordCnt0405.txt"
pathOut=r"C:\Philomath\pocPSec\lengthAnalysis.csv"
class word:
    def __init__(self, wd, fNg,ngL):
        self.ws = wd
        self.firstNG = fNg
        self.ngL = ngL

# Write a program to create
# list of n-grams of a given word
def getNGrams(wd,n):
    s = len(wd)
    nGrams = []
    for i in range(s-(n-1)):
        ng = wd[i:i+n]
        nGrams.append(ng)
    return nGrams
wrdDict = {}
cnt=0
for line in open(path):
    #print(line)

    w,c = line.strip().split("~")
    c = int(c)
    s = len(w)
    if(s>3 and s<8):
        cnt +=1
        #print(w)
        nG = getNGrams(w,3)
        #print(nG)
        tW = word(w,nG[0],nG)
        if(nG[0] in wrdDict):
            oL = wrdDict[nG[0]]
            oL.append(tW)
            wrdDict[nG[0]] = oL
        else:
            oL = []
            oL.append(tW)
            wrdDict[nG[0]] = oL
    else:
        continue

print(len(wrdDict))
for fN,ol in wrdDict.items():
    if(fN =="CAR"):
        for o in ol:
            print(o.ws)
