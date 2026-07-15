import pandas as pd
import mysql.connector

# MySQL Connection
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="0777",
    database="connections"
)

QUERY = """
SELECT * FROM 
(
SELECT l.* , a.current_employee_estimate, 
ROW_NUMBER() OVER (
    PARTITION BY Seniority,l.industry,Owner
    ORDER BY a.current_employee_estimate DESC
) AS ranking 
FROM connections.linkedin_comapanies_extented l
JOIN all_companies a
ON l.Updated_Company= a.company
)s
WHERE ranking > 10
;
"""

# Read Query Result
df = pd.read_sql(QUERY, conn)

# Export to CSV
df.to_csv(
    r"C:\Users\Om Mandhare\Desktop\Connection_Analysis\greater than ranking.csv",
    index=False,
    encoding="utf-8-sig"
)

conn.close()

print("CSV Exported Successfully!")