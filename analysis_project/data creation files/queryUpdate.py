import pandas as pd
from sqlalchemy import create_engine

DATABASE_URI = 'mysql+pymysql://root:0777@localhost:3306/retail_project'
engine = create_engine(DATABASE_URI)

seasonality = r"C:\Users\Om Mandhare\PycharmProjects\python_ALL_complete\analysis_project\OBJECTIVE QUERIES\NEW ANALYSIS\seasonalityIndex.sql"

affinity = r"C:\Users\Om Mandhare\PycharmProjects\python_ALL_complete\analysis_project\OBJECTIVE QUERIES\NEW ANALYSIS\affinityScore.sql"

reward = r"C:\Users\Om Mandhare\PycharmProjects\python_ALL_complete\analysis_project\OBJECTIVE QUERIES\NEW ANALYSIS\reward_member.sql"


def update(sql_query, table_name):
    with open(sql_query, "r") as file:
        sql_query = file.read()

    df = pd.read_sql_query(sql_query, engine)

    # print(df)
    df.to_sql(table_name, engine, if_exists='replace', index=False)
    print("Done to sql...")


update(seasonality, "seasonality")
print("Seasonality updated")

update(affinity, "affinity")
print("Affinity updated")

update(reward, "reward")
print("reward updated")
