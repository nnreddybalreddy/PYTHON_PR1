# def myfunction1():
#     print("Welcome to functions")
#     myfunction2()
#     return None 

# def myfunction2():
#     print("Thanks you!!")
#     return None 

# myfunction1()


# def my_function1():
#     print("Welcome to functions")
#     myfunction2()
#     return None

# def myfunction2():
#     print("Thanks you!!")
#     return None


# my_function1()

############ output ############
#Welcome to functions
#Thanks you!!

#######2 

# def myfunction1():
#     print("x from function1",x)
#     return None

# def myfunction2():
#     print("x from function2",x)
#     return None 

# x=10
# myfunction1()
# myfunction2()

######## output ##########
# x from function1 10
# x from function2 10

###############
#### 3


# def myfunction1():
#     x=60
#     print("x from function1",x)
#     return None

# def myfunction2():
#     print("x from function2",x)
#     return None 

# #x=10
# myfunction1()
# myfunction2()

# NameError: name 'x' is not defined

##########

####### 4

# def myfunction1():
#     x=60 # Local variable 
#     print("x from function1",x)
#     return None

# def myfunction2():
#     print("x from function2",x)
#     return None 

# x=10 # Global variabel 
# myfunction1()
# myfunction2()

# x from function1 60 (Local variable is having priority)
# x from function2 10


########## 5

# def myfunction1():
#     x=60 # Local variable 
#     print("x from function1",x)
#     myfunction2()
#     return None

# def myfunction2():
#     print("x from function2",x)
#     return None 

# def  main():
#     x=10 
#     myfunction1()
#     return None 

# main()

###
#   print("x from function2",x)
#   NameError: name 'x' is not defined

##### 6

# def myfunction1():
#     x=60 # Local variable 
#     print("x from function1",x)
#     myfunction2()
#     return None

# def myfunction2():
#     print("x from function2",x)
#     return None 

# def  main():
#     global x
#     x=10
#     myfunction1()
#     return None 

# main()

# x from function1 60
# x from function2 10


############# 7

def myfunction1():
    x=60
    print("x from function1",x)
    return None

def myfunction2(y):
    print("y from function2",y)
    return None 

def  main():
    #global x
    x=10
    myfunction1()
    myfunction2(x)
    return None 

main()

# x from function1 60
# y from function2 10















