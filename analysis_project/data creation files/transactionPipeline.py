from datetime import date
import subprocess


current_date = date.today()
print(current_date)




tran_daily = r"C:\Users\Om Mandhare\PycharmProjects\python_ALL_complete\analysis_project\data creation files\transactions_Daily.py"

k = input(
    f"If you want to run {current_date} for stock data and append it to the SQL database, then press 'q' key: ")


if k == "q":
    try:

        subprocess.run(["python", tran_daily], check=True)
        print("nse Daily data generated...")
        print("appended to the SQL...")


    except subprocess.CalledProcessError as e:
        print(f"An error occurred while running the scripts: {e}")


print("DONE ALL.............")