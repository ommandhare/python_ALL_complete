"""
Get two dates from config file and generate a
report that shows 1st Monday of every month between these days
"""


"""
start date : something convert to first date of month 
find first monday
"""
from datetime import date ,timedelta
from config import startDate,endDate

begining = date(startDate.year,startDate.month,1)
mondayList=[]
while begining < endDate:
    if begining.weekday() == 0:
        mondayList.append(begining)
        begining=date(begining.year,begining.month+1,1)
    else:
        begining+=timedelta(days=1)

for dt in mondayList:
    if(dt >= startDate):
        print(dt)