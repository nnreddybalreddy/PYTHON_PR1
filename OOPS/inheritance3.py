class Mother():
    mother_name=' '
    def print_mother(self):
        print("Mother name: ",self.mother_name)
    
#Base class 2        
class Father():
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
obj1.mother_name='sita'#Mother name:  sita
obj1.father_name='Ram' #Father name:  Ram

print("Base class prints ------------------ ")

obj1.print_mother() #Father : Ram
obj1.print_father() #Mother : sita


# class Mother():
#     mother_name=""
#     def mother_name(self):
#         print(self.mother_name)

# class Father():
#     father_name=""
#     def father_name(self):
#         print(self.father_name)

# class child(Mother,Father):
#     def print_parent(self):
#         print("Child class print...")
#         print("Father:",self.father_name)
#         print("Mother:",self.mother_name)
# c1=child()
# c1.mother_name="Sita"
# c1.father_name="Ram"

# c1.print_parent()