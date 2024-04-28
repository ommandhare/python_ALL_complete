# -*- coding: utf-8 -*-
"""
Created on Sun Jun 14 14:59:14 2020

@author: MANDAR
"""
#### polymorphism --- one morphology multiple behaviours -- frog -- swims in water, walks on land
#### 1. operator
#### 2. functions - methods
#### 3. classes

##### polymorphism - operator
###-- operator overloading
a = 10
b = 15
c = a+b
print(c) ### 25

a = "Priyanka"
b = "Nikam"

c = a + "_" + b
print(c) ### Priyanka_Nikam

##c = a + 10

#in this case operator + is showing polymorphism

a = [1,2,3]
b = [4,5]

c = a + b
print(c) #### [1,2,3,4,5]
a=2
c = a*2
print(c)
a = "satish"
a = a*2
print(a)

########################## Function polymorphism ####################

a = "welcome to python"
b = [2,3,4,5,6,7,[2,3,4]]
c = {"soham":56, "saurabh":87, "swati":12,"siddhi":[1,2,3]}

l = len(a)
m = len(b)
n = len(c)

print(l)
print(m)
print(n)
#####
print(a)
print(b)
print(c)
########################## polymorphism of class ######################
import person as p
import doctor as d
import engineer as e


person_list = []
e1 = e.Engg("Pranav", "Kulkarni", 60, "M", "Mech", 300000)
person_list.append(e1)
d1 = d.Doctor("Rakesh", "Koparde", 60, "M", "EYE")
person_list.append(d1)

print(person_list)
print("$@$#$@$@$@$@$@$@$@$@$@$@$@$@$@$@$@$@")
for obj in person_list:
    print("OBJECT: ",obj)
    print("THIS NEW OBJECT is of : ", type(obj), ":::::TYPE")
    obj.print_person() ### override and polymorphism
    obj.print_tax() # example of polymorphism
              

"""
prof_list = []

for line in open("F:\PRESENTATIONS\Python\Doc_Engg.txt"):
    print(line)
    Prof,fname,lname,age,gender,Speciality,Sal = line.strip().split(",")
    if(Prof == "DOC"):
        doc = d.Doctor(fname,lname,age,gender,Speciality)
        prof_list.append(doc)
    else:
        eng = e.Engg(fname,lname,age,gender,Speciality,Sal)
        prof_list.append(eng)
        
for obj in prof_list:
    obj.print_person() ### override and polymorphism
    obj.print_tax() # example of polymorphism
              
"""



