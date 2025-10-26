# Local and Global
def fun():
    a=10
    print(a)
    

fun()
10

###############

# g=5.25
# print("Outside:::1",g)

# def fun():
#     a=10
#     print(a)

# fun()
# # Outside:::1 5.25
# # 10

######################

# g=5.25
# print("Outside:::1",g)

# def fun():
#     a=10
#     print(f'local: {a}')
#     print(f'global:::{g}')

# fun()
# # Outside:::1 5.25
# # local: 10
# # global:::5.25

#################################

# g=5.25
# print("Outside:::1",g)

# def fun():
#     a=10
#     print(f'local: {a}')
#     print(f'global:::{g}')

# fun()
# print("Outside:::2",g)
# # Outside:::1 5.25
# # local: 10
# # global:::5.25
# # Outside:::2 5.25

##################################

g=5.25
print("Outside:::1",g)

def fun():
    a=10
    g=199
    print(f'local: {a}')
    print(f'global:::{g}')

fun()
print("Outside:::2",g)
#   Outside:::1 5.25
#   local: 10
#   global:::199
#   Outside:::2 5.25

#########################################

g=5.25
print("Outside:::1",g)

def fun():
    a=10
    global g
    g=199
    print(f'local: {a}')
    print(f'global:::{g}')

fun()
print("Outside:::2",g)

# Outside:::1 5.25
# local: 10
# global:::199
# Outside:::2 199

################################

g=5.25

def fun():
    a=10
    print(f'local: {a}')
    print(f'global:::{g}')

g=5.25
fun()
g=5.25
#NameError: name 'g' is not defined

######################## 
# Declared outside all function
# Can be read inside all functins
# Cannot be modified unless global g is declared
# Must be declared before function call
##############################

x,y,z=5,1.25,"hi"

def fun():
    a,b,c=1,2,3
    print(locals())
    # {'a': 1, 'b': 2, 'c': 3}
    print(globals())
    #{'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__':
    #  <_frozen_importlib_external.SourceFileLoader object at 0x000001AF1B945390>,
    #  '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, 
    # '__file__': 'local_global.py', '__cached__': None, 
    # 'x': 5, 'y': 1.25, 'z': 'hi', 
    # 'fun': <function fun at 0x000001AF1B8FC2F0>}


fun()
#  locals() gives a dictonry of local variables
# globals() gives a dictionary of global variables



