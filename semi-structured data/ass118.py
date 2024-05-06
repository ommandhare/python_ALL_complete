"""
read xml file and print all lines, search specific tags

"""

import xml.etree.ElementTree as ET


tree = ET.parse(r'C:\Users\om\PycharmProjects\python_All\data\countryTest.xml')
print("TYPE OF TREE: ", type(tree))
print(tree)


for node in tree.iter():
    tag=node.tag
    attrib=node.attrib
    value=node.text
    print("TAG: ",tag)
    print("Attrib: ", attrib)
    print("value: ",value)

find=input(print("search tag: "))

found_tags=tree.findall('.//'+find)

for tag in found_tags:
    print(tag.tag,tag.attrib,tag.text)