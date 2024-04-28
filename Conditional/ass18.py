"""
get three sides of a triangle from user and check if that is a valid triangle

"""

a=float(input("enter a side: "))
b=float(input("enter b side: "))
c=float(input("enter c side: "))

if(a+b>c) and (b+c>a) and (a+c>b):
    print("Valid triangle")
else:
    print("invalid triangle")
