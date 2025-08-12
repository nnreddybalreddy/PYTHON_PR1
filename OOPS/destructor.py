class Emp(object):
    def __init__(self,salary,age):
        self.salary=salary 
        self.age=age 

    def __del__(self):
        print("Delete object")

emp1=Emp(15000,65)