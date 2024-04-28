"""
write a function to get maximum element of list and second highest element in a list

"""

numList = [34,23,33,45,56,98,22,3,47,87,63]
## for loop helps us browsing over a collection
count=0
for num in numList:
    if(count==0):
        highest = num
        count +=1
        continue
    if(count==1):
        if(num>highest):
            secondHighest = highest
            highest = num
            count +=1
            continue
        else:
            secondHighest=num
            count +=1
            continue
    if(num>highest):
        secondHighest = highest
        highest = num
    elif(num>secondHighest):
        secondHighest=num


print("HIGHEST: ",highest)
print("SECOND HIGHEST: ",secondHighest)
print("##########################################")
count=0
size = len(numList)
for idx in range(size):
    if(idx==0):
        highest = numList[idx]
        hiIdx = idx
        #count +=1
        continue
    if(idx==1):
        if(numList[idx]>highest):
            secondHighest = highest
            highest = numList[idx]
            secondHi = idx
            #count +=1
            continue
        else:
            secondHighest=num
            count +=1
            continue
    if(numList[idx]>highest):
        secondHighest = highest
        secondHi = hiIdx
        highest = numList[idx]
        hiIdx = idx
    elif(numList[idx]>secondHighest):
        secondHighest=numList[idx]
        secondHi = idx

print("HIGHEST: ",highest, " at IDX: ",hiIdx)
print("SECOND HIGHEST: ",secondHighest," at IDX: ",secondHi)