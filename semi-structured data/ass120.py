"""
read yaml file and print all lines, search specific tags

"""

import yaml

path=r"C:\Users\om\PycharmProjects\python_All\data\yaml_simple.yaml"

with open(path) as f:
    data=yaml.safe_load(f)

print(data)

search_tag=input(print("enter tag : "))

if search_tag in data:
    print(search_tag," found in yaml file")
    print(data[search_tag])