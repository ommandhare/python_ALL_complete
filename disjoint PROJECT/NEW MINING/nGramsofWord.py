"""
IT FINDS FIRST NGRAMS IN CLEANED DATA  AND RETURN WORD WHICH HAVE FIRST NGRAM OF PARTTICULAR WORDS
"""

path=r"C:\Users\om\PycharmProjects\python_All\disjoint PROJECT\cleanedData.csv"

word=("carrots")
word=word.upper()
List=[]
n=3

for i in range(len(word)-n+1):
     ngram=''
     for j in range(n):
         ngram+= word[i+j]
     List.append(ngram)

print(List)

firstGram=List[0]
print(firstGram)


nDict={}
fList=[]
for line in open(path):
    words=line.strip().split(",")
    # print(words)
    for word in words:
        # print(word)
        if firstGram in word:
            fList.append(word)


print(fList)

