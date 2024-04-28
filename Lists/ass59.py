"""
get two inputs on command line
1. symbol file
and
2. operations flag
(flag 1 to find peak, flag 2 to find trough and flag 3 to find both)
and find peaks or troughs as per given by operations flag.

"""
from sys import argv
path=argv[1]
flag=argv[2]
flag=int(flag)
def PEAKS(path,dataList):
    peakList=[]
    size=len(dataList)
    for i in range(1,size-1):
        if(dataList[i]>dataList[i+1]) and (dataList[i]>dataList[i-1]):
            peakList.append(dataList[i])
    print(peakList)

def TROUGHS(path,dataList):
    troughsList=[]
    size=len(dataList)
    for i in range(1,size-1):
        if(dataList[i]<dataList[i+1]) :
            troughsList.append(dataList[i])
    print(troughsList)



# path=r"C:\Users\HP\PycharmProjects\pythonProject.py\venv\Assignments\data\nseSample"
closeList=[]
for line in open(path):
    sym,dt,cls=line.strip().split(",")
    cls=float(cls)
    # print(cls)
    closeList.append(cls)




if flag==1:
 print("PEAKS :::")
 PEAKS(path,closeList)
elif flag==2:
 print("TROUGHS :::")
 TROUGHS(path,closeList)
elif flag==3:
    print("PEAKS AND TROUGHS ::::")
    PEAKS(path, closeList)
    TROUGHS(path, closeList)
else:
    print("INVALID CHOICE:::::")





