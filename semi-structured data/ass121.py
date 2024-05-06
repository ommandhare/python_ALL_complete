"""
build small application to query xml file

"""


import xml.etree.ElementTree as ET

path=r"C:\Users\om\PycharmProjects\python_All\data\countryTest.xml"

def query(findTag):
    found_tags=tree.findall('.//'+findTag)
    print(found_tags)



tree=ET.parse(path)
print(tree)


print("####################")

findTag=input(print("enter tag"))

query(findTag)