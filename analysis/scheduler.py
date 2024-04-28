import schedule
import time
import os
import subprocess


def run_data_generator():
    print("running")
    os.system(r"C:\Users\HP\PycharmProjects\pythonProject.py\venv\Assignments\analysis project\gen_daily.py")

# Schedule data generation every day at a specific time
# (schedule.every().day.at("12:14").do(run_data_generator))
schedule.every(1).minutes.do(run_data_generator())


while True:
    schedule.run_pending()
    time.sleep(60)  # Check every minute