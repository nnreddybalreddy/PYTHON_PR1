# def display(a):
#     print(type(a))
#     return None 

# display(4) #class 'int'
# #display(4,5) #TypeError: display() takes 1 positional argument but 2 were given
# # No of variables are more

##################  2

# def display(*arg):
#     #print(type(arg)) # <class 'tuple'>
#     print(arg)
#     return None 

# display()
# display(4) 
# display(4,5)
# display(4,5,6)

#()
# (4,)
#(4, 5)
# (4, 5, 6)

############## 3 

# def display(*arg):
#     for each in arg:
#         print(each,end=' ')
#     return None 


# display(4,5,6)
# print("\n-----------")
# display("Hi",4,64)

# 4 5,6
# Hi,4,64

##################### 4


def display(*arg):
    for each in arg:
        print(type(each),end=' ')
    return None 


display(4,5,6)
print("\n-----------")
display("Hi",4.6,64)

# <class 'int'> <class 'int'> <class 'int'>
# -----------
# <class 'str'> <class 'float'> <class 'int'>
