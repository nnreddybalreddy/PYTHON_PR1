# class Person(object):
#     def assign(self,name,age):
#         self.name=name
#         self.age=age 
#         return None 
    
#     def display(self):
#         print(self.name,self.age)
#         return None 

# per1=Person()
# per1.assign("john",21)
# # #per1.display() #John , 21
# # print(per1.name) # Jo hn
# # print(per1.age)  # 21

########### 2

# class Person(object):
#     def assign(self,name,age):
#         self.name=name
#         self.__age=age 
#         return None 
    
#     def __display(self):
#         print(self.name,self.age)
#         return None 

# per1=Person()
# per1.assign("john",21)
# # print(per1.__age)
# print(per1.__display())

############ 3

class Person(object):
    def assign(self,name,age):
        self.name=name
        self.__age=age 
        self.__display()
        return None 
    
    def __display(self):
        print(self.name,self.__age)
        return None 

per1=Person()
per1.assign("john",21)
# print(per1.__age)
# print(per1.__display())