import re

str=[['5 FLUID'],
['4 PACK'],
['0 FLUID']]

List=[]

for i in str:
    for j in i:
        item=j.strip().split(" ")
        List.append(item)

print(List)


for i in List:
    for j in i:
        print(j)
