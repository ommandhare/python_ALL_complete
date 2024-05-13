import re

text="welcome home.I hope you have nice day. Its my phone number 7350077732.Its my mail id ommandhare007@gmail.com. Bye"

# [] check the character with pattern
pattern = r'[a-f]'
match = re.findall(pattern, text)
print("\n\nTEXT: ",text)
print("PATTERN: ",pattern,"\nMATCH: ",match)
print("**********************************************")

# ^ caret to find line start with word or not
pattern = r'^welcome'
match = re.findall(pattern, text)
print("\n\nTEXT: ",text)
print("PATTERN: ",pattern,"\nMATCH: ",match)
if match:
    print(f"Yes line starts with {match} ")
print("**********************************************")


# $ to find out line end with word or not
pattern = r'Bye'
match = re.findall(pattern, text)
print("\n\nTEXT: ",text)
print("PATTERN: ",pattern,"\nMATCH: ",match)
if match:
    print(f"Yes line ends with {match} ")
print("**********************************************")


# multiple patterns
pattern = r'[p,s,l,w,o][^b,^e]'
match = re.findall(pattern, text)
print("\n\nTEXT: ",text)
print("PATTERN: ",pattern,"\nMATCH: ",match)
print("**********************************************")

# \ finds special seqeunce (\d finds all numeric value)
pattern = r'\d'
match = re.findall(pattern, text)
print("\n\nTEXT: ",text)
print("PATTERN: ",pattern,"\nMATCH: ",match)
print("**********************************************")


# . any character except newline
pattern = r'.'
match = re.findall(pattern, text)
print("\n\nTEXT: ",text)
print("PATTERN: ",pattern,"\nMATCH: ",match)
print("**********************************************")

# . any character and second is  d
pattern = r'.d'
match = re.findall(pattern, text)
print("\n\nTEXT: ",text)
print("PATTERN: ",pattern,"\nMATCH: ",match)
print("**********************************************")


# . any character and second is  d
pattern = r'.d'
match = re.findall(pattern, text)
print("\n\nTEXT: ",text)
print("PATTERN: ",pattern,"\nMATCH: ",match)
print("**********************************************")


#   +  finds exact letter occurances in file
pattern = r'om+'
match = re.findall(pattern, text)
print("\n\nTEXT: ",text)
print("PATTERN: ",pattern,"\nMATCH: ",match)
print("**********************************************")


#   *  finds first letter or exact letter occurances in file
pattern = r'om*'
match = re.findall(pattern, text)
print("\n\nTEXT: ",text)
print("PATTERN: ",pattern,"\nMATCH: ",match)
print("**********************************************")


#   ? Zero or one occurances
pattern = r'om?'
match = re.findall(pattern, text)
print("\n\nTEXT: ",text)
print("PATTERN: ",pattern,"\nMATCH: ",match)
print("**********************************************")

#   {} Exactly the specified number of occurrences
pattern = r'we.{2}om'
match = re.findall(pattern, text)
print("\n\nTEXT: ",text)
print("PATTERN: ",pattern,"\nMATCH: ",match)
print("**********************************************")

#   | Either this or that
pattern = r'nice|god'
match = re.findall(pattern, text)
print("\n\nTEXT: ",text)
print("PATTERN: ",pattern,"\nMATCH: ",match)
print("**********************************************")

# () Captures
pattern = r'(Its)'
match = re.findall(pattern, text)
print("\n\nTEXT: ",text)
print("PATTERN: ",pattern,"\nMATCH: ",match)
print("**********************************************")