def welcome():
    print("Welcome to function parameter example!")

def fun(f):
    f()

fun(welcome)
# Welcome to function parameter example!

#########################################

def add(x,y):
    return x+y

def sub(x,y):
    return x-y

def calculator(f,x,y):
    return f(x,y)

print(calculator(add,10,5))
# 15

print(calculator(sub,10,5))
# 5

