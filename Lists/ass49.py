"""
start with a hard coded list a = [3,4,5,86,34,2,3,4,7,33,44,66,88,34,32,11,22] and write a program (bubble sort) to sort the list in descending order - bubble sort

"""

a = [3,4,5,86,34,2,3,4,7,33,44,66,88,34,32,11,22]
n=len(a)
print("non sorted list")
for line in a:
    print(line)

for i in range(n):
    for j in range(0,n-1):
        if a[j] < a[j + 1]:
            temp = a[j]
            a[j] = a[j + 1]
            a[j + 1] = temp


print("\n descending sorted list\n")

for result in a:
    print(result)


