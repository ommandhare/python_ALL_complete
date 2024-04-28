"""
Ask user to enter two strings as command line arguments and check if 2nd string is subset of 1st string without using string functions

"""
from sys import argv
str1 = argv[1]
str2 = argv[2]
# str1=input("enter the string 1")
# print(type(str1))
#
# str2=input("enter the string 2")
# print(type(str2))

flag=0
for i in range(len(str1)):
    for j in range(len(str2)):
        if str1[i]==str2[j]:
            flag+=1



if flag==len(str2):
    print("substring")
else:
    print("not")       