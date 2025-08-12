# class Emp:
#     def __init__(self):
#         print("This is a init method...")
#     def display(self):
#         print("This is display method...")

# emp1=Emp()
# emp2=Emp()

# emp1.display() # This is display method...
# emp.2display() # This is display method...


# #This is a init method...
# # This is a init method...


############   2
class Emp:
    count=0
    def __init__(self):
        Emp.count=Emp.count+1
    def display(self):
        print("This is display method...")

emp1=Emp()
emp2=Emp()

# print(Emp.count)  #2 

####################### 3

class Emp(object):
    # def name_salary(self,name,salary):
    #     self.name=name
    #     self.salary=salary
    #     return None 

    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
        return None

    def display(self):
        print(f'The name is ::{self.name}\n The salary is :: {self.salary}')    
        return None 

emp1=Emp("Ramu",56000)
# emp1.name_salary("Ramu",56000)
emp2=Emp("Narendra",90000)
# emp2.name_salary("Narendra",90000)

emp1.display()
emp2.display()


# Output:
# $ python constructor.py
# The name is ::Ramu
#  The salary is :: 56000
# The name is ::Narendra
#  The salary is :: 90000


