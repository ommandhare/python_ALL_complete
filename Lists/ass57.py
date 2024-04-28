"""
read symbol_day_close file,
store all close prices (only for one symbol) in a list and find peaks in the list

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

peakList=[]

for i in range(1,n-1):
      if closeList[i]>closeList[i+1] and closeList[i]>closeList[i-1]:
        peakList.append(closeList[i])

print("#########")
print("PEAKS IN LISTs")
print(peakList)