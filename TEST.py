w="carrot"
n=3
nList=[]
for i in range(len(w) - n + 1):
    ngram = ''
    for j in range(n):
        ngram += w[i + j]
    nList.append(ngram)

print(nList)

tWord="carroe"

matched=[]
for i in nList:
    if i in tWord:
        matched.append(i)

diff=len(matched)/len(nList)
print(diff*100)






