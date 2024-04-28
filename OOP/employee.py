# -*- coding: utf-8 -*-
"""
Created on Sat Jun 20 19:58:06 2020

@author: MANDAR
"""
# int a=10 ==> 4 byte
# float b=10.0 ==> 8 byte
# Employee e ==> 32 byte
#always use meaningful names
# class Employee {
#
#
##
### Abstraction, Encaptulation, Inheritance, Polymorphism
class Employee: ### employee is one derived data type -- custom data type
   counEmployees = 0 ### class variable
   def  __init__(self,emp_id,name,age,height,salary,manager_id): ### __init__ is a constructor of class
       self.emp_id = emp_id #int
       self.name = name #string --> array of characters
       self.age = int(age) #int
       self.height = float(height) #float
       self.salary = float(salary) #float
       self.manager_id = manager_id #int
       #### increment class variable
       self.__class__.counEmployees +=1
       
   def print_employee(self):
       print("EMPLOYEE ID: ", self.emp_id)
       print("##############################################")
       print("EMPLOYEE NAME: ", self.name)
       print("##############################################")
       print("EMPLOYEE AGE: ", self.age)
       print("EMPLOYEE HEIGHT: ", self.height)
       print("EMPLOYEE SALARY: ", self.salary)
       print("::::::::::::::::::::EMPLOYEE MANAGER ::::::::::::::::: ")
       print("--------", self.manager_id)

   def print_name(self):
       print("Employee Name: ", self.name)

