# class emp():
#     count=0
#     def get_name_age_salary(self,name,age,salary):
#         self.name=name 
#         self.age=age
#         self.salary=salary
#         self.increase_count_for_emp()
#         return None

#     def increase_count_for_emp(self):
#         emp.count=emp.count+1
#         return None    

#     def display_details(self):
#         print(f"The name is: {self.name}\n The age is : {self.age}\n Salary is::: {self.salary}")
#         return None

# emp1=emp()
# emp2=emp()

# emp1.get_name_age_salary("John",34,45000)
# # emp1.increase_count_for_emp()
# emp2.get_name_age_salary("Cliton",25,54000)
# # emp1.increase_count_for_emp()
# # print(dir(emp1))
# # 'age', 'display_details', 'get_name_age_salary', 'name', 'salary']

# # print(emp1.name)
# # print(emp1.age)
# # print(emp1.salary)

# emp1.display_details()



# print(emp.count)

class emp():
    count=0
    def get_name_age_salary(self,name,age,salary):
        self.name=name
        self.age=age
        self.salary=salary
        self.get_count_objs()
        return None

    def get_count_objs(self):
        emp.count=emp.count+1


    def display_details(self):
        print(f'name:{self.name}\nage:{self.age}\nsalary:{self.salary}')
        return None     

emp1=emp()
emp2=emp()

emp1.get_name_age_salary("John",34,45000)
emp2.get_name_age_salary("Ram",45,56000)

# print(dir(emp1))
# 'age', 'display_details', 'get_name_age_salary', 'name', 'salary']

print(emp1.name) # John

emp1.display_details()
# name:John
# age:34
# salary:45000

print(emp.count) #2


