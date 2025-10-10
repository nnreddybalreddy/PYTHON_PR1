#Concatination
            # + 

# Repetation:
             # *

# Packing and unpacking:
         # * 

#membership
    # in , not in

T1=(1,2,3)

T2=(8,9,10)

print(T1+T2)
#  (1, 2, 3, 8, 9, 10)

#Repetation

T1=(1,2,3)
print(T1*5)
# (1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3)

#packing and unpacking

T1=1,2,3,4,5
print(type(T1)) #single variable for multiple variables as tuple
# <class 'tuple'>
a,b,c,d,e=T1 #multiple variables for single variable as tuple
print(a,b,c,d,e)
# (1 2 3 4 5)

############

# a,b,c=T1 #ValueError: too many values to unpack (expected 3)

a,b,*c=T1

print(a,b,c)
# a=1 b=2 c=[3, 4, 5]

a,*b,c=T1
print(a,b,c)
# a=1 b=[2, 3, 4] c=5

*a,b,c=T1
print(a,b,c)
# a=[1, 2, 3] b=4 c=5

#membership

t1=[1,2,3,4,5]

print(1 in t1) #True

print(3 not in t1) #False


