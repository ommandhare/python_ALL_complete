"""
read file containing details of professionals (doctor, engineer, etc).
Implement OOP solution and check polymorphism (see if correct method is getting called)

"""

import person as p
import doctor as d
import engineer as e


person_list = []

e1 = e.Engg("Pranav", "Kulkarni", 60, "M", "Mech", 300000)
person_list.append(e1)

d1 = d.Doctor("Rakesh", "Koparde", 60, "M", "EYE")
person_list.append(d1)



for obj in person_list:
    obj.print_person()  ### override and polymorphism
    print("####################")