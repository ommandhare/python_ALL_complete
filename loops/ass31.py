"""
print patterns -- NUMBERS sequence right angeled

"""

n = 5
num = 1

for i in range(0, n):
    for j in range(0, i + 1):
        print(num, end=" ")
        num = num + 1
    print(" ")
