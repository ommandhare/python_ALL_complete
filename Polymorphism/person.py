# -*- coding: utf-8 -*-
"""
Created on Sat Jun 13 08:08:21 2020

@author: MANDAR
"""


class Person:
    def __init__(self, fname, lname,age,gender):
        self.first_name = fname
        self.last_name = lname
        self.__age = age #private variable
        self._gender = gender #protected variable
    def __test_private_method(self):
        print("this is test")
    def change_person_age(self, age):
        self.__age = age
    def test_private(self):
        self.__test_private_method()
    def print_tax(self):
        pass
    
    def print_person(self):
        print(self.first_name, self.last_name,self.__age, self._gender)
        
        
        