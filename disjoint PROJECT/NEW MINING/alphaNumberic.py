import re
path = r"C:\Users\om\PycharmProjects\python_All\disjoint PROJECT\item_descr.csv"
pathOut=r"C:\Users\om\PycharmProjects\python_All\disjoint PROJECT\measurements.csv"
aNumeric=[]
wordList=[]
for line in open(path):
    # print(line)
    desc = line.strip().split(",",2)
    # print(desc)
    desc=desc[1].split(",",1)
    # print(desc)
    str=''
    for let in desc:
        str+=let
    # print(str)
    numeric=re.findall(r"[0-9]+",str)
    # alphaNumeric=re.findall(r"[0-9]+[a-z,A-Z]+",str)
    alphaNumeric = re.findall(r"[0-9]+.?[a-z,A-Z]+", str) #joined or non join alpha numeric
    aNumeric.append(alphaNumeric)
    if not numeric:
      continue
    # wordList.append(result)
    # print(desc,"----",numeric)
    # print(alphaNumeric)


# print(aNumeric)

#getting measures.....

mList=[]
for item in aNumeric:
    if not item:
        continue
    else:
        str=''
        for let in item:
            str+=let
            result=re.findall(r"[0-9] .+",str)
            mList.append(result)

# print(mList)
measureDict={}
for i in mList:
    str=''
    for j in i:
        item=re.split(r" ",j)
        # print(item)
        for k in item:
            if k.isdigit():
                continue
            else:
               measure=re.split("[0-9]",k)
               for m in measure:
                   # print(m)
                   if not m:
                       continue
                   else:
                       if m in measureDict:
                           measureDict[m]+=1
                       else:
                           measureDict[m]=1

f=open(pathOut,"w")
for k,v in measureDict.items():
    f.write(f"{k},~{v}\n")
    print(k,v)

f.close()
