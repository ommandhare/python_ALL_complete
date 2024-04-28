"""
get a number from user, write a program to check if number is prime number

"""
num=int(input("enter the number: "))
i=2
count=0
while i<num:
    if(num%i==0):
        count=1
        break
    i+=1
if count==1:
    print("composite")
else:
    print("prime")
