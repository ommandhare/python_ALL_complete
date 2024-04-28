"""
Get endDate from config file, get numdays from config file, calculate begindate as endDate -
numDays, Find number of saturdays between these two dates,
exclude 3rd Satudays that are 3rd Saturday of that month. Write date and associated count in a csv file.
 ** NAME this program as "countSaturday.py"


"""
from datetime import(
    datetime as DateTime,
    date as Date,
    time as Time,
    timedelta as TimeDelta
)
import csv

endDate=Date(2024,2,1)

numdays=TimeDelta(days=31)

beginDate=endDate-numdays

print("beginDate : ",beginDate)
print("EndDate : ",endDate)



currentDate=beginDate
# while currentDate <= endDate:
#     if currentDate.weekday()==5:
#        print(currentDate)
#     currentDate += TimeDelta(days=1)



Saturdays=[]
saturday_count=0
while currentDate <= endDate:
     weekday=currentDate.weekday()
     while currentDate <= endDate:
         if currentDate.weekday() == 5:
             if saturday_count ==2 :
                 saturday_count += 1
             else:
                 Saturdays.append((currentDate, currentDate.strftime('%A')))
                 saturday_count += 1
         currentDate += TimeDelta(days=1)

print("Total Saturdays : ",saturday_count)
print(Saturdays)




path=r"C:\Users\HP\PycharmProjects\pythonProject.py\venv\Assignments\Date_time\count_saturday.csv"

def write_to_csv(Saturdays):
    with open(path, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Saturdays'])
        for date, weekday in Saturdays:
            writer.writerow([date.strftime('%Y-%m-%d'), weekday])

write_to_csv(Saturdays)
