path = r"C:\PythonWork\sqlGen\bucketConfig.csv"
def getBucketList(mn,mx,bkt,bktList):
    intercept = mx - mn
    bktList.append(mn)
    while(intercept > bkt):
        mn = mn + bkt
        bktList.append(mn)
        intercept = mx - mn
    bktList.append(mx)

bktDict = {}
cnt=0
for line in open(path):
    if(cnt==0):
        cnt +=1
        continue
    print(line)
    fact,minFact,maxFact,bktSize,windowSeq = line.strip().split(",")
    fact = fact +"_" + windowSeq
    minFact = float(minFact)
    maxFact = float(maxFact)
    bktSize = int(bktSize)
    bktList = []
    getBucketList(minFact,maxFact,bktSize,bktList)
    bktDict[fact]=bktList

print(bktDict)
codeStr = "SUM(CASE WHEN fact >= lc AND fact < rc THEN 1 ELSE 0 END) as fact_lc_rc_cnt"
"""
SUM(CASE WHEN amt >= lc AND amt < rc THEN 1 ELSE 0 END) as amt_lc_rc_cnt,
SUM(CASE WHEN 
"""
for fact,bktList in bktDict.items():
    fact = fact.split("_")[0]
    lc = bktList[0]
    c=0
    for b in bktList[1:]:
        rc = b
        codStr = codeStr.replace("fact",fact).replace("lc",str(int(lc))).replace("rc",str(int(rc)))
        if(c==0):
            print(codStr)
            c +=1
        else:
            print(",",codStr)
        lc = b
