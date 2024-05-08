path=r"C:\Users\om\PycharmProjects\python_All\disjoint PROJECT\cleanedData.csv"
pathOut=r"C:\Users\om\PycharmProjects\python_All\disjoint PROJECT\wordCount.csv"
def count_Words(path):
    cntDict={}
    for line in open(path):
        words=line.strip().split(",")
        # print(words)
        for word in words:
            # print(word)
            if word in cntDict:
                cntDict[word]+=1
            else:
                cntDict[word]=1
        return cntDict

wordCount=count_Words(path)
# print(wordCount)


f=open(pathOut,"w")
for k,v in wordCount.items():
    f.write(k+"~"+str(v)+"\n")

f.close()

print("file created for Word Count...\n")
print("total length of Word Count :::::",len(wordCount))

