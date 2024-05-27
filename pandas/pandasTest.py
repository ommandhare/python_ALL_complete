import pandas as pd

a=[1,2,3,4]
b=[3,6,2,4]

a_df=pd.DataFrame(a)
# print(a_df)

b_df=pd.DataFrame(b)
# print(b_df)

concat_df=pd.concat([a_df,b_df],ignore_index=True)

merge_df=pd.merge(a_df,b_df)


# print(concat_df)

print(merge_df)