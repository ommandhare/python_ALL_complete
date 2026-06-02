import pandas as pd
import os

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns',None)

import WordCount as wc
import baseword as bs
import baseword_replacer as br
import Seniority as sn
import companyNormalization as cn


folderPath = r"C:\Users\Om Mandhare\PycharmProjects\python_ALL_complete\LinkedIn\Process_sql\data"

# Final Combined DF
masterDf = pd.DataFrame(columns=["First Name","Last Name","URL","Email Address","Company","Updated Company","Position","Base Role","Seniority","Connected On","Owner"])

# Loop all files
for file in os.listdir(folderPath):

    # Check only connection csv files
    if file.endswith("_connection.csv"):

        # Extract Name
        Name = file.replace("_connection.csv", "")

        path = os.path.join(folderPath, file)

        print("Processing :", Name)

        # # Read File
        df_path = pd.read_csv(
            path,
            encoding='utf-8-sig',
            on_bad_lines='skip'
        )
        #
        # print(df)

        # Clean column names
        df_path.columns = df_path.columns.str.strip()

        df_path.columns = df_path.columns.str.replace(" ", "_")

        # # Match schema
        # df_path = df_path[masterDf.columns]




        #
        # Path=r"C:\Users\Om Mandhare\PycharmProjects\python_ALL_complete\LinkedIn\Process_sql\data\Mandar_kale_connection.csv"
        # df_Path=pd.read_csv(path)
        #
        #
        df_role,df_co= wc.wordCount(path)
        print("Word Count Done...")
        #
        df_base_word = bs.baseword(df_role)
        print("Base word Done")
        #
        updated_df = br.replace_basewords(df_path,df_base_word)
        print("Base Word Replaced")

        updated_df=sn.get_levels(updated_df)
        print("Levels Extracted")

        updated_df=cn.normalize_company(updated_df)
        print("Company Normalized")

        updated_df["Owner"]=Name
        #
        if masterDf.empty:

            masterDf = updated_df.copy()

            # OTHER FILES
        else:

            # force same columns/order
            df = updated_df[masterDf.columns]

            masterDf = pd.concat(
                [masterDf, df],
                ignore_index=True
            )

print(masterDf)
masterDf.to_csv("Final_flat_table.csv")

