def get_bkt_index(freq):
    # index 0 - freq less than eq 10
    # index 1 - freq less than eq 20
    # index 2 - freq less than eq 50
    # index 3 - freq less than eq 100
    # index 4 - freq greater than 100
    if(freq <= 10):
        return 0
    elif(freq <= 20):
        return 1
    elif(freq <= 50):
        return 2
    elif(freq <= 100):
        return 3
    else:
        return 4

def getImportantWordCount(idList,idDict,impDict):
    impWdCnt = 0
    for id in idList:
        wd = idDict[id].word
        # print("WORD: ",wd)
        if(wd in impDict):
            # print("WORD FOUND IN IMPDICt: ",wd)
            impWdCnt +=1
    return impWdCnt
####--------------------------
def checkIgnoreComb(idList,idDict,ignoreDict):
    #ignFlag = 0
    for id in idList:
        #print("inside check")
        wd = idDict[id].word
        #print("ID: ",id, "WORD: ",wd)
        if(wd not in ignoreDict):
            return 0
        # else:
            # print("IGNORE WORD FOUND")
    return 1


def addListToCombList(comb, combList):
    tempList = []
    for item in comb:
        tempList.append(item)
    combList.append(tempList)


def combinGen(n, r, lst, lvl, idx, comb, combList):
    beginIndex = idx
    # 5c3 == 3 + 0, 3+1, 3+2
    # 5c2 == 4 + 0, 4 + 1
    endIndex = n - r + 1 + lvl
    if (lvl == r):
        # print("LEVEL ===== R")
        return
    else:
        for i in range(beginIndex, endIndex):
            comb[lvl] = lst[i]
            if (lvl == (r - 1)):
                addListToCombList(comb, combList)
            combinGen(n, r, lst, lvl + 1, i + 1, comb, combList)


def findInList(w, l):
    for wd in l:
        if (w == wd):
            return 1
    return 0


def sortList(wordList, size):
    for i in range(0, size - 1):
        for j in range(i + 1, size):
            if (wordList[i].freq < wordList[j].freq):
                t = wordList[i]
                wordList[i] = wordList[j]
                wordList[j] = t

