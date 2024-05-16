w="carrot"
wordList=["parrot","water"]

n=2
nList=[]
for i in range(len(w) - n + 1):
    ngram = ''
    for j in range(n):
        ngram += w[i + j]
    nList.append(ngram)

print(nList)

matched=[]
for word in wordList:
 for i in nList:
    if i in word:
        print(i,word)
        matched.append(i)
    print(matched)





