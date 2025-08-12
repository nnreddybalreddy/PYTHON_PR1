class Bird():
    def about(self):
        print("They are diff types of birds")
    
    def fly(self):
        print("Some birds can fly and some or not fly")

class parrot(Bird):
    def fly(self):
        print("Parrot can fly")

class penguin(Bird):
    def fly(self):
        print("Penguin cannot fly")
        
        
obj_Bird=Bird()
obj_parrot=parrot()
obj_penguin=penguin()


print('--------- Bird---------')
obj_Bird.about() #They are diff types of birds
obj_Bird.fly() #Some birds can fly and some or not fly

print("parraot------------------")

obj_parrot.about() #They are diff types of birds
obj_parrot.fly() #Parrot can fly

obj_penguin.about()#They are diff types of birds
obj_penguin.fly() # Priority will given to Derived class. Penguin cannot fly