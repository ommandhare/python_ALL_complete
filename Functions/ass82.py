"""
write a function to study pass by value and pass by reference (write a function that accepts one variable and one list,
 increment variable inside the function by 1 and print the variable inside function and print variable before and after
  function call. inside function add 3 to all the elements of the list. print list inside function and before and after
  function call)

"""

a=15
b=10
def passbyvalue(a,b):
    c=a+b
    print("sum by pass value: ",c)

def passbyreference():
    c=a-b
    print("substraction by pass refrence : ",c)

print("PASS BY VALUES")
passbyvalue(2,4)
print("\n")
print("PASS BY REFRENCE")
passbyreference()
