import json

# json object exist as a string.
p = '{"name": "Bob", "languages": ["Python", "Java"]}'

p2 = '[{"name": "Bob", "languages": ["Python", "Java"]},\
{"name":"Aditya","languages":["Python", "Java","scala"]},\
{"name":"OM","languages":["c","c++","python","java","php","scala"]}]'

personJson = json.loads(p2)
for obj in personJson:
    for k,v in obj.items():
        print("KEY: ",k, " VALUE: ",v)

print("###############################")
## get languages for OM
l = personJson[2]["languages"]
print(l)
for rec in personJson:
    #print(rec)
    print(rec['languages'])