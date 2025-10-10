#T=(iterable)
#for x in range(1,5):
#     print(x)


T=(x for x in range(1,5))
print(type(T))
# <class 'generator'>

T=(*(x for x in range(1,5)),)
print(type(T))
#<class 'tuple'>

print(T)
#(1, 2, 3, 4)


T2=tuple(x for x in range(1,5))
print(type(T2))
#class 'tuple'>
print(T2)
#(1,2,3,4)


T3=tuple(x**2 for x in range(1,5))
print(type(T3))
#<class 'tuple'>
print(T3)
#(1, 4, 9, 16)

T4=tuple(  x.lower() for x in "PyThoN")
print(type(T4))
#<class 'tuple'>    
print(T4)
#('p', 'y', 't', 'h', 'o', 'n')


T5=tuple(int(x) for x in "12345")
print(type(T5))
#<class 'tuple'>
print(T5)
#(1, 2, 3, 4, 5)
# 

T6=tuple(x for x in "ab*#%6" if x.isalpha())
print(type(T6))
#<class 'tuple'>    
print(T6)
#('a', 'b')