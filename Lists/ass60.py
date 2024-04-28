"""
write a program to compute height and length of every peak
(create three lists 1. to store index of the peak,
2. to store height of the peak and 3. to store length of the peak)
"""

path=r"C:\Users\HP\PycharmProjects\pythonProject.py\venv\Assignments\data\nseSample"
closeList=[]
for line in open(path):
    sym,dt,cls=line.strip().split(",")
    cls=float(cls)
    # print(cls)
    closeList.append(cls)

print(closeList)

n=len(closeList)

heightList=[]
indexList=[]
lenghtList=[]
count=1
for i in range(n-1):
      if closeList[i]>closeList[i+1] and closeList[i]>closeList[i-1]:
        indexList.append(i)
        heightList.append(closeList[i])
      else:
          count+=1
          lenghtList.append(count)


print("#########")
print("index list")
print(indexList)
print("HEIGHT list")
print(heightList)
print("lenght list")
print(lenghtList)
