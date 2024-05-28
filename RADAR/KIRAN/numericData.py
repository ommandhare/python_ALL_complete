
idPath = r'wordId.csv'
dataPath = r'cleanData.csv'

wordIdDec = {}
with open(idPath) as fp:
    next(fp)
    for line in fp:
        wd,id,cnt = line.strip().split(',')
        if wd not in wordIdDec:
            wordIdDec[wd] = int(id)

file = []
with open(dataPath) as fp:
    next(fp)
    cnt = 0
    for line in fp:
        cnt+=1
        lineList = line.strip().split()
        for idx in range(len(lineList)):
            if lineList[idx] in wordIdDec:
                lineList[idx] = wordIdDec[lineList[idx]]
        file.append(lineList)
print(file)