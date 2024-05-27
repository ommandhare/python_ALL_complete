import re
path=r"C:\Users\om\PycharmProjects\python_All\RADAR\internet_Sample.csv"

aNumeric=[]
for line in open(path):
    desc = line.strip().split(" ")
    # print(desc)
    for word in desc:
     alphaNumeric=re.findall(r"[0-9]+.?[a-z,A-Z]+", word)
     if alphaNumeric:
         aNumeric.append(alphaNumeric)
         for i in alphaNumeric:
          numbers=re.findall(r"[0-9]+",i)
          alpha=re.findall(r"[A-Z]+",i)
          # print(alphaNumeric)
          # print(numbers)
          # print(alpha)

#
print(aNumeric)
# print(len(aNumeric))



