path=r"C:\Users\HP\PycharmProjects\pythonProject.py\venv\Assignments\sqlGen\casewhen.csv"

def getbuckeList(mn,mx,bktList):
    intercept = mx -mn
    bktList.append(mn)
    while(intercept > bkt):
        mn =mn + bktList
        bktList.append(mn)
        intercept = mx -mn
        bktList.append(mx)

bktDict={}

cnt=0
for line in open(path):
    if(cnt==0):
        cnt+=1
        continue
    print(line)
    fact,minFact,maxFact,bktSize = line.strip().split(",")
    minFact =float(minFact)
    maxFact = float(Fact)
