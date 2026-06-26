import pandas as pd
import mysql.connector
import sqlalchemy
# from sqlalchemy import create_engine

# pd.set_option('display.max_rows', None)
# pd.set_option('display.max_columns',None)

import WordCount as wc
import baseword as bs
import baseword_replacer as br
import Seniority as sn
import companyNormalization as cn

print(pd.__version__)
print(sqlalchemy.__version__)

# folderPath = r"C:\Users\Om Mandhare\PycharmProjects\python_ALL_complete\LinkedIn\Process\data"



# # Final Combined DF
masterDf = pd.DataFrame(columns=
                        ["First Name",
                        "Last Name",
                        "URL",
                        "Email Address",
                        "Company",
                        "Updated Company",
                        "Position",
                        "Base Role",
                        "Seniority",
                        "Connected On",
                        "Owner"])

QUERY_TOTAL_CONNECTIONS=''' SELECT * FROM connections.all_connections '''


QUERY_ALL_COMPANIES=''' SELECT * FROM connections.all_companies '''

JOIN_QUERY = ''' SELECT c.*,
                 a.company AS original_company,
                 a.country,a.industry FROM connect_project.all_companies a
                JOIN final_flat_table c
                ON a.company=c.Updated_Company
                and country <> ("nan") and country is not null;
                 '''



def dataframe_to_mysql(
        df,
        table_name,
        host="localhost",
        user="root",
        password="0777",
        database="connections",
        replace=True,
        batch_size=5000
):
    """
    Save a Pandas DataFrame to MySQL using mysql.connector.

    Parameters
    ----------
    df : pandas.DataFrame
    table_name : str
    host : str
    user : str
    password : str
    database : str
    replace : bool
        True  -> Drop existing table and recreate it.
        False -> Append to existing table.
    batch_size : int
        Number of rows inserted per batch.
    """

    # Copy dataframe
    df = df.copy()

    # Replace NaN
    df = df.fillna("")

    # Clean column names
    df.columns = (
        df.columns
        .str.strip()
        .str.replace(" ", "_")
        .str.replace("-", "_")
    )

    # Connect MySQL
    conn = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database
    )

    cursor = conn.cursor()

    # Drop Table
    if replace:
        cursor.execute(f"DROP TABLE IF EXISTS `{table_name}`")

    # Create Table
    column_definition = ", ".join(
        [f"`{col}` TEXT" for col in df.columns]
    )

    create_query = f"""
    CREATE TABLE IF NOT EXISTS `{table_name}`
    (
        {column_definition}
    )
    """

    cursor.execute(create_query)

    # Insert Query
    columns = ",".join([f"`{c}`" for c in df.columns])

    placeholders = ",".join(["%s"] * len(df.columns))

    insert_query = f"""
    INSERT INTO `{table_name}`
    ({columns})
    VALUES ({placeholders})
    """

    # Convert dataframe to tuples
    data = [tuple(row) for row in df.astype(str).values]

    # Batch Insert
    total_rows = len(data)

    for i in range(0, total_rows, batch_size):

        batch = data[i:i + batch_size]

        cursor.executemany(insert_query, batch)

        conn.commit()

        print(
            f"Inserted {min(i + batch_size, total_rows)} / {total_rows} rows"
        )

    print(f"\nSuccessfully inserted {total_rows} rows into '{table_name}'")

    cursor.close()
    conn.close()


def get_db_connection():
    """Create and return database connection"""
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='0777',
        database='connections'
    )

conn = get_db_connection()
cursor = conn.cursor()

# ======================== FUNCTION TO FETCH DATA FROM DATABASE ========================
def fetch_query(query, params=None):
    """Execute query and return dataframe"""
    if params:
        cursor.execute(query, params)
    else:
        cursor.execute(query)
    results = cursor.fetchall()
    columns = [desc[0] for desc in cursor.description] if cursor.description else []
    cursor.close()
    conn.close()
    return pd.DataFrame(results, columns=columns)



master_input_df = fetch_query(QUERY_TOTAL_CONNECTIONS)

# print(master_input_df)


# Loop all files
for owner in master_input_df["Owner"].unique():

    print(f"Processing : {owner}")

    # Filter one person's data
    df_path = master_input_df[
        master_input_df["Owner"] == owner
    ].copy()

    # print(df_path)

    # Clean column names
    df_path.columns = df_path.columns.str.strip()

    df_path.columns = df_path.columns.str.replace(" ", "_")

    #  Match schema
    # df_path = df_path[masterDf.columns]


    df_role,df_co= wc.wordCount(df_path)
    print("Word Count Done...")

    df_base_word = bs.baseword(df_role)
    print("Base word Done")

    updated_df = br.replace_basewords(df_path,df_base_word)
    print("Base Word Replaced")

    updated_df=sn.get_levels(updated_df)
    print("Levels Extracted")

    updated_df=cn.normalize_company(updated_df)
    print("Company Normalized")

    updated_df["Owner"]=owner
    #
    if masterDf.empty:

        masterDf = updated_df.copy()

    else:

        # force same columns/order
        df = updated_df[masterDf.columns]

        masterDf = pd.concat(
            [masterDf, df],
            ignore_index=True
        )

# print(masterDf)
masterDf.to_csv("Final_flat_table_NEW.csv")


conn = get_db_connection()

cursor = conn.cursor(dictionary=True)

cursor.execute(JOIN_QUERY)

rows = cursor.fetchall()

df_final = pd.DataFrame(rows)

df_final["Connected_On_Clean"] = pd.to_datetime(
    df_final["Connected_On"],
    errors="coerce"
).dt.strftime("%Y-%m-%d")



dataframe_to_mysql(df_final,table_name="linkedin_comapanies_extented")
print("Process is Done")
#End of th code