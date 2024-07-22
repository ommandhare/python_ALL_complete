list=[]

for i in range(5):
    item=input("enter the number...")
    list.append(item)

maximum=list[0]
for num in list:
    if num>maximum:
        maximum=num

print(list)