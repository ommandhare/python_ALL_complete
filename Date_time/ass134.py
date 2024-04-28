"""
Get two dates from config file and generate a report that shows 1st Monday of every months between these days

"""
from datetime import(
    datetime as DateTime,
    date as Date,
    time as Time,
    timedelta as TimeDelta
)
from dateutil.relativedelta import relativedelta
import csv

beginDate=Date(2024,1,1)

numdays=TimeDelta(days=150)

endDate=beginDate+numdays

print("beginDate : ",beginDate)
print("EndDate : ",endDate)


# beginDate=Date(beginDate.year,beginDate.month,day=1)
# print(beginDate)

currentDate=beginDate
cnt=0
mondays=[]
while currentDate <= endDate:
    if currentDate.weekday()==0:
       print(currentDate,currentDate.strftime("%A"))
       mondays.append((currentDate, currentDate.strftime('%A')))
       currentDate=Date(currentDate.year,currentDate.month+1,1)
    else:
        currentDate+=TimeDelta(days=1)




# print(cnt)
print(mondays)



path=r"C:\Users\HP\PycharmProjects\pythonProject.py\venv\Assignments\Date_time\first_mondays.csv"

def write_to_csv(mondays):
    with open(path, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['first_mondays'])
        for date, weekday in mondays:
            writer.writerow([date.strftime('%Y-%m-%d'), weekday])

write_to_csv(mondays)
