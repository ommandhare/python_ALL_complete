def getWordList(path):
    wordList = []
    with open(path, 'r') as file:
        next(file)
        for line in file:
            # print(line)
            desc = line.strip().split(",", 1)
            if len(desc) > 1:  # Check if there are at least two fields
                words = desc[1].strip().split(" ")
                for word in words:
                    # print(word)
                    wordList.append(word)
    return wordList


def getSameword(wordList, word):
    cnt = 0
    for idx in wordList:
        if idx == word:
            cnt += 1
            print(idx)

    print("result::::")
    if cnt > 1:
        print(f"{word} founded {cnt} times")
    elif (cnt == 1):
        print(f"{word} is single in list")
    else:
        print(f"{word} not found in list")


def getSubset(wordList, word):
    subsetList = []

    print("INSIDE SUBSET::::")
    for key in wordList:
        # print(key)
        if word == key:
            continue
        elif word in key:
            subsetList.append(key)
    return subsetList


def nGrams(word,n):
    nGramList=[]
    for i in range(len(word) - n + 1):
        ngram = ''
        for j in range(n):
            ngram += word[i + j]
        nGramList.append(ngram)
    # print(nGramList)
    return nGramList

def getNgramWords(word,ngramlist):
    nDict={}
    with open(path, 'r') as file:
        next(file)
        for line in file:
            # print(line)
            desc = line.strip().split(",", 1)
            if len(desc) > 1:  # Check if there are at least two fields
                words = desc[1].strip().split(" ")
                for word in words:
                    #print(word)
                    for key in ngramlist:
                        if key in word:
                            # print(key, "---", word)
                            if key not in nDict:
                                nDict[key]=[word]
                            else:
                                nDict[key]+=[word]
        print(nDict)

path = r"C:\Users\om\PycharmProjects\python_All\disjoint PROJECT\sample.txt"


sWord = "veer"
n=2

wordList = getWordList(path)

print("\n###############################")
print("GETING SAME WORDS")
getSameword(wordList, sWord)

print("\n######################################")
subsetList=getSubset(wordList, sWord)
print(subsetList)

print("\n#######################################")
print("NGRAM AND WORDS WHICH CONTAINS NGRAMS")
nGramWords=nGrams(sWord,n)
getNgramWords(sWord,nGramWords)