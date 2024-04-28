"""
Get current date time from system and display units of datetime (year, month, day, hour, minute, second)

"""

import datetime as dt
#from dateutil.relativedelta import *
import datetime
weekDay = {0:"MONDAY",1:"TUESDAY",2:"WEDNESDAY",3:"THURSDAY",4:"FRIDAY",5:"SATURDAY",6:"SUNDAY"}
from datetime import(
    datetime as DateTime,
    date as Date,
    time as Time,
    timedelta as TimeDelta
)

import calendar
print(DateTime.now())
currentDateTime = DateTime.now()

print("CURRENT DATE TIME:::: ",currentDateTime)
currentYear = currentDateTime.year
currentMonth = currentDateTime.month
currentDay = currentDateTime.day
print("YEAR: ",currentYear)
print("MONTH: ",currentMonth)
print("DAY: ",currentDay)
print("HOUR: ",currentDateTime.hour)
print("MINUTE: ",currentDateTime.minute)
print("SECOND: ",currentDateTime.second)
