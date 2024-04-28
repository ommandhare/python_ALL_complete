"""
get 3 numbers from the user and find maximum
"""

a=int(input("enter the a "))
b=int(input("enter the b "))
c=int(input("enter the c "))

if(a>b and a>c):
    print("a is greater")
elif(b>a and b>c):
    print("b is greater")
else:
    print("c is greater")
