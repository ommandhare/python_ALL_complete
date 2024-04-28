"""
start with hard coded list say a = [12,3,34,45,88,23,45,63,3,4,69,99], get two numbers from user, store them in second list. Write a program to check if sencond list is subset of first list. Print the output

"""

a = [12,3,34,45,88,23,45,63,3,4,69,99]
b=[]

subset=True

print("Enter B ")
for i in range(0,2):
    ele=int(input())
    b.append(ele)


    for ele in b:
        if ele not in a:
            subset=False
            break;




print("A list",a)
if(subset==True):
    print("B is subset of A")
else:
    print("B is NOT subset of A")

print("B list",b)


