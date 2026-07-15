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
SELECT 
DISTINCT
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
 Owner,
 original_company,
 country,
 industry, 
 Connected_On_Clean, 
current_employee_estimate,
 ranking
 FROM 
(
SELECT l.* , a.current_employee_estimate,
ROW_NUMBER() OVER (
    PARTITION BY Seniority,l.industry,Owner
    ORDER BY a.current_employee_estimate DESC
) AS ranking 
FROM connections.linkedin_comapanies_extented l
LEFT JOIN (select * from (select *, row_number() over(partition by company order by current_employee_estimate desc) as rnk from all_companies)a where rnk = 1) a
ON l.Updated_Company= a.company
)s

"""

# Read Query Result
df = pd.read_sql(QUERY, conn)

# Export to CSV
df.to_csv(
    r"C:\Users\Om Mandhare\Desktop\Connection_Analyis\Ranked_connects.csv",
    index=False,
    encoding="utf-8-sig"
)

conn.close()

print("CSV Exported Successfully!")