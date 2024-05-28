# this code separates all words and all alphanumeric values

import re
path=r"C:\Users\om\PycharmProjects\python_All\RADAR\internet_des.csv"
pathOut=r"C:\Users\om\PycharmProjects\python_All\RADAR\seperated(alphanumneric).csv"
newLineList=[]
aNumeric=[]


def separated_all_words(path):
  for line in open(path):
    desc = line.strip().split(" ")
    # print(desc)
    for i in range(len(desc)):
        # print(desc[i])
        match = re.findall(r"\b(?=(?:[A-Za-z]*\d)[A-Za-z\d]*)\w+\b", desc[i])
        if match:
            alpha = re.findall(r"[^0-9]+", desc[i])
            num = alpha + re.findall(r"[0-9]+", desc[i])
            # print(num)
            desc[i] = num[0]
            for j in range(1, len(num)):
                desc.insert(i + j, num[j])
            # print(desc)
    new=''
    for word in desc:
         if word.find(","):
             spl=word.split(",")
             for s in spl:
                 new+=s+" "
         else:
           new += s + " "
    newLineList.append(new)
  return newLineList


newLineList=separated_all_words(path)

# print(newLineList)
with open(pathOut,'w') as f:
 for line in newLineList:
    f.write(line+"\n")
f.close()
print("file saved as separated(alphanumeric)......")

