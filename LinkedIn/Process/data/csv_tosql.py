import pandas as pd
import mysql.connector

# Read CSV
df = pd.read_csv(
    r"C:\Users\Om Mandhare\PycharmProjects\python_ALL_complete\LinkedIn\Process\data\Jigar_Vasani_connection.csv",
    dtype=str,
    low_memory=False
)

df = df.fillna("")

# Connect MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="0777",
    database="connections"
)

cursor = conn.cursor()

# Table Name
table_name = "Jigar_Vasani_connections"

# Drop Table if Exists
cursor.execute(f"DROP TABLE IF EXISTS {table_name}")

# Create Table Dynamically
columns = []

for col in df.columns:
    clean_col = col.replace(" ", "_").replace("-", "_")
    columns.append(f"`{clean_col}` TEXT")

create_query = f"""
CREATE TABLE {table_name}
(
    {",".join(columns)}
)
"""

cursor.execute(create_query)

# Insert Query
col_names = [f"`{c.replace(' ','_').replace('-','_')}`" for c in df.columns]

insert_query = f"""
INSERT INTO {table_name}
({",".join(col_names)})
VALUES ({",".join(['%s']*len(col_names))})
"""

# Convert dataframe to tuples
data = [tuple(row) for row in df.values]

# Bulk Insert
cursor.executemany(insert_query, data)

conn.commit()

print(f"Rows Inserted: {cursor.rowcount}")

# Verify Count
cursor.execute(f"SELECT COUNT(*) FROM {table_name}")
print("Total Rows in Table:", cursor.fetchone()[0])

cursor.close()
conn.close()