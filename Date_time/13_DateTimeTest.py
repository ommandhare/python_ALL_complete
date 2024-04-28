#1. get date time from system -- type -- date time
#2. how to extract elements of date time from date time object
#3. how to build date time object from individual elemenst (DateTime())
#4. how to build date string (yyyy-mm-dd) -- 2022,9,25 --> 2022-09-25 -- using individual elements
#5. how to build date time object from date time string
#6. how to use time delta library to find a new date given input date and timedelta (+- numDays, or +- numMonths, +-numYears)


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
from time import strptime

from dateutil import relativedelta
import calendar

### how to build date time object using now() method (current date time)
### how to compute date time components from date time object
### how to build date time object from date string
### how to build string from date time object
### how to build date time object from individual date-time components
### how to do time delta functions and relative delta functions


### how to convert this string into date time objects
###myStr = "2020-01-02"
print(DateTime.now())
currentDateTime = DateTime.now()


#print(type(currentDateTime))
print("CURRENT DATE TIME:::: ",currentDateTime)
print("type of current date time: ",type(currentDateTime))
currentYear = currentDateTime.year
currentMonth = currentDateTime.month
currentDay = currentDateTime.day
print("YEAR: ",currentYear)
print("MONTH: ",currentMonth)
print("DAY: ",currentDay)
print("HOUR: ",currentDateTime.hour)
print("MINUTE: ",currentDateTime.minute)
print("SECOND: ",currentDateTime.second)
print("WEEK DAY: ",currentDateTime.weekday())
print("WEEK DAY NAME: ", weekDay[currentDateTime.weekday()])

##### BELOW LINES OF CODE COMPUTE DATE TIME COMPONENS FROM DATE TIME OBJECT
currentYear = DateTime.now().year
#print(temp_employee.emp_id)
print("type of current year: ", type(currentYear), "CURRENT YEAR: ", currentYear)
currentMonth = DateTime.now().month
print("TYPE OF CURRENT MONTH: ", type(currentMonth))
currentDay = DateTime.now().day
current_day = currentDateTime.day
print("TYPE OF CURRENT DAY: ", type(currentDay))
currentHour = currentDateTime.hour
currentMinutes = currentDateTime.minute
currentSeconds = currentDateTime.second
### DateTime.Now() returns Current Date Time in DataTimeObject
### we extracted Day, Month, Year, Hour, Minute, Senconds from Date Time Objects
currentDate = DateTime.now().date()
print("###########################################")
print("DATE: ", currentDate,"\nMONTH: ",currentMonth)
print("DAY: ",currentDay,"\nDATE: ",currentDate)
print("HOUR: ", currentHour,"\nMinutes: ", currentMinutes,"\nSeconds: ",currentSeconds)
print("###################################################")


#### How to Build DateTime Object if i have individual Date Elements.
### for example i have year, month and Day value and want to build date time object
### get and set (constructor)
dateFromElements = DateTime(currentYear+5,currentMonth+5,currentDay,currentHour,currentMinutes,currentSeconds)
print("dateFromElements: ",dateFromElements, "   TYPE::: ",type(dateFromElements))

#currentDay1 = 5
#-5
### last year date as Date Time Object
### Generate last year date programatically based on current date and our requirements.
lastYearDate = DateTime(currentYear-1,currentMonth,currentDay,19,12,45)

print(lastYearDate)
lastYearDateStr = str(currentYear -1) + "-" + str(currentMonth) + "-" + str(currentDay)
print("&*&*&***&*&::: ",lastYearDateStr)

### last year date as string
if(currentDay < 10):
    currentDayStr = "0" + str(currentDay)
else:
    currentDayStr = str(currentDay)
if(currentMonth < 10):
    currentMonthStr = "0" + str(currentMonth)
else:
    currentMonthStr = str(currentMonth)
lastYearDateStr = str(currentYear -1) + "-" + currentMonthStr + "-" + currentDayStr
print("last year date string: ", lastYearDateStr)
print(type(lastYearDateStr))
## you can convert date in string format to date in datetime format.
lastYrDateDT = DateTime.strptime(lastYearDateStr,"%Y-%m-%d").date()
print("#########################################################: ",lastYrDateDT, type(lastYrDateDT))
print("LAST YEAR DATE DATETIME OBJECT: ", lastYearDate)

twoYrBefore = DateTime(currentYear-2,currentMonth,currentDay)
print(type(twoYrBefore))



