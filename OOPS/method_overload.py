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
        

def Func(obj):
    obj.Type()
    obj.color()
    
Obj_Tomoto=Tomoto()
Obj_Apple=Apple()

Func(Obj_Tomoto) #
Func(Obj_Apple)