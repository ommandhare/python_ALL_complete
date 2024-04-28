from datetime import(
    datetime as DateTime,
    date as Date,
    time as Time,
    timedelta as TimeDelta
)
import csv

beginDate=Date(2024,3,1)

numdays=TimeDelta(days=30)

endDate=beginDate+numdays

print("beginDate : ",beginDate)
print("EndDate : ",endDate)


all= Date.day
print(all)