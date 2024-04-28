"""
two - number sum:input list l1 = [2,18,11,23,34,3,22]
Write a program to find out two numbers that have sum = 45

"""

a=[2,18,11,23,34,3,22]

nums=[]
dict={}
for i in a:
    for j in a:
        sum= i + j
        if (sum==45):
            nums.append([i,j])
            dict[sum]=nums


print(nums)


print(dict)