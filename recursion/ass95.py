def n_C_r(n,r):
    return fact(n)/(fact(r)*fact(n-r))

def fact(n):
    if(n==0):
        return 1
    else:
     return n*fact(n-1)


n=int(input("Enter the N ::"))

r=int(input("Enter R ::"))



value=n_C_r(n,r)
print(value)
