"""
write a function to find factors of a number and add them in list

"""

num=int(input("enter the number : "))
factors=[]
def check_factors(n):
    for i in range(1,n+1):

        if(n%i==0):
         factors.append(i)
    print("factors of number",factors)

check_factors(num)