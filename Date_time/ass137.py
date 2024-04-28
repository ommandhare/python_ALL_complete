from datetime import datetime, timedelta
start_date = datetime(2024, 1, 1)
end_date = datetime(2024, 12, 31)

current_date = start_date
calendar_dimension = []

while current_date <= end_date:
    day = current_date.day
    month = current_date.month
    year = current_date.year
    weekday = current_date.strftime('%A')
    day_of_week = current_date.weekday()+1
    day_of_month = current_date.day
    day_of_year = current_date.timetuple().tm_yday


    calendar_dimension.append({
        'day': day,
        'month': month,
        'year': year,
        'weekday': weekday,
        'day_of_week': day_of_week,
        'day_of_month': day_of_month,
        'day_of_year': day_of_year,

    })

    current_date += timedelta(days=1)


for entry in calendar_dimension:
    print(entry)
