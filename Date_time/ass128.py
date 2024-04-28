"""
Ask user to give day, month, year and create date in "YYYY-mm-dd" format

"""
import datetime as dt
#from dateutil.relativedelta import *
import datetime

from datetime import(
    datetime as DateTime,
    date as Date,
    time as Time,
    timedelta as TimeDelta
)
from time import strptime

from dateutil import relativedelta
import calendar

day=input(print("enter day "))
month=input(print("enter month "))
year=input(print("enter year "))


date_formatted = f"{year}-{month}-{day}"

print(date_formatted)