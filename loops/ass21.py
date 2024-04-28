"""
get a list a = [2,3,4,55,33,4,55,343,66,77,88,99] and write a program to browse over this list and print previous number and current number

"""
a = [2, 3, 4, 55, 33, 4, 55, 343, 66, 77, 88, 99]

# Iterate through the list, starting from the second element (index 1)
for i in range(1, len(a)):
    previous_number = a[i - 1]
    current_number = a[i]
    print(f"Previous Number: {previous_number}, Current Number: {current_number}")



