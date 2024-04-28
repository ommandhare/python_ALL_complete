"""
get number from user and check if number is odd or even, multiply number by 2 is number is even and calculate square of the number if number is odd

"""

num=int(input("enter the number: "))

if(num%2==0):
    print("numer is even")
    prod=num*2
    print("product of number is: ",prod)
else:
    print("numer is odd")
    prod = num * num
    print("square of even number is: ",prod)