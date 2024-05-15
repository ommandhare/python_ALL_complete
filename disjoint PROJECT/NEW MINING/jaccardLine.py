path=r"C:\Users\om\PycharmProjects\python_All\disjoint PROJECT\realSample.txt"

setList=[]

for line in open(path):
    str=''
    desc=line.strip().split(",",2)
    desc=desc[1]
    # print(desc)
    words=desc.split(",")
    # print(words)
    for word in words:
        # print(word)
        for let in word:
            # print(let)
            str+=let
    strSet=set(str)
    setList.append(strSet)

# print(setList)


sWord="BOLTHOUSE FARMS STRAWBERRY PARFAIT BREAKFAST SMOOTHIE"
swordSet=set(sWord)

print(swordSet)
cnt=0
for i in setList:
    cnt+=1
    inter=i.intersection(sWord)
    union=i.union(sWord)
    jaccard=len(inter)/len(union)
    if jaccard==1:
     print(f"no.{cnt}---{i}---{jaccard}")


