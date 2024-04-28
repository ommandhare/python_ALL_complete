"""
Ask user to enter 2 lists of 5 elements each (user should enter as comma separated string), generate lists from the strings and check if two lists entered by user are same

"""

a=[]
b=[]
equal=True
print("Enter A list ")
for i in range(0,5):
    ele=int(input())
    a.append(ele)

print("Enter B list ")
for i in range(0,5):
    ele=int(input())
    b.append(ele)



for j in range(5):
    if a[j]!=b[j]:
        equal=False

print(a)
print(b)


if equal:
    print("LIST ARE EQUAL")
else:
    print("LIST ARE NOT EQUAL")




