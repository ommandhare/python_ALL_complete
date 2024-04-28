## repetation or iteration or loop
"""
print("NUMBER: ",1)
print("NUMBER: ",2)
print("NUMBER: ",3)
print("NUMBER: ",4)
print("NUMBER: ",5)
print("NUMBER: ",6)
print("NUMBER: ",7)
print("NUMBER: ",8)
print("NUMBER: ",9)
print("NUMBER: ",10)
"""
## same problem solved using loop
# range function - range(n) -  generates list of numbers between 0 and n-1
# range(n) --> [0,1,2,3,.....,n-1]
print("Print Number using for loop")
for num in range(10):
    print("NUMBER: ",num+1)

## same problem can be solved by a while loop
## while loop iterates or repeats certain lines of code until a condition is met
num=1
while(num<=1000):
    print("NUMBER - WHILE LOOP: ",num)
    num = num + 1

print("OUT OF WHILE LOOP AT NUM = ",num)



