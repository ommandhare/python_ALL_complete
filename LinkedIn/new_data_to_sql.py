import pandas as pd
import mysql.connector

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
# CREATE TABLE
# =========================

createQuery = """

CREATE TABLE IF NOT EXISTS all_companies (

    srno BIGINT,
    company VARCHAR(255),
    domain VARCHAR(255),
    year_founded VARCHAR(255),
    industry VARCHAR(255),
    size_range VARCHAR(255),
    locality VARCHAR(255),
    country VARCHAR(255),
    linkedin_url TEXT,
    current_employee_estimate BIGINT,
    total_employee_estimate BIGINT

)

"""

cursor.execute(createQuery)


# =========================
# INSERT QUERY
# =========================

insertQuery = """

INSERT INTO all_companies (

    srno,
    company,
    domain,
    year_founded,
    industry,
    size_range,
    locality,
    country,
    linkedin_url,
    current_employee_estimate,
    total_employee_estimate

)

VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)

"""


# =========================
# READ CSV IN CHUNKS
# =========================

chunksize = 100000

for chunk in pd.read_csv(
        r"C:\Users\Om Mandhare\Desktop\companies_sorted.csv",
        chunksize=chunksize,
        encoding='utf-8',
        low_memory=False):


    # =========================
    # CLEAN COLUMN NAMES
    # =========================

    chunk.columns = chunk.columns.str.strip()

    chunk.columns = chunk.columns.str.lower()

    chunk.columns = chunk.columns.str.replace(" ", "_")

    print(chunk.columns)


    # =========================
    # BULK VALUES
    # =========================

    valuesList = []

    for _, row in chunk.iterrows():

        values = (

            row.get('srno', None),
            str(row.get('name', '')),
            str(row.get('domain', '')),
            str(row.get('year_founded', '')),
            str(row.get('industry', '')),
            str(row.get('size_range', '')),
            str(row.get('locality', '')),
            str(row.get('country', '')),
            str(row.get('linkedin_url', '')),
            row.get('current_employee_estimate', None),
            row.get('total_employee_estimate', None)

        )

        valuesList.append(values)


    # =========================
    # FAST BULK INSERT
    # =========================

    cursor.executemany(insertQuery, valuesList)

    conn.commit()

    print("Chunk Inserted")


# =========================
# CLOSE CONNECTION
# =========================

cursor.close()

conn.close()

print("All Data Imported")