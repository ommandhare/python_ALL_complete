import pandas as pd

df=pd.read_csv(r"C:\Users\Om Mandhare\PycharmProjects\python_ALL_complete\pandas\pandas_practices\product.csv")

#sum
sum=df.qty.sum()
print(sum)

#mean
mean=df.qty.mean()
print(mean)

#std
std=df.qty.std()
print(std)


#median
median=df.qty.median()
print(median)
