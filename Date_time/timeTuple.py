from datetime import timedelta,datetime,date

currentDate=date.today()


print("TYPE OF MY DATE: ",type(currentDate),"\n MY DATE: ", currentDate)
print("CURRENT DATE::", currentDate, "TYPE: ",type(currentDate))
m_day = currentDate.timetuple().tm_mday
print("DAY OF MONTH: ", m_day)
y_day = currentDate.timetuple().tm_yday
print("DAY OF THE YEAR: ", y_day)
w_day = currentDate.timetuple().tm_wday
print("DAY OF WEEK: ", w_day)
