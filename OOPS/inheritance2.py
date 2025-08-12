class Calculation1:
    def __init__(self,c,d):
        self.c=c
        self.d=d
    def sum(self,a,b):
        return a+b
  
 #Derived Class       
class Calc(Calculation1):
    def __init__(self,a,b,c,d):
        self.a=a
        self.b=b
        super().__init__(c,d)  #This is for to send the parameter to __init method of base class. 
        
    def div(self,a,b):
        return a/b
        
obj1=Calc(8,4,22,11)

div=obj1.div(obj1.a,obj1.b)
sum=obj1.sum(obj1.c,obj1.d) #The calculation is based on parameters passed to base class through Derived class. 

print("Div: ",div)
print("Sum: ",sum)

# def Calculation():
#     def __init__(self,c,d):
#         self.c=c
#         self.d=d 

#     def div(self,c,d):
#         print(c/d)

# def Calc(Calculation):
#     def __init__(self,a,b):
#         self.a=a 
#         self.b=b 
#         super().__init__(c,d)

#     def add(self,a,b):
#         print(a+b)


# c1=Calc(4,8,12,24)

# c1.div(c1.a,c1.b)
# c1.add(c1.c,c1.d)




  


