path=r"C:\Users\om\PycharmProjects\python_All\disjoint PROJECT\realSample.txt"

setList=[]
for line in open(path):
    desc=line.strip().split(",")
    desc=desc[1]
    words=desc.split(" ")
    for word in words:
        # print(word)
        setword=set(word)
        setList.append(setword)

# print(setList)


sWord="OUNCE"
swordSet=set(sWord)

for i in setList:
    inter=i.intersection(sWord)
    union=i.union(sWord)
    jaccard=len(inter)/len(union)
    if jaccard==1:
     print(f"{i}---{jaccard}")


