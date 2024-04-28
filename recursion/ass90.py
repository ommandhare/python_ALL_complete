"""
Write a program to get fibonaci number of given number

"""
def fibonacci(n):
    if n<=1:
        return n
    else:
        return fibonacci(n-1)+fibonacci(n-2)



n=int(input("Enter number "))


print(f"fibonnaci of {n} is {fibonacci(n)}")


