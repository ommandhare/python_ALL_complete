"""
ask user to enter 10 numbers store them in list and print list, count the number of times 10 is present in the list and print the result

"""

# creating an empty list
lst = []
flag=0
# number of elements as input
n = int(input("Enter number of elements : "))

# iterating till the range
for i in range(0, n):
    ele = int(input())
    # adding the element
    lst.append(ele)
    if(ele==10):
        flag=flag+1


print(lst)
print("10s: ",flag)


