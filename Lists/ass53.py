"""
smallest difference between two numbers from two lists
(one number from each list). Input l1: [2,4,6,8], l2:[3,10,18,19]
.. Output is 1 for this example

"""

l1=[2,4,6,8]
l2=[3,10,18,19]
diffs=[]
min_diff=0
for i in l1:
    for j in l2:
       diff=i-j
       diffs.append(diff)
       min_diff=min(min_diff,diff)


print(diffs)
print(min_diff)