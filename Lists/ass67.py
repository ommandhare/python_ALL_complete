"""
Write a program to find duplicate number in a list without using setfunction

"""

list=[1,2,3,4,5,5,9]
seen=[]
duplicates=[]


for num in list:
     if num in seen:
        duplicates.append(num)
     else:
        seen.append(num)



if duplicates:
 print("duplicate values: ")
 print(duplicates)
else:
    print("no duplicates found")
