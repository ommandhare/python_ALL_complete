
import person as p

class Doctor(p.Person): ## Doctor class is child class of person class
    def __init__(self, fname,lname,age,gender,speciality):
        super().__init__(fname,lname,age,gender)
        self.speciality = speciality
        
    def change_data(self,fname,lname,age,gender,speciality):
        self.first_name = fname
        self.last_name = lname
        #self.__age = age
        self._gender = gender
        self.speciality = speciality
        
        
    def __print_doctor_special(self):
       print("THIS METHOD CAN NOT BE CALLED FROM OUTSIDE")
       print(self.speciality)
       print(self.first_name,"_",self.last_name,self._gender)
        
    def print_gen(self):
        self.__print_doctor_special()
        self.print_person()
        
    def print_doctor(self):
        print("SUPER CLASS DATA ")
        super().print_person()
        print("CHILD CLASS DATA ")
        print("SPECIALITY: ", self.speciality)
        
    def print_tax(self):
        print("SAME METHOD FROM DOC::: ","Profit and Loss Based Tax")

    #override
    def print_person(self):
        print("OVERRIDE METHODE IN Doctor CLASS")
        print("######################112233445566###################")
        print("DR.",end="")
        print(self.first_name, self.last_name,self._gender)

  