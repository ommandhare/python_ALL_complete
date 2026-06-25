import pandas as pd
from sqlalchemy import create_engine

engine = create_engine(
    "mysql+pymysql://root:0777@localhost/connections"
)

print(type(engine))

df = pd.DataFrame({
    "id": [1, 2],
    "name": ["Om", "Mandhare"]
})

df.to_sql(
    "test_table",
    con=engine,
    if_exists="replace",
    index=False
)

print("Success")