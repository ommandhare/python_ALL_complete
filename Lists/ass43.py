"""
ask user to enter a string, ask user to enter a character, write a program to check number of occurances of that character in the string given by user.

"""

str=input("enter the string: ")
char=input("enter character")
flag=0
for i in range(len(str)):
    if(char==str[i]):
        flag=flag+1



if(flag==0):
    print("character is not in string")
else:
    print("total occurances: ",flag)