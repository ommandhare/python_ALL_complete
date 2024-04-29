path=r"C:\Users\om\PycharmProjects\python_All\disjoint PROJECT\sample.txt"

word="ommandhare"
List=[]
n=2

for i in range(len(word)-n+1):
     ngram=''
     for j in range(n):
         ngram+= word[i+j]
     List.append(ngram)

print(List)
nDict={}
cnt=0
with open(path, 'r') as file:
    next(file)
    for line in file:
        # print(line)
        desc = line.strip().split(",", 1)
        if len(desc) > 1:  # Check if there are at least two fields
            words = desc[1].strip().split(" ")
            for word in words:
                # print(word)
                for key in List:
                    cnt=0
                    if key in word:
                        nDict[key]=word



print(nDict)