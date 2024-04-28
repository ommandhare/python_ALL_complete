
# COUNT OCCURANCES
def countOccurances(path):
    wordDict = {}
    cnt=0
    with open(path, 'r') as file:
        next(file)
        for line in file:
            desc = line.strip().split(",",1)
            if len(desc) > 1:  # Check if there are at least two fields
                words = desc[1].strip().split(" ")
                for word in words:
                    if word not in wordDict:
                        wordDict[word] = 1
                    else:
                        wordDict[word] += 1
    return wordDict


# TO SORT THE RESULT/DICT/LIST
def sortList(list:list):
    sortedList=sorted(list,key=lambda word:word[1],reverse=True)
    return sortedList

# TO GIVE ID TO EACH SORTED
def giveId(sortedList):
    sortedIdDict={}
    id=1
    for k,v in sortedList:
        sortedIdDict[k]=id
        id+=1
    return sortedIdDict

#TO GET THE LIST FROM ORIGINAL
def getList(path):
    wordList = []
    finalDict = {}
    ls = []
    idList = []
    with open(path, 'r') as file:
        next(file)
        for line in file:
            desc = line.strip().split(",",1)
            if len(desc) > 1:  # Check if there are at least two fields
                sent = desc[1].strip().split(" ")
                # print(sent)
                ls.append(sent)
    return ls


# REPLACE ALL WORDS TO ID
def replaceId(sortedIdDict):
    for wl in ls:
        # print(wl)
        for idx in range(len(wl)):
            # print(wl[idx])
            # wl[idx]=sortedIdDict[wl[idx]]  not working
            wl[idx] = sortedIdDict.get(wl[idx], wl[idx])
    return ls


# SORTING ALL IDs
def sortIDs(idReplacedList):
    for line in idReplacedList:
        # print(line)
        for i in range(len(line)):
            # print(idx)
            for j in range(0, len(line) - i - 1):
                if line[j] < line[j + 1]:
                    line[j], line[j + 1] = line[j + 1], line[j]
    return idReplacedList


# GET TWO COMBINATION OF EACH VALUES
def combination(sortedIDs):
    comboDict={}
    for line in sortedIDs:
        # print(line)
        for i in line:
         pairList=[]
         for j in line:
             pairList.append(j)
         comboDict[i]=pairList
    return comboDict


# GET DISJOINTS FROM REST OF COMBINATION
def DISJOINT(comboDict):
    disjoint={}
    samplejoin={}
    set=[]
    setList=[]
    samplejoin=comboDict

    for k, v in samplejoin.items():
        for idx in v:
         setList.append(idx)

    for k,v in comboDict.items():
        newList=[]
        for s in setList:
            if s not in v:
              newList.append(s)
              disjoint[k]=newList


    print(disjoint)




# FUNCTION CALLS
path=r"C:\Users\HP\PycharmProjects\pythonProject.py\venv\Assignments\disjoint PROJECT\item_desc.csv"

# COUNT OCCURANCES
wordDict=countOccurances(path)
# print(wordDict)

# MAKING TUPLES
allList=[]
for k,v in wordDict.items():
   row=(k,v)
   allList.append(row)

# print(allList)


# SORTED LIST
sortedList=sortList(allList)
# print(sortedList)

# GIVING ID TO EACH SORTED
sortedIdDict=giveId(sortedList)
# print(sortedIdDict)

ls=getList(path)

# REPLACING WORD TO ID
idReplacedList=replaceId(sortedIdDict)
# print(idReplacedList)


sortedIDs=sortIDs(idReplacedList)
# print(sortedIDs)


comboDict=combination(sortedIDs)
# print(comboDict)

print("REST DONE:::")

DISJOINT(comboDict)