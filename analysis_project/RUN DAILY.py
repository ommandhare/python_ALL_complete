import os
from datetime import date

currendate=date.today()
print(currendate)



generate=r"C:\Users\HP\PycharmProjects\pythonProject.py\venv\Assignments\analysis_project\generate_all_at_schedule.py"
query=r"C:\Users\HP\PycharmProjects\pythonProject.py\venv\Assignments\analysis_project\query_schedule.py"
storetoriginal=r"C:\Users\HP\PycharmProjects\pythonProject.py\venv\Assignments\analysis_project\append_daily_to_original.py"

k=input(f"if you want run {currendate}  data press q key : ")
if k=="q":
    os.system(f"python {generate}")
    os.system(f"python {query}")
    os.system(f"python {storetoriginal}")



