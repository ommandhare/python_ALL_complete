import re
str="my name is 12om13 mandhare"



data=str.split(" ")

for i in range(len(data)):
    match=re.findall(r"\b(?=(?:[A-Za-z]*\d)[A-Za-z\d]*)\w+\b",data[i])
    if match:
     alpha = re.findall(r"[^0-9]+", data[i])
     num =alpha + re.findall(r"[0-9]+", data[i])
     # print(num)
     data[i]=num[0]
     for j in range(1, len(num)):
         data.insert(i+j,num[j])

print(data)
new=""
for word in data:
    new+=word+" "

print(new)


