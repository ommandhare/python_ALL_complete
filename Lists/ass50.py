"""
get a list a = [2,3,4,55,33,4,55,343,66,77,88,99]
write a program to find list of non adjacent numbers of every number.

"""

a = [1,2,3,4,5,6,7]
nonAdjacent = {}

for i in range(len(a)):
    for j in range(len(a)):
        if(j == i-1 or j==i or j== i+1):
            continue
        elif(a[i] not in nonAdjacent):
            nonAdjacent[a[i]]=[a[j]]
        else:
            if a[j] not in nonAdjacent[a[i]]:
             nonAdjacent[a[i]].append(a[j])



print(nonAdjacent)

