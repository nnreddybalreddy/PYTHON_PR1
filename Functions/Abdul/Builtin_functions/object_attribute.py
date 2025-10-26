########Type
# type(object,bases=None,dict=None) -> a type object

print(type(10))
#<class 'int'>
print(type(10.5))
#<class 'float'>
print(type("Hello"))
#<class 'str'>
print(type(True))
#<class 'bool'>
print(type([1,2,3]))
#<class 'list'>
print(type((1,2,3)))
#<class 'tuple'>    
print(type({1,2,3}))
#<class 'set'> 
print(type({"a":1,"b":2}))
#<class 'dict'>
print(type(None))
#<class 'NoneType'>
# 

############# isistance
# 
# isinstance(object,classinfo) -> bool
# 
x=10
print(isinstance(x,int))
#True
print(isinstance(x,float))
#False
print(isinstance(x,(int,str)))
#True
# 
# 
##hasattr
#hasattr(object,attribute) -> bool

s="Hello World"
print(hasattr(s,"find"))
#True
print(hasattr(s,"islower"))
#True
print(hasattr(s,"search"))
#False


#################getattr    
#getattr(object,attribute,default=None) -> value

import math
print(getattr(math,"pi"))
#3.141592653589793
# 

print(getattr(math,"sqrt")(16))
#4.0

#####################ID
#id(object) -> integer

x=10
y=10

print(id(x),id(y))
#140732799907888 140732799907888

L1=[1,2,3]
L2=[4,5,6]
print(id(L1),id(L2))
#140732778823680 140732778824064

############dir
#dir(object) 

# print(dir(list))
# #['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter


print(dir(math))
# #['__doc__', '__loader__', '__name__', '__package__', '__spec__', 'acos', 'acosh', 'asin', 'asinh', 'atan', 'atan2', 'atanh', 'ceil', 'comb', 'copysign', 'cos', 'cosh', 'degrees', 'dist', 'e', 'erf', 'erfc', 'exp', 'expm1', 'fabs', 'factorial', 'floor', 'fmod', 'frexp', 'fsum', 'gamma', 'gcd', 'hypot', 'inf', 'isclose', 'isfinite', 'isinf', 'isnan', 'isqrt', 'ldexp', 'lgamma', 'log', 'log10', 'log1p', 'log2', 'modf', 'nan', 'perm', 'pi', 'pow', 'prod', 'radians', 'remainder', 'sin', 'sinh', 'sqrt', 'tan', 'tanh', 'tau', 'trunc']

#########repr
#repr(object) -> string

text="Hello World"
print(repr(text))
#"Hello World"