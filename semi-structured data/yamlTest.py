import yaml

with open(r"C:\Users\om\PycharmProjects\python_All\semi-structured data\yaml_dict.yaml") as f:
    data=yaml.safe_load(f)

print(data)


search=input("Enter the Tag:::")

for tag in data:
    if search == tag:
     print(data[tag])
