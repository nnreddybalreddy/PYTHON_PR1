# Nested Function
# Return Function
# Inner Function access to outer variables
# Function as parameter

def Outer(f):
    def Inner():
        print("*" * 10)
        f()
        print("*" * 10)
    return Inner    
    
def welcome():
    print("Welcome to Decorator Function")

f=Outer(welcome)
f()
# **********
# Welcome to Decorator Function 
# **********


# #################################################

def Outer(f):
    def Inner():
        print("*" * 10)
        f()
        print("*" * 10)
    return Inner

def display():
    print("Display Function")   

#case 1
# r=Outer(display)
# r()

#case 2
display=Outer(display)
display()

# **********
# Display Function  
# **********

#case 3
# display=Outer(display)
display()
# **********
# Display Function  
# **********


# case 4 :Decorator

def Outer(f):
    def Inner():
        print("*" * 10)
        f()
        print("*" * 10)
    return Inner

@Outer
def display():
    print("Display Function") 

display()
# #**********
# Display Function
# **********


# case 5
def decorator(f):
    def Inner():
        print("*" * 10)
        f()
        print("*" * 10)
    return Inner

@decorator
def display():
    print("Display Function") 

display()

# **********
# Display Function  
# **********
