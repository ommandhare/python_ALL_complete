path=r"C:\Users\om\PycharmProjects\python_All\RADAR\category.csv"
wordDict={}
cnt=0
for line in open(path):
    if cnt==0:
        cnt+=1
        continue
    words=line.strip().split(",")
    for word in words:
        # print(word)
        if word in wordDict:
            wordDict[word]+=1
        else:
            wordDict[word]=1

print(wordDict)
with open("category_count.csv","w") as f:
    f.write(f"category,size,Frequency\n")
    for category,size in wordDict.items():
     f.write(f"{category},{1},{size}\n")

f.close()