"""
write a program to check working of deep copy and shallow copy

"""

import copy

list=[1,2,3,4,[1,23,45,5]]


deep= copy.deepcopy(list)
print(deep,id(deep))

print("Change")
list[0]+=1
print(list[0])


print("result ")

print(list,id(list))
print(deep,id(deep))