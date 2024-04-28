class Student:
   def  __init__(self,stdId,name,stdHt,stdWt,stdAge): ### constructor
       self.stdId = stdId
       self.name = name
       self.stdHt = stdHt
       self.stdWt = stdWt
       self.stdAge = stdAge
   def printStudent(self):
       print("\n################# GREAT GREAT GREAT#########################")
       print("STUDENT ID::::",self.stdId)
       print("STUDENT NAME::: ",self.name)
       print("STUDENT HEIGHT::: ",self.stdHt)
       if(self.stdAge > 60):
           print("############## SENIOR #########################")
       print("$##$#$#$#$#  STUDENT AGE::: ", self.stdAge , " @!@!@!@!@!@!!@!")
       print("*****************************************************")
