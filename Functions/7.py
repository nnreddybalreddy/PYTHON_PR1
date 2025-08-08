# def display(a):
#     print(f'a={a}')
#     return None 

# display(4) # 4

##########2 

# def display(a):
#     print(f'a={a}')
#     return None 

# display() 
# TypeError: display() missing 1 required positional argument: 'a' 


#########   3
# def display(a=1):
#     print(f'a={a}') # a=1
#     return None 

# display() #1
# display(4) # a=4
# display(5.5) # a=5.5


##########  4

# def add_numbers(p, q):
#     result = p + q
#     print(f'Result: {result}')
#     return None

# add_numbers(5,6)  # Result: 11
# #add_numbers()  #TypeError: add_numbers() missing 2 required positional arguments: 'p' and 'q'


#####################  5

# def add_numbers(p, q=10): # Default value for q=10 
#     result = p + q
#     print(f'Result: {result}')
#     return None

# add_numbers(5,6)  # Result: 11
# add_numbers(10)  # Result: 20
 

################ 6

# def add_numbers(p=20, q=10): # Default value for q=10 
#     result = p + q
#     print(f'Result: {result}')
#     return None

# add_numbers()  # Result: 30


################ 7

# def add_numbers(p, q=10): # Default value for q=10 
#     result = p + q
#     print(f'Result: {result}')
#     return None

# add_numbers(5)  # Result: 15


#############  8

# def add_numbers(p=5, q):  
#     result = p + q
#     print(f'Result: {result}') # SyntaxError: non-default argument follows default argument

#     return None

# add_numbers(5)  

############## 9 

# def add_numbers(p, q=22):   # default values are alwyas right
#     result = p + q
#     print(f'Result: {result}') 

#     return None

# add_numbers(5)  # 27

########### 10
def add_numbers(p, q=22):  
    result = p + q
    print(f'Result: {result}') 

    return None

add_numbers(5)  # 27
add_numbers(10,20)  # 30
add_numbers(10) #32

