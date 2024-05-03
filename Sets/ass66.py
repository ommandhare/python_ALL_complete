"""
generate two lists (list a - size 10 and list b - size 8)
using random number generation (generate numbers between 10 to 20),
browse over the lists save numbers in two different sets
and findout intersection and union of the two sets.

"""
import random

a=[random.randint(10,20) for x in range(10)]

b=[random.randint(10,20) for x in range(8)]

print("SET A")
set_a=set(a)
print(set_a)

print("SET B")
set_b=set(b)
print(set_b)

intersection=set_a.intersection(set_b)

union=set_a.union(set_b)

print("INTERSECTION::::")
print(intersection)

print("UNION:::::")
print(union)
