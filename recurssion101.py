def printNum(n):
    print("NUMBER n:",n)
def printNumRecur(n,lvl):
    if(n==0):
        return
    else:
        print("LEVEL: ",lvl,"NUMBER N: ",n)
        printNumRecur(n-1,lvl+1)
def factRecur(n):
    if(n==1):
        return 1
    else:
        print("FACT N:",n," =",n,"* FACT(",n-1,")")
        fact =  n*factRecur(n-1)
        print("FACT N=",n," = ",fact)
        return fact
n = 10
printNum(n)
#printNumRecur(n,0)
fact = factRecur(10)