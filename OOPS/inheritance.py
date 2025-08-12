class Calculation1:
    def sum(self,a,b):
        return a+b
  
 #Derived Class       
class Calc(Calculation1):
    def __init__(self,a,b):
        self.a=a
        self.b=b
        
    def div(self,a,b):
        return a/b
        
obj1=Calc(8,4)

div=obj1.div(obj1.a,obj1.b) #Derived class accessing
sum=obj1.sum(obj1.a,obj1.b) #Base class accessing 

print("Div: ",div) #2.0
 
print("Sum: ",sum) #12

# class Calculation():
#     def sum(self,a,b):
#         print(a+b) 

# class Calc(Calculation):
#     def __init__(self,a,b):
#         self.a=a 
#         self.b=b 

#     def div(self,a,b):
#         print(a/b)

# c1=Calc(4,8)
# c1.div(c1.a,c1.b)

# c1.sum(c1.a,c1.b)



