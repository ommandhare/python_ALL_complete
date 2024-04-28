"""
write a program to compute factorial of a number using function

"""

num=int(input("enter the number :"))

def factorial(n):
    for i in range(1,n):
        n=n*i

    print(n)

factorial(num)