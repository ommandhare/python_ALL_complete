"""
get a string from user and write a function to return 1st non repeating character
(if 1st character is not repeating then return -1)

"""

string=input("Enter the string ")
seen=[]
repeating=[]


for i in string:
     if i in seen:
        repeating.append(i)
        seen.append(i)
     else:
        seen.append(i)



print("Seen ::",seen)
if(repeating[0]==string[0]):
    print(-1)
else:
    print("first repeating char",repeating[0])
