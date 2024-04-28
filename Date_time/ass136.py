"""
Read a file containing one date per line and find day (Monday, Tuesday etc) for every date.

"""

from datetime import(
    datetime ,
    date as Date,
    time as Time,
    timedelta as TimeDelta
)
path=r"C:\Users\HP\PycharmProjects\pythonProject.py\venv\Assignments\Date_time\dates"

def find_day_of_week(file_path):
 with open(path,"r") as file:
    for line in file:
        date_str=line.strip()
        date_obj = datetime.strptime(date_str, '%Y-%m-%d')
        day_of_week = date_obj.strftime('%A')
        print(f"{date_str}: {day_of_week}")


find_day_of_week('dates.txt')