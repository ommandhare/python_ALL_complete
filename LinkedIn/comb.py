import pandas as pd
import csv
import re
import unicodedata

path=r"C:\Users\Om Mandhare\PycharmProjects\python_ALL_complete\LinkedIn\connections.csv"
posLst=[]
comLst=[]
wordLst=[]
nameLst=[]
roleWrdDict={}
wordDict={}
comDict={}
wordIdDict={}
idToWord={}
newCombList=[]
cleanWordList=[]
cnt=0

class ItemSet:
    def __init__(self,id,word,freq):
        self.id = int(id)
        self.word = word
        self.freq =  int(freq)

def getWordList(wrd,wl):
    pattern =r'[A-Za-z]+'
    tmpWdLst=re.findall(pattern,wrd)
    for word in tmpWdLst:
        wl.append(word)

def addListToCombList(comb,combList):
    tempList =[]
    for item in comb:
        tempList.append(item)
    combList.append(tempList)


def combigen(n,r,lst,lvl,idx,comb,combList):
    beginIndex= idx
    endIndex=n-r+1+lvl
    if(lvl==r):
        return
    else:
        for i in range(beginIndex, endIndex):
            comb[lvl] = lst[i]
            if(lvl == (r -1)):
                addListToCombList(comb,combList)
            combigen(n,r,lst,lvl+1,i+1,comb,combList)




def clean_text(txt):
    txt = str(txt)

    # Remove corrupted UTF patterns
    txt = re.sub(r'â\S*', ' ', txt)

    # Normalize unicode
    txt = unicodedata.normalize('NFKD', txt)

    # Convert accented chars to ASCII
    txt = txt.encode('ascii', 'ignore').decode('utf-8')

    # Replace &
    txt = txt.replace("&", "and")

    # Keep only letters/numbers/spaces
    txt = re.sub(r'[^A-Za-z0-9 ]', '', txt)

    # Remove extra spaces
    txt = " ".join(txt.split())

    return txt

def sortlist(wordList,size):
    for i in range(0, size-1):
        for j in range(i+1,size):
            if(wordList[i].freq < wordList[j].freq):
                t=wordList[i]
                wordList[i]=wordList[j]
                wordList[j]=t



with open(path, newline='', encoding='utf-8') as file:
    reader = csv.reader(file)

    for line in reader:
        if cnt == 0:
            cnt += 1
            continue

        First_Name, Last_Name, URL, Email_Address, Company, Position, Connected_On = line

        posLst.append(Position)
        comLst.append(Company)
        nameLst.append(First_Name)



# print(posLst)

for role in posLst:
    clean_role = role.replace("(", "") \
        .replace(")", "") \
        .replace(",", "") \
        .replace("'", "") \
        .replace("/", " ")

    words = clean_role.split()
    for word in words:
        # print(word)
        wordLst.append(word)

# print(cleanWordLst)

for word in wordLst:
    if len(word)==1 or word=="and":
        continue
    else:
        if word not in roleWrdDict:
            roleWrdDict[word] = 1
        else:
            roleWrdDict[word] += 1

# print(roleWrdDict)


for company in comLst:

    company=clean_text(company)

    if company not in comDict:
        comDict[company] = 1
    else:
        comDict[company] += 1



cnt=-1
for datatuple in list(roleWrdDict.items()):
    cnt+=1
    word,freq=datatuple
    if(len(word)<3):
        continue
    if(int(freq)<2):
        continue
    tempItemSet = ItemSet(cnt, word, freq)
    wordDict[word]=tempItemSet
    wordIdDict[int(cnt)] = tempItemSet
ctt=0
with open(path, newline='', encoding='utf-8') as file:
    ctt+=1
    combList=[]
    reader = csv.reader(file)

    for line in reader:
        if cnt == 0:
            cnt += 1
            continue

        First_Name, Last_Name, URL, Email_Address, Company, Position, Connected_On = line

        if(len(Position)<2):
            continue
        wList=[]
        # print(Position)

        getWordList(Position,wList)
        # print(wList)

        desWords=[]
        for word in wList:
            if word in wordDict:
                cleanWordList.append(word)
                desWords.append(wordDict[word])
        size=len(desWords)

        sortlist(desWords, size)

        itemList=[]
        for wordObj in desWords:
            # print(f"{wordObj.id}__{wordObj.word}")
            itemList.append(wordObj.id)
            n = len(itemList)

            r=2 #comb_size
            comb=[]
            for i in range(r):
                comb.append(0)
            combigen(n,r,itemList,0,0,comb,combList)

            idToWord = {}

            for word in wordDict:
                obj = wordDict[word]

                idToWord[obj.id] = obj.word

            for comb in combList:
                words=[]
                for id in comb:
                    words.append(idToWord[id])
            joinedCombination="_".join(words)
            print(f"{comb}___{joinedCombination}")
            newCombList.append(joinedCombination)






print(cleanWordList)
print(newCombList)

dfwords = pd.DataFrame(cleanWordList).drop_duplicates()

dfcombination = pd.DataFrame(newCombList).drop_duplicates()

with pd.ExcelWriter("combinations.xlsx") as writer:
    dfwords.to_excel(writer, sheet_name="words", index=False)
    dfcombination.to_excel(writer, sheet_name="2_size_combinarion", index=False)

print("Excel genrated")




