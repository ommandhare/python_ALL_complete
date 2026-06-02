
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
# GET ALL companies_ TABLES
# =========================

cursor.execute("""

SHOW TABLES LIKE 'companies_%'

""")

tables = cursor.fetchall()


# =========================
# DROP TABLES
# =========================

for table in tables:

    tableName = table[0]

    dropQuery = f"DROP TABLE {tableName}"

    cursor.execute(dropQuery)

    print(f"{tableName} dropped")


# =========================
# COMMIT + CLOSE
# =========================

conn.commit()

cursor.close()

conn.close()

print("All companies_ tables deleted")
