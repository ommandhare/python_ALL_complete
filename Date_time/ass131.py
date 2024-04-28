"""
Get Date and find last month first date, last quarter 1st date, last year 1st date

"""


from datetime import datetime, timedelta


current_date = datetime(2024,2,6)
last_month_first_date = current_date-timedelta(days=30)
last_month_first_date = last_month_first_date.replace(day=1)

print(last_month_first_date)

quarter_month = (current_date.month - 1) // 3
last_quarter_first_date = current_date.replace(month=quarter_month*3 + 1, day=1) - timedelta(days=1)
last_quarter_first_date = last_quarter_first_date.replace(day=1)
# print(last_quarter_first_date)

last_year_first_date = current_date.replace(year=current_date.year - 1, month=1, day=1)

print("Last Month's First Date:", last_month_first_date.strftime('%Y-%m-%d'))
print("Last Quarter's First Date:", last_quarter_first_date.strftime('%Y-%m-%d'))
print("Last Year's First Date:", last_year_first_date.strftime('%Y-%m-%d'))
