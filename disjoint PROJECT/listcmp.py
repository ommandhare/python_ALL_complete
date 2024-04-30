a=[2,3,4,5,6,]
b=[6,8,98,66,5]
c=[6,3,5,66]
itemList=[]
resultList=[]
commList=[]
for i in a:
    itemList.append(i)

for i in b:
    itemList.append(i)


print(itemList)

for i in itemList:
    if i not in resultList:
        resultList.append(i)
    elif i in commList:
        continue
    else:
        commList.append(i)



print(commList)
# for i in itemList:
#     if i in resultList:
#         commList.append(i)
#     else:
#         resultList.append(i)
#
# print(commList)
#
# for j in b:
#     if j not in resultList:
#         resultList.append(j)
#     elif j in commList:
#         continue
#     else:
#         commList.append(j)
# print(commList)
