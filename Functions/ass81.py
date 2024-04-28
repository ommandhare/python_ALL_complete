"""
write a function to compare two lists, function should return 1 if lists are same and 0 if lists are not same

"""

list1=[1,2,3,4,5,6,7]
list2=[1,2,3,4,5,6,9]
flag=0
for i in list1:
    for j in list2:
        if(list1==list2):
            flag=0
        else:
            flag+=4

if(flag==0):
    print("list are same")
else:
    print("list are not same")