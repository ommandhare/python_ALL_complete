"""
Get two dates from config file and generate a report that shows
last Saturday of every month between these days

"""

from datetime import(
    datetime as DateTime,
    date as Date,
    time as Time,
    timedelta as TimeDelta
)
import csv
import calendar

beginDate=Date(2024,3,1)

numdays=TimeDelta(days=90)

endDate=beginDate+numdays

print("beginDate : ",beginDate)
print("EndDate : ",endDate)


currentDate=beginDate
cnt=0
last_saturday=[]



while currentDate <= endDate:
    weekday=currentDate.weekday()

    if weekday==5 and currentDate.day >= 24 :
           print(currentDate,currentDate.strftime("%A"))
           last_saturday.append((currentDate, currentDate.strftime('%A')))
           cnt+=1
    currentDate += TimeDelta(days=1)


currentDate=Date(currentDate.year,currentDate.month,1)-TimeDelta(days=31)






print(cnt)
print(last_saturday)



# path=r"C:\Users\HP\PycharmProjects\pythonProject.py\venv\Assignments\Date_time\count_saturday.csv"
#
# def write_to_csv(last_saturday):
#     with open(path, 'w', newline='') as csvfile:
#         writer = csv.writer(csvfile)
#         writer.writerow(['first_mondays'])
#         for date, weekday in last_saturday:
#             writer.writerow([date.strftime('%Y-%m-%d'), weekday])
#
# write_to_csv(last_saturday)
