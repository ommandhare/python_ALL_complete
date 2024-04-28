"""
read nse_daily_stock file (create class that stores symbol, date, closing price as attributes).
Store objects in a list, implement algorithm to find peaks in the list (peak price) and print
objects that are on the peak

"""
import csv
class NseDaily:
    def _init_(self,dt,op,hi,lo,cls,shrTred,turnOvr):
        self.dt=dt
        self.op=op
        self.hi=hi
        self.lo=lo
        self.cls=cls
        self.shrTred=shrTred
        self.turnOvr=turnOvr

def dataExtrector(path):
    ObjList=[]
    for line in open(path):
        dt,op,hi,lo,cls,shrTred,turnOvr=line.strip().split(",")
        nifty=NseDaily(dt,op,hi,lo,cls,shrTred,turnOvr)
        ObjList.append(nifty)
        print(nifty[0])

    # with open(path) as fs:
    #     data = csv.reader(fs)
    #     next(data,None)
    #     for line in data:
    #         nifty=NseDaily(line[0],line[1],line[2],line[3],line[4],line[5],line[6])
    #         ObjList.append(nifty)
    #         print(nifty)
    return ObjList

def peaks(objList):
    peak=[]
    asend=False
    for idx in range(len(objList)-1):
        if(objList[idx].cls <objList[idx+1].cls):
            if(not asend):
                asend=True
        else:
            if(asend):
                peak.append(objList[idx])
                asend=False
    return peak




path=r'C:\Users\HP\PycharmProjects\pythonProject.py\venv\Assignments\OOP\NIFTY 50-17-01-2024-to-17-04-2024.csv'
objList=dataExtrector(path)
# peakObjs=peaks(objList)
# for obj in peakObjs:
#     print(f"Date: {obj.dt} peak price : {obj.cls}")

