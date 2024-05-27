import re
path=r"C:\Users\om\PycharmProjects\python_All\RADAR\internet_Sample.csv"
pathOut=r"C:\Users\om\PycharmProjects\python_All\RADAR\Cleaned(alphanumneric)"
newLineList=[]
aNumeric=[]
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
        # if re.match(r"[\w\s]", word):
         new += word + " "
    newLineList.append(new)

with open(pathOut,'w') as f:
 for line in newLineList:
    f.write(line+"\n")

f.close()