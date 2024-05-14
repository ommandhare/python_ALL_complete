path=r"C:\Users\om\PycharmProjects\python_All\disjoint PROJECT\wordSample"


def getNgrams(w):
    w = w.upper()
    nList = []
    n = 3

    for i in range(len(w) - n + 1):
        ngram = ''
        for j in range(n):
            ngram += w[i + j]
        nList.append(ngram)

    # print(nList)
    return nList

def get_1_2_ngramList(firstGram,secondGram):
    fList=[]
    # print(firstGram,secondGram)
    for desc in open(path):
        words=desc.strip().split(",")
        for w in words:
            if (firstGram in w[:3] and secondGram in w[:6]):
                   fList.append(w)
    # print(fList)
    return fList



# making wordList from word file
wordList=[]
for i in open(path):
    words=i.strip().split(",")
    # print(words)
    for word in words:
        # print(word)
        wordList.append(word)


# getting 1 and 2 ngram matching list among
nDict={}
for word in wordList:
 # print(word)
 ngrams=getNgrams(word)
 # print(word)
 # print(ngrams)
 if len(ngrams)<2:
     continue
 else:
     fList=get_1_2_ngramList(ngrams[0],ngrams[1])
     if word not in nDict:
      nDict[word]=fList

for k,v in nDict.items():
    print(f"{k}:{v}")

