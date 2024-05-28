path=r"C:\Users\om\PycharmProjects\python_All\RADAR\clean_data_with_category.csv"

for line in open(path):
    desc,c1,c2,c3,c4,c5,c6,c7=line.strip().split(",")
    print(desc)