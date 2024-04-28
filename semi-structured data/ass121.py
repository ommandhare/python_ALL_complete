"""
build small application to query xml file

"""


import xml.etree.ElementTree as ET

path=r"C:\Users\HP\PycharmProjects\pythonProject.py\venv\Assignments\countryTest.xml"

def query(findTag):
    found_tags=tree.findall('.//'+findTag)
    print(found_tags)



tree=ET.parse(path)
print(tree)


print("####################")

findTag=input(print("enter tag"))

query(findTag)