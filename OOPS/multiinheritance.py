  #Base Class 1. Multiple Inheritance. 
class Grandparent:
    Grandparent_name=' '
    def gp_name(self):
        print("Gp name:",self.Grandparent_name)

#Base Class 2: 
class Mother:
    mother_name=' '
    def print_mother(self):
        print("Mother name: ",self.mother_name)
    
#Base class 3        
class Father(Grandparent):
    father_name=' '
    def print_father(self):
        print("Father name: ",self.father_name) 
        
#Child class

class child(Mother,Father):
    def print_parent(self):
        print("Child class prints-----------")
        print("Father :",self.father_name)
        print("Mother :",self.mother_name)
     
        
obj1=child()        
obj1.mother_name='sita'
obj1.father_name='Ram'
obj1.Grandparent_name='Ravi'

print("Base class prints ------------------ ")

obj1.print_mother()
obj1.print_father()
obj1.gp_name()
obj1.print_parent()