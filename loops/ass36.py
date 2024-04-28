"""
get a number from user and check if the number is perfect square.

"""
num=int(input("enter the number: "))
sqrt_num = num ** 0.5
if sqrt_num.is_integer():
    print("The provided number is a perfect square")
else:
    print("The provided number is not a perfect square")