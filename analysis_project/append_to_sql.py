import pandas as pd
import mysql.connector
import csv

def append():
    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password='0777',
        database='retail'
    )

    cursor = conn.cursor()



    path1 = r"C:\Users\HP\PycharmProjects\pythonProject.py\venv\Assignments\analysis_project\daily_files\tran_dtl_daily.csv"
    path2 = r"C:\Users\HP\PycharmProjects\pythonProject.py\venv\Assignments\analysis_project\daily_files\tran_hdr_daily.csv"

    with open(path1, 'r') as file:
        data = csv.reader(file)
        next(data)
        for line in data:
            query = f"INSERT INTO {'tran_dtl'} VALUES {tuple(line)}"

            cursor.execute(query)

    with open(path2, 'r') as file:
        data = csv.reader(file)
        next(data)
        for line in data:
            query = f"INSERT INTO {'tran_hdr'} VALUES {tuple(line)}"

            cursor.execute(query)

    conn.commit()
    cursor.close()
    conn.close()

append()