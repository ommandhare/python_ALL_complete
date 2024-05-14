import re

path = r"C:\Users\om\PycharmProjects\python_All\disjoint PROJECT\item_descr.csv"

pathOut=r"C:\Users\om\PycharmProjects\python_All\disjoint PROJECT\CleanWord.txt"
# str='MARTHA WHITE CHOCOLATE CHIP 9 MUFFIN MIX'
# result=re.split(r"[^a-zA-Z\s]+",str)
# print(result)


wordList=[]
for line in open(path):
    # print(line)
    desc = line.strip().split(",")
    # print(desc)
    desc=desc[1].split(",")
    # print(desc)
    str=''
    for let in desc:
        str+=let
    # print(str)
    result=re.split(r"[^a-zA-Z\s]+",str)
    wordList.append(result)

# print(wordList)
finalWordList=[]
for set in wordList:
    # print(set)
    for wordls in set:
        words=wordls.strip().split(" ")
        for word in words:
            # print(word)
            finalWordList.append(word)

f=open(pathOut,"w")

for i in finalWordList:
    print(i)
    f.write(i+",")

f.close()