"""
Get a number from user and check if number is twin prime number

"""

def is_prime(num):
    i = 2
    count = 0
    while i < num:
        if (num % i == 0):
            count = 1
            break
        i += 1
    if count == 1:
        return False
    else:
        print("prime")
        return True

def is_twin_prime(num):
    if is_prime(num):
        return (is_prime(num - 2) or is_prime(num + 2))
    return False

num = int(input("Enter a number: "))

if is_twin_prime(num):
    print(f"{num} is a twin prime number.")
else:
    print(f"{num} is not a twin prime number.")
