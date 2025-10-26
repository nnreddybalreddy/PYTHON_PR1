# def display(a,b):
#     print(a)
#     print(b)
#     return None 

# display(5,6) # 5,6
# display(a=5,b=4) # 5,4
# display(b=44,a=33) # 33,44
# #display(a=8,b=66,c=56) # TypeError: display() got an unexpected keyword argument 'c'


##########   2

# def display(**karg):
#     print(type(karg)) # <class 'dict'>

# display(a=1,b=2,c=3)

################  3

# def display(**karg):
#     print(karg)

# display(a=1,b=2)
# display(a=1,b=2,c=3)

# {'a': 1, 'b': 2}
# {'a': 1, 'b': 2, 'c': 3}


###########  4

# def display(p,**karg):
#     print(p)
#     print(karg)

# display(56,q=10,r=20)

#
   #   56
   #  {'q': 10, 'r': 20}
#



def display(**karg):
    for each in karg:
        print(each)    

display(a=1, b=2, c=3)
#a
#b
#c

