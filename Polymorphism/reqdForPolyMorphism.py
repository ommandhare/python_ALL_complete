## keywards
## expressions
## operands
## operators -> +-*/,//,**



def addTwoThings(a,b):
    c = a + b
    return c

x="test"
y=str(2)
z = x+y
z = addTwoThings(x,y)
print(z)
a = 10
print(a)
b=[1,2,5,6,7,8,10]
print(b)
c = {"basic":0.3,"hra":0.2,"key":20}
print(c)

sizeList = len(b)
print(sizeList)
sizeDict = len(c)
print(sizeDict)

"""
## function name = myprint, indata type= int
def myprint(a):
      print(a)
## function name = myprint, indata = list
def myprint(a):
        print("[",end="")
        count=0
        for item in a:
            if(count==0):
                print(item,end="")
                count +=1
            else:
                print(", ",item,end="")
        print("]")
            
lop = input("Enter type of lef side operand (a + b): ")
rop = input("Enter type  of right side operand (a + b)")
if(lop=="int" and rop=="int"):
    print("Addition of two integers ")
elif(lop=="string" and rop=="string"):
    print("Addition of two strings")
else:
    print("can not add string and int comination")
"""