"""
You are given two positive integers
1. Height of ladder and
2. Max number of steps
you can take at a time to reach the top.
Write a program to list all possible ways in which one can reach to the top of the ladder.

"""

def climb(ht,steps,cnt):
     if ht==0:
         print("Climbed",cnt)
         return
     elif steps > ht:
        climb(ht,steps-1,cnt)
     else:
         climb(ht-steps,steps,cnt+1)

climb(50,5,0)



