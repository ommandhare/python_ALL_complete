from datetime import(
    datetime as DateTime,
    date as Date,
    time as Time,
    timedelta as TimeDelta
)
from dateutil.relativedelta import relativedelta


beginDate=Date(2024,3,1)

numdays=TimeDelta(days=90)

endDate=beginDate+numdays

print("beginDate : ",beginDate)
print("EndDate : ",endDate)


for i in range(5):
 beginDate=beginDate+relativedelta(months=1)
 print(beginDate)