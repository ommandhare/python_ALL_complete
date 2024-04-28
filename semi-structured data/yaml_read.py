import yaml
#--- for installing yaml::: python -m pip install pyyaml
# Semistructured Data Formats are useful for data transfer (on network)
# especially for sparce data.
# Semistructured Data can easily represent OBJECT Models
# Appications: configuration files(for ex. Hadoop Conf), data transfer (for ex. Twitter, Facebook), parameter files,
# devOps tools(Maven, SBT), cloud formation (infrastructure as code)
# no sql data bases use xml or json.
# Advanced Data Warehousing Tools like Snowflake support xml and json formats
## yaml supports integer, float, strings, Boolean and Dates - format ISO8601, null values as well
## yaml list
### counries:
#       - india
#       - usa
# indentation is important
# Block Sequence and Flow Sequence
# Flow Sequence--- Countries: [india,usa]

## Dictionary
## country:
#       name:india
#       size:large

## Yaml pipe: | literal block, all new lines, indentation, extra spaces everything preserved as it is .

## Yaml greatr than sign::: folder block. it renders text as single line all new lines will be converted to single space
### all blank lins will be converted to new line.
#print(dir(yaml))

#with open(r"C:\Users\HP\PycharmProjects\pythonProject.py\venv\Assignments\semi-structured data\yaml_simple.yaml") as f:
#with open(r"C:\Users\HP\PycharmProjects\pythonProject.py\venv\Assignments\semi-structured data\yaml_lists.yaml") as f:
#with open(r"C:\Users\HP\PycharmProjects\pythonProject.py\venv\Assignments\semi-structured data\yaml_dict.yaml") as f:
with open(r"C:\Users\HP\PycharmProjects\pythonProject.py\venv\Assignments\semi-structured data\nested_yaml_dict.yaml") as f:
#with open('D:\PythonWork\Data\category2.yaml') as f:
   document = yaml.safe_load(f)
   #document = yaml.load(f,Loader=yaml.FullLoader)
   print(type(document))

   for key,value in document.items():
       print(key, "= " ,value)
       print("DATA TYPE OF VALUE: ", type(value))

queryOutput = document['client1']['assistants'][0]['assistant1'][0]

#queryOutput = document['client1']['assistants'][0]['assistant1']

print("QUERYING YAML FILE DIRECTLY::::::::::")
print("QUERY OUTPUT::: ", queryOutput)
print("type_of: ",type(queryOutput))
"""
client = document['client6']
print("type of value", type(client))
nameOfClient = client['name']
#assistants = client['assistants']
companyTypeClient = client['type']
companySize = client['companySize']
print("COMPANY SIZE: ", companySize, "TYPE: ", type(companySize))
assistant0 = assistants[0]
print("Name of the client: ", nameOfClient)
print("COMPANY TYPE FOR Client: ", companyTypeClient)
print("TYPE OF ASSISTANTS VALUE: ", type(assistants))
print("TYPE OF FIRST ASSISTANT VALUE: ", type(assistant0))


### deprication warning == for any product some old features are no more supported after
# #   avanced versions are available (instead some alternative, better features are available)
'''
   sports_list = document['sports']
   print(type(sports_list))
   
   countries = document['countries']
   print(type(countries))
   
   us = countries[0]
   print(type(us))
   print(us)
"""
