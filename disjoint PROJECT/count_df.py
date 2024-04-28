import pandas as pd

df=pd.read_csv(r"C:\Users\HP\PycharmProjects\pythonProject.py\venv\Assignments\disjoint PROJECT\item_desc.csv")
path=r"C:\Users\HP\PycharmProjects\pythonProject.py\venv\Assignments\disjoint PROJECT\item_desc.csv"
description=df['description']

# TOO COUNT THE OCCURANCE OF EACH WORD pandas
def count_occurance(desc):
    wordList=[]
    count=0
    for line in description:
        word=line.strip(" ")
        wordList.append(word)
        count+=1
    wordDict={}
    for line in wordList:
        word=line.strip().split(" ")
        # print(word)
        for w in word:
            # print(w)
            if w not in wordDict:
                wordDict[w]=1
            else:
                wordDict[w]+=1
    return wordDict
    # for k,v in wordDict.items():
    #     print(k,"==>",v)

def count_occurances(path):
    wordDict = {}
    with open(path, 'r') as file:
        for line in file:
            desc = line.strip().split(",")
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
def give_id(sortedList):
    sortedIdDict={}
    id=1
    for k in sortedList:
        sortedIdDict[id]=k
        id+=1
    return sortedIdDict



# FUNCTION CALLS

# COUNT OCCURANCES by df
wordDict=count_occurance(description)
# print(wordDict)


# COUNT OCCURANCES
wordDict=count_occurances(path)
print(wordDict)

# MAKING TUPLES
allList=[]
for k,v in wordDict.items():
   row=(k,v)
   allList.append(row)

# SORTED LIST
sortedList=sortList(allList)
# print(sortedList)

# GIVING ID TO EACH SORTED
sortedIdDict=give_id(sortedList)
# print(sortedIdDict)

#

file=[]
finalIdList=[]

for line in description:
    word = line.strip().split(" ")
    for i in range(len(word)):
      word[i]=sortedIdDict[word[i]]
    file.append(word)

# print(file)
# print(sortedIdDict)

# print(sortedIdDict.values())