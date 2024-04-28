"""
Get a number from user, write a program to calculate factorial of the number using for loop and while loop

"""

num=int(input("enter the number: "))
fact=1;
for i in range(1,num+1):

    fact=fact*i

print("factorial value: ",fact)
