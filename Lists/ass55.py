"""
findout largest range - input: l1:[1,2,3,4,5,6,8,20,21,22,23,24,25,26,33,32,71,87,7]
------ hint sort list in ascending order… only consider those parts that are consecutive
"""


a=[1,2,3,4,5,6,8,20,21,22,23,24,25,26,33,32,87,7]
n=len(a)

for i in range(n):
    for j in range(0,n-1):
        if a[j] > a[j + 1]:
            temp = a[j]
            a[j] = a[j + 1]
            a[j + 1] = temp

print("SORTED LIST :::")
print(a)
count = 0
consecutiveList=[]

for i in range(n-1):
     if count==n-1:
       print("end list")
     else:
      next = i + 1
      if(next == next):
       print("consecutive",a[i],"@",count)
       consecutiveList.append(a[i])
      count+=1




print(consecutiveList)