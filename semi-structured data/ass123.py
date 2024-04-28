"""
build small application to query yaml file

"""

import yaml

path=r"C:\Users\HP\PycharmProjects\pythonProject.py\venv\Assignments\semi-structured data\yaml_dict.yaml"

with open(path) as f:
    data=yaml.safe_load(f)

print(data)

query=data['client1']['type']
print(query)