#kwargs
#TimeDelta()
print("TYPE LAST YEAR DATE::: ",type(lastYearDate))
print("LAST YEAR DATE: ",lastYrDateDT)
newDate = lastYearDate.date() - TimeDelta(days=32)
threeYearBackDate = lastYearDate.date() - TimeDelta(days=1100)
print("TYPE OF NEW DATE", type(newDate))
print("NEW DATE - last year - 32 days: ", newDate)
print("LAST YEAR DATE: ", lastYearDate.date(), "threeyearBackDate: ", threeYearBackDate)
print('RESULT')
print("\nLAST YEAR DATE: ",lastYearDate,type(lastYearDate))
print("TWO YEARS BEFORE: ", twoYrBefore)
print(DateTime(newDate.year,newDate.month,newDate.day))

#newDateOneYearOneMonthBack = lastYearDate.date() + relativedelta(months=+2)
#print("MONTH SUBSTRACTION USING TIME DELTA *******: ",newDateOneYearOneMonthBack)


print("LAST YEAR DATE:",lastYearDate,"\nTWO YR BACK DATE: ", twoYrBefore)
diff = lastYearDate - twoYrBefore
print("TYPE OF DATE DIFFERENCE: ", type(diff))
print(diff.days)
print("DAYS: ",diff.days)



######### relative delta calculates
r = relativedelta.relativedelta(currentDate, twoYrBefore)
print("TYPE OF relative delta return::: ", type(r))
y = r.years
print(y)
print("##############################################################################")


weekDay = {0:"Monday",1:"Tuesday",2:"Wednesday",3:"Thursday",4:"Friday",5:"Saturday",6:"Sunday"}
#print(diff)
myDate = DateTime(2021,6,28).date()
print("TYPE OF MY DATE: ",type(myDate),"\n MY DATE: ", myDate)
print("CURRENT DATE::", currentDate, "TYPE: ",type(currentDate))
m_day = currentDate.timetuple().tm_mday
print("DAY OF MONTH: ", m_day)
y_day = currentDate.timetuple().tm_yday
print("DAY OF THE YEAR: ", y_day)
w_day = currentDate.timetuple().tm_wday
print("DAY OF WEEK: ", w_day)
week_day = weekDay[currentDate.weekday()]
print("DAY OF WEEK (DAY NAME) :: ", week_day)


# Convert the integer to english representation
WeekDayFromDate = myDate.strftime("%A")

print("MY DATE: ",myDate)
print("##################################### DAY OF YEAR: ", y_day)
print("##################################### DAY OF THE WEEK: ", w_day)
print("##################################### Week Day: ", week_day)
print("##################################### Week Day from Date: ", WeekDayFromDate)


newDateFeb = currentDate - TimeDelta(days=55)
print(currentDate)
print(newDateFeb)
print("#######################################################################")
#### convert string to date object

date_str = "01-01-2019"
date_str1 = "JAN 01 2019"
date_str2 = "1 JAN 2019"

date_obj = DateTime.strptime(date_str,'%m-%d-%Y').date()
print(type(date_obj))
month = date_obj.month
next_month = month+1
if(month == 12):
    next_month = 1
else:
    next_month = month + 1

if(next_month < 10):
    next_month = "0" + str(next_month)
else:
    next_month = str(next_month)

print(next_month)
next_mon_date =  next_month +"-01" + "-2019"
print("next mon date",next_mon_date)
nxt_mn_date = DateTime.strptime(next_mon_date,"%m-%d-%Y")
#### strptime - convert string to date time object
#### strftime - convert from date time object to string

month_last_date = nxt_mn_date - TimeDelta(days=1)
print("mon_last_date: ", month_last_date)
print(date_obj.year, " " ,date_obj.month, " " ,date_obj.day)

day_of_week = nxt_mn_date.weekday()
print("day of the week: ", day_of_week)
### tuple is immutable == can not modify once assigned -- functional programming
### list is set of elements.. in traditional sense list is supposed to be elements of same data type
### in python list can have elements with different data types (heterogeneous data types)
### Traditionally Tuple is list of elemenst of different types -- one row of a table is tuple -- attributes of a class
myList = (1,1,3,4,5,"Rushi")

####weekFirstDay = calendar
day_name = calendar.day_name[day_of_week]
print("DAY NAME: ", day_name)
day_name1 = calendar.day_name[0]
print("FIRST DAY OF WEEK: ",day_name1)


