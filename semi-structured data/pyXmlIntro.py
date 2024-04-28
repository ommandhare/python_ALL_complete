import xml.etree.ElementTree as ET
### xml file has 3 important things
### 1 name of the tag
### 2 attributes of that tag :: attributes of that tag are stored in dict (elementTree)
### 3 value of the tag -- 3.1  --> text, 3.2 it can be another tag, 3.3 combination of value and other tags
### sample xml tag:::: <nameOfTag attributes>value</nameOfTag>, <tagname with or without attrib />

### using for loop we can browse over list of child tags of a particular tag
# (it goes only one level deep its not a recurssion)

### findall function of element class in elementTree looks
# for tags by tag name in immediate chlid list of the tag that calls find all

## tree.iter() -- recurssive function -- query tree recurssively for selected tag

## how to modify existing xml file and create a new version of xml with updated tag attribs

## how to write our own recurrssive function to browse over xml file.


### Read xml file
tree = ET.parse(r'C:\Users\HP\PycharmProjects\pythonProject.py\venv\Assignments/CountryTest.xml')
print("TYPE OF TREE: ",type(tree))
for elem in tree.iter():
    tag = elem.tag
    attrib = elem.attrib
    print(" TAG : ",tag)
    print(" TAG ATTRIB: ", attrib, "attrib type:: ", type(attrib), "LENTGH OF THE ATTRIB DICT: ", len(attrib))
    print(" PRINTING TEXT: ", elem.text)
    ##print(type(attrib))
    cnt=0
    for at,v in attrib.items():
         print("KEY-VALUE PAIR-",cnt,": ",at, "-->", v)
         cnt+=1
    text = elem.text
    print("*************************************************\n")
print("#$#$##$#$# element.iter() ENDS")

    
