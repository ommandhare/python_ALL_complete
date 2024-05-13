import re

path = r"C:\Users\om\PycharmProjects\python_All\disjoint PROJECT\item_descr.csv"


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

print(wordList)