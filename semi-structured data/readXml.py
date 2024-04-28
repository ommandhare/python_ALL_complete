


import xml.etree.ElementTree as ET


tree = ET.parse(r'C:\Users\HP\PycharmProjects\pythonProject.py\venv\Assignments/CountryTest.xml')
print("TYPE OF TREE: ", type(tree))

for elem in tree.iter():
    tag = elem.tag
    attrib = elem.attrib
    print(" TAG : ", tag)
    print(" TAG ATTRIB: ", attrib, "attrib type:: ", type(attrib), "LENTGH OF THE ATTRIB DICT: ", len(attrib))
    print(" PRINTING TEXT: ", elem.text)
    ##print(type(attrib))
    cnt = 0
    for at, v in attrib.items():
        print("KEY-VALUE PAIR-", cnt, ": ", at, "-->", v)
        cnt += 1
    text = elem.text
    print("*************************************************\n")
print("#$#$##$#$# element.iter() ENDS")


