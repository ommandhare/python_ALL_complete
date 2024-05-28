
path = r"C:\Users\om\PycharmProjects\python_All\RADAR\KIRAN\cleanData.csv"

wordDec ={}

with open(path) as fp:
    cnt = -1
    for line in fp:
        if cnt == -1:
            cnt+=1
            continue
        lineList = line.strip().split()
        for word in lineList:
            if word not in wordDec:
                wordDec[word] = 1
            else:
                wordDec[word]+=1

wordCntList = []
for wd,cnt in wordDec.items():
    wordCntList.append((wd,cnt))
wordCntList=sorted(wordCntList,key=lambda obj:obj[1],reverse=True)

hdr = 'word,id,cnt\n'
file = open(r'wordId.csv','w')
file.write(hdr)
id = 1
for wd,cnt in wordCntList:
    file.write(f"{wd},{id},{cnt}\n")
    id+=1
file.close()