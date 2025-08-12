class Tomoto:
    def Type(self):
        print("Veg")

    def color(self):
        print("Red")

class Apple:
    def Type(self):
        print("Fruit")
    
    def color(self):
        print("Red")
        

def Func(obj): #Function with obj have many forms.
    obj.Type()
    obj.color()
    
Obj_Tomoto=Tomoto()
Obj_Apple=Apple()

Func(Obj_Tomoto) #Veg , Red
Func(Obj_Apple) #Fruit, Red

# class Tomoto():
#     def type(self):
#         print("Veg")

#     def color(self):
#         print("Red") 

# class Apple():
#     def type(self):
#         print("Fruit")

#     def color(self):
#         print("Red")

# def func(obj):
#     obj.type()
#     obj.color()



# Obj_Tomoto=Tomoto()
# Obj_Apple=Apple()

# func(Obj_Tomoto)
# func(Obj_Apple)