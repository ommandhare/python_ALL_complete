"""
IT FINDS FIRST NGRAMS IN CLEANED DATA  AND RETURN WORD WHICH HAVE FIRST NGRAM OF PARTTICULAR WORDS
"""

path=r"C:\Users\om\PycharmProjects\python_All\disjoint PROJECT\cleanedData.csv"

worda=("strawberry")
worda=worda.upper()
List=[]
n=3

for i in range(len(worda)-n+1):
     ngram=''
     for j in range(n):
         ngram+= worda[i+j]
     List.append(ngram)

print(List)

firstGram=List[0]
secondGram=List[1]
print(firstGram)
print(secondGram)

nDict={}
fList=[]
for line in open(path):
    words=line.strip().split(",")
    # print(words)
    for word in words:
        # print(word)
        if (firstGram in word[:3] and secondGram in word[:6]):
             fList.append(word)


print(fList)




