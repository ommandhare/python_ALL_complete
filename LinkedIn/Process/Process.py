import pandas as pd

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns',None)

import WordCount as wc
import baseword as bs
import baseword_replacer as br
import Seniority as sn
import companyNormalization as cn

Path=r"C:\Users\Om Mandhare\PycharmProjects\python_ALL_complete\LinkedIn\Process\connections.csv"
df_Path=pd.read_csv(Path)


df_role,df_co= wc.wordCount(Path)

# print(df_role)

df_base_word = bs.baseword(df_role)

# print(df_base_word)

updated_df = br.replace_basewords(df_Path,df_base_word)

# print(updated_df)

updated_df=sn.get_levels(updated_df)

updated_df=cn._normalize_company(updated_df)

print(updated_df)



