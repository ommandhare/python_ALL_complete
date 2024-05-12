import re
## CUSTOMERID.*
test_str = "welcome to python 7720036071 no of students are learning python with 36 assignments welcome 9902920121"
multi_str = '''maaaaaaaandar
ra
ma
mmadhav
nitin
abhijit
ranish
mohan
jaydeep
mahesh
sachin
vinod
soham
sohamaaaaa
ta
'''

### . indicates any one character except newline character -  1 letter
### [] list -- any one from the list - 1 letter
### [^] list -- not in list - 1 letter
### + one or more occurance of previsou pattern -- more than one letter (variable size pattern)
### * zero or more accurance of previous pattern -- zero or more letters (variable size pattern)
### ? makes previous pattern optional (previous pattern can occur one or zero times)

print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
s = r'\nPranav Kulkarni'
print(s)
print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")

#[pslw]
### fix size patterns
### variable size patterns
pattern = r'[p,s,l,w,o][^b,^e]'
match = re.findall(pattern, test_str)
print("\n\nTEST STR: ",test_str)
print("PATTERN: ",pattern,"\nMATCH: ",match)
print("**********************************************")


pattern = r'[1-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]'
match = re.findall(pattern, test_str)
print("\n\nTEST STR: ",test_str)
print("PATTERN: ",pattern,"\nMATCH: ",match)
print("**********************************************")
print("**********************************************")

pattern = r'[0-9]+'
testStrS = '\tes\nttest'
print(testStrS)
testStrWS = r'\tes\nttest'
print(testStrWS)
# what is string--- anything that is enclosed in single or double quotes is a string
# what is a raw string -- prefix r to a string definition --
# --and string will be considered as raw (no speical meaning characters are evaluated.
#print(testStrS)
#print(testStrWS)
match = re.findall(pattern, test_str)
print("\n\nTEST STR: ",test_str)
print("PATTERN: ",pattern,"\nMATCH: ",match)

pattern = r'.[^ ,^e][0-9]'
match = re.findall(pattern, test_str)
print("\n\nTEST STR: ",test_str)
print("PATTERN: ",pattern,"\nMATCH: ",match)

print("**********************************************")
pattern = r'.[^e,^p][0-9,a-z]'
match = re.findall(pattern, test_str)
print("\n\nTEST STR: ",test_str)
print("PATTERN: ",pattern,"\nMATCH: ",match)

print("**********************************************")





pattern = r'.[a,b]'
match = re.findall(pattern, test_str)
print("\n\nTEST STR: ",test_str)

print("**********************************************")
pattern = r'[^ 0-9]+'
match = re.findall(pattern, test_str)
print("\n\nTEST STR: ",test_str)
print("PATTERN: ",pattern,"\nMATCH: ",match)
print("**********************************************")

pattern = r'[0-9]+'
my_str = "welcome to python 1234 no of students are learning python with 36 assignments"
match = re.findall(pattern, my_str)
print("\n\nTEST STR: ",my_str)
print("PATTERN: ",pattern,"\nMATCH: ",match)
print("**********************************************")

print("PATTERN: ",pattern,"\nMATCH: ",match)

pattern = r'[a-z0-9][^ ]+'
my_str = "welcome             to python 1234 no of students are learning python with 36 assignments"
match = re.findall(pattern, my_str)
print("\n\nPATTERN: ",pattern,"\nMATCH: ",match)
print("**********************************************")

##### why this pattern does not work as expected...... code nit pahava.. hota aahe :-)
pattern = r'[^ ][a-zA-Z]+'
match = re.findall(pattern, test_str)
print("\n\nPATTERN: ",pattern,"\nMATCH: ",match)
print("**********************$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$************************")

pattern = r'm.*'
test_str1 = "om Mandhare is our student."
match = re.findall(pattern, test_str1)
print("\n\nTEST STR: ",test_str1)
print("PATTERN: ",pattern,"\nMATCH: ",match)
print("************************$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$**********************")

pattern = r'm.+'
match = re.findall(pattern, multi_str)
print("\n\nPATTERN: ",pattern,"\nMATCH: ",match)
print("**********************************************")

pattern = r'ma+'
match = re.findall(pattern, multi_str)
print(" INPUT STR: ",multi_str)
print("\n\nPATTERN: ",pattern,"\nMATCH: ",match)
print("**********************************************")

pattern = r'ma*'
match = re.findall(pattern, multi_str)
print("\n\nPATTERN: ",pattern,"\nMATCH: ",match)
print("**********************************************")


pattern = r'm[o,a].*'
match = re.findall(pattern, multi_str)
print("\n\nPATTERN: ",pattern,"\nMATCH: ",match)
print("**********************************************")

pattern = r'.a.*'
match = re.findall(pattern, multi_str)
print("\n\nPATTERN: ",pattern,"\nMATCH: ",match)
print("**********************************************")

##### something to look for end of the string ???????????
#### caret looks only at begining of the string
pattern = r'^.el[^ ]*'
patternC = r'\w+g$'
test_str = "Welcome to wag python and data warehouseing"
match = re.findall(patternC, test_str)
print("\n\nTEST STR: ", test_str)
print("PATTERN: ",pattern,"\nMATCH: ",match)
print("**********************************************")

#### caret looks only at begining of the string
pattern = r'.el[^ ]*'
match = re.findall(pattern, test_str)
print("\n\nTEST STR: ", test_str)
print("PATTERN: ",pattern,"\nMATCH: ",match)
print("**********************************************")


#### caret looks only at begining of the string
pattern = r'^.a.*'
match = re.findall(pattern, multi_str)
print("\n\nPATTERN: ",pattern,"\nMATCH: ",match)
print("**********************************************")


pattern = r'm?a.*'
match = re.findall(pattern, multi_str)
print("\n\nPATTERN: ",pattern,"\nMATCH: ",match)
print("**********************************************")


pattern = r'[rjs]a.*'
match = re.findall(pattern, multi_str)
print("\n\nPATTERN: ",pattern,"\nMATCH: ",match)
print("**********************************************")

pattern = r'[rjs][ao].*'
match = re.findall(pattern, multi_str)
print("\n\nPATTERN: ",pattern,"\nMATCH: ",match)
print("**********************************************")

pattern = r'[rjs]a.+'
match = re.findall(pattern, multi_str)
print("\n\nPATTERN: ",pattern,"\nMATCH: ",match)
print("**********************************************")

pattern = r'[rjs]?a.+'
match = re.findall(pattern, multi_str)
print("\n\nPATTERN: ",pattern,"\nMATCH: ",match)
print("**********************************************")


pattern = r'[rjs]?a.*'
match = re.findall(pattern, multi_str)
print("\n\nPATTERN: ",pattern,"\nMATCH: ",match)
print("**********************************************")


pattern = r'[rjs]?a.*'
match = re.findall(pattern, multi_str)
print("\n\nPATTERN: ",pattern,"\nMATCH: ",match)
print("**********************************************")


#### \b tells search whole words only search
pattern = r'[jvh].*'
match = re.findall(pattern, multi_str)
print("\n\nPATTERN: ",pattern,"\nMATCH: ",match)
print("**********************************************")
#### \b tells search whole words only search
pattern = r'\b[jvh].*\b'
match = re.findall(pattern, multi_str)
print("\n\nPATTERN: ",pattern,"\nMATCH: ",match)
print("**********************************************")

#### need to look more in \b
#### \b tells search whole words only search
pattern = r'welc\b'
my_str = "welc****ome to python 1234 no of students are learning python with 36 assignments welcome"
match = re.findall(pattern, my_str)
print("TEST STR: ",my_str)
print("PATTERN: ",pattern,"\nMATCH: ",match)


pattern = r'[jvh].*\b'
match = re.findall(pattern, multi_str)
print("\n\nPATTERN: ",pattern,"\nMATCH: ",match)
print("**********************************************")


pattern = r'\b.*[jvh].*\b'
match = re.findall(pattern, multi_str)
print("\n\nPATTERN: ",pattern,"\nMATCH: ",match)
print("**********************************************")


