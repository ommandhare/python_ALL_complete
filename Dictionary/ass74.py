"""
Three number sum: input list l1 = [2,18,11,23,34,3,22] ..
 Write a program to find out three numbers that have sum = 43

"""

a=[2,18,11,23,34,3,22]

nums=[]
dict={}
for i in a:
    for j in a:
        for k in a:
            sum= i + j + k
            if (sum==43):
                nums.append([i,j,k])
                dict[sum]=nums




print(dict)