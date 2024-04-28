"""
ask user to enter name, age and address and let user know if user can do voting

"""

name=input("enter the name: ")
age=input("enter the age: ")
age=int(age)
address=input("enter the address")

if(age>18):
    print("eligible for vote")
else:
    print("not eligible for vote")
    