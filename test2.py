import pandas as pd
import mysql.connector

# =========================
# READ CSV
# =========================

path = r"C:\Users\Om Mandhare\PycharmProjects\python_ALL_complete\LinkedIn\Process\Final_flat_table.csv"

df = pd.read_csv(path, encoding='utf-8-sig')


# =========================
# MYSQL CONNECTION
# =========================

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="0777",
    database="connect_project"
)

cursor = conn.cursor()


# =========================
# CREATE TABLE IF NOT EXISTS
# =========================

createTableQuery = """
CREATE TABLE IF NOT EXISTS linkedin_connections (

    First_Name VARCHAR(255),
    Last_Name VARCHAR(255),
    URL TEXT,
    Email_Address VARCHAR(255),
    Company VARCHAR(255),
    Updated_Company VARCHAR(255),
    Position TEXT,
    Base_Role VARCHAR(255),
    Seniority VARCHAR(255),
    Connected_On VARCHAR(255),
    Owner VARCHAR(255)

)
"""

cursor.execute(createTableQuery)


# =========================
# INSERT DATA
# =========================

insertQuery = """
INSERT INTO linkedin_connections (

    First_Name,
    Last_Name,
    URL,
    Email_Address,
    Company,
    Updated_Company,
    Position,
    Base_Role,
    Seniority,
    Connected_On,
    Owner

)

VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
"""


for _, row in df.iterrows():

    values = (

        row['First_Name'],
        row['Last_Name'],
        row['URL'],
        row['Email_Address'],
        row['Company'],
        row['Updated_Company'],
        row['Position'],
        row['Base_Role'],
        row['Seniority'],
        row['Connected_On'],
        row['Owner']

    )

    cursor.execute(insertQuery, values)


# =========================
# SAVE CHANGES
# =========================

conn.commit()

print("CSV Imported Successfully")


# =========================
# CLOSE CONNECTION
# =========================

cursor.close()

conn.close()
