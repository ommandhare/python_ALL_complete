"""
build small application to query yaml file

"""

import yaml

path=r"C:\Users\om\PycharmProjects\python_All\semi-structured data\yaml_dict.yaml"

with open(path) as f:
    data=yaml.safe_load(f)

print(data)

query=data['client1']['name']
print(query)