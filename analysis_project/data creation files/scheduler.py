import schedule
from datetime import time,timedelta,datetime
import time
import os
count=0
def daily_task():
    # Example: Create a daily log file
    os.system(r"C:\Users\HP\PycharmProjects\pythonProject.py\venv\Assignments\analysis_project\gen_daily.py")
    os.system(r"C:\Users\HP\PycharmProjects\pythonProject.py\venv\Assignments\analysis_project\append_to_sql.py")
    print("done")
# Schedule the daily task to run every day at a specific time
schedule.every(2).seconds.do(daily_task)
# schedule.every().day.at('15:21').do(daily_task)

while True:
    schedule.run_pending()
    time.sleep(1)