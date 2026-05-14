import pandas as pd
import csv

def loadSet(output, input):
    for wd in input:
        output.add(wd)

def nGram(s:str, n:int) -> list[str]:
    lst=[]
    for i in range(len(s) - n + 1):
        lst.append(s[i:i + n])
    return lst

def genSynonymsData(word, wordLenDict, wordCntDict):
    baseWd = word
    wordSize = len(word)
    allDataSet = set()
    for i in range(wordSize-2, wordSize+3):
        if i in wordLenDict and word[0] in wordLenDict[i]:
            loadSet(allDataSet, wordLenDict[i][word[0]])

    simList=[]
    for target in allDataSet:
        similarity= nGramSimilarity(baseWd,target)
        if similarity > 0.75:
            if int(wordCntDict[target]) > int(wordCntDict[baseWd]):
                baseWd = target

            simList.append(target)

    return baseWd, simList

def nGramSimilarity(w1, w2, n=2):

    ng1 = set(nGram(w1.lower(), n))
    ng2 = set(nGram(w2.lower(), n))

    common = ng1.intersection(ng2)

    similarity = len(common) / max(len(ng1), len(ng2))

    return similarity


path= r"/LinkedIn/Word Count.csv"

wordCntDict ={}
wordLenDict = {}
wordLst=[]
cnt=0
for datatuple in open(path):
   if cnt==0:
       cnt+=1
       continue
   # print(datatuple)
   word,count=datatuple.strip().split(",")
   if len(word) < 3:
       continue
   wordCntDict[word]= count
   wordLst.append(word)

   if len(word) not in wordLenDict:
       wordLenDict[len(word)] = {word[0] : {word}}
   else:
       if word[0] not in wordLenDict[len(word)]:
           wordLenDict[len(word)][word[0]]={word}
       else:
           wordLenDict[len(word)][word[0]].add(word)

# print(wordCntDict)
#
# print(wordLenDict)
#
# print(cleanWordLst)

wordLst.sort(key= lambda x:wordCntDict[x], reverse=True)

# print(cleanWordLst)
wordBaseWordDict={}
for word in wordLst:
    if word in wordBaseWordDict:
        continue
    baseWd, simList = genSynonymsData(word,wordLenDict,wordCntDict)

    for wd in simList:
        wordBaseWordDict[wd] = baseWd

        if wd in wordLenDict[len(wd)][wd[0]]:
            wordLenDict[len(wd)][wd[0]].remove(wd)

allData=[]
for word, baseWd in wordBaseWordDict.items():
    allData.append([word,baseWd])


df = pd.DataFrame(allData, columns=['word', 'base'])

df.to_csv("base_word.csv", index=False)

