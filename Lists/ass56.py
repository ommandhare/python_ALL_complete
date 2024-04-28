"""
move elements to last.
- input l1:[2,3,5,6,7,2,4,2,6,2,3,9,7] and
number given is 2 ---
move all instances of 2 to end of the list
==> l1:[3,4,5,6,7,4,6,3,9,7,2,2,2,2]

"""
a=[2,3,5,6,7,2,4,2,6,2,3,9,7]
twos=[]
numbers=[]
List=[]
for i in a:
    if i==2:
        twos.append(i)
    else:
         numbers.append(i)

List=numbers+twos

print(List)


