import MyModule

print("Data from MyModule:", MyModule.data)
print("Addition from MyModule:", MyModule.add(20, 10))
print("Subtraction from MyModule:", MyModule.sub(20, 10))



# python MyProgram.py
# sum is: 15
# sub is: 5
# Data from MyModule: 500
# Addition from MyModule: 30
# Subtraction from MyModule: 10


#Result 2:
#Inclusion __name__ in module

# MyModule
# sum is: 15
# sub is: 5
#Data from MyModule: 500
#Addition from MyModule: 30
# Subtraction from MyModule: 10


#Result 3:
#Inclusion of __name__=="__main__" in module

# $ python MyProgram.py
# Data from MyModule: 500
# Addition from MyModule: 30
# Subtraction from MyModule: 10


