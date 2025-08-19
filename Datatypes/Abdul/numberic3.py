import sys
# x=101
# y=12345678910101010101010110011010
# print(y) #12345678910101010101010110011010

# print(sys.getsizeof(x)) #28
# print(sys.getsizeof(y)) # 40

# x=101
# print(id(x)) #140723183935648
# x=205
# print(id(y)) # 2247921997744


################## Float

# a=29.75
# b=-3.75
# c=-2.5E2
# d=-3.1E-2

# print(a,b,c,d)
# # 29.75 -3.75 -250.0 -0.031

# print(sys.getsizeof(a)) #24
# print(sys.getsizeof(b)) #24
# print(sys.getsizeof(c)) #24
# print(sys.getsizeof(d)) #24

################## bool and complex 

# x=True
# y=False

# print(x,y) # True,False
# print(int(x),int(y)) #1,0

# # z=true 
# # print(z)
# #NameError: name 'true' is not defined

# print(type(x),type(y))
# #<class 'bool'> <class 'bool'>

# a=10
# b=5
# print(a>b) # True


########################### complex 

# c=10+5j
# print(c,type(c))
# # 10+5j --> complex

# c=complex(-5,-3.1)
# print(c)
# #(-5-3.1j)




