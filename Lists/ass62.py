

a=[4,6,2,5,9,3,6,3,8,1,9,3,5,3,5,9,2,2,6,7]

def findSteps(lst):
    final = len(a)
    i=0
    while i<final:
           step=a[i]
           print(step)
           i+=step



print("MINIMUM STEPS TO GO")
findSteps(a)