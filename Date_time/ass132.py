"""
Get endDate from config file, get numdays from config file, calculate begindate as endDate
numDays  and
generate a report that shows all weekend dates between these days
(write dates and associated weekday in a csv file)

"""
from datetime import(
    datetime as DateTime,
    date as Date,
    time as Time,
    timedelta as TimeDelta
)
import csv

endDate=Date(2024,3,5)

numdays=TimeDelta(days=30)

beginDate=endDate-numdays

print("beginDate : ",beginDate)
print("EndDate : ",endDate)


currentDate=beginDate

weekends=[]

while currentDate <= endDate:
     weekday=currentDate.weekday()
     if(weekday)==5:
        weekends.append((currentDate, currentDate.strftime('%A')))
        # weekends.append(currentDate)
     elif(weekday)==6:
         weekends.append((currentDate, currentDate.strftime('%A')))
         # weekends.append(currentDate,weekday)
     currentDate += TimeDelta(days=1)

     print(weekday)

print(weekends)
path=r"C:\Users\HP\PycharmProjects\pythonProject.py\venv\Assignments\Date_time\weekends.csv"

def write_to_csv(weekends):
    with open(path, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Date', 'Weekday'])
        for date, weekday in weekends:
            writer.writerow([date.strftime('%Y-%m-%d'), weekday])

write_to_csv(weekends)

