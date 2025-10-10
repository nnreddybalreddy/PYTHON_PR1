t1=(1,2,3,4,5,6)
print(type(t1))
# <class 'tuple'>
print(t1)
#(1, 2, 3, 4, 5, 6)

t2=tuple([1,2,3,4,5,6])
print(type(t2))
#<class 'tuple'>
print(t2)
#(1, 2, 3, 4, 5, 6)

t3=tuple("python")
print(type(t3)) 
# ('p', 'y', 't', 'h', 'o', 'n')
print(t3)
# <class 'tuple'>

t4=tuple(range(1,5))
print(type(t4))
#<class 'tuple'>
print(t4)
# (1, 2, 3, 4)

t5=()
print(type(t5))
#<class 'tuple'>
print(t5)
# ()

t6=(5)
print(type(t6)) 
# <class 'int'>


t7=(5,)
print(type(t7))
# <class 'tuple'>
print(t7)
# (5,)

t8=10,11,12,13,14
print(type(t8))
# <class 'tuple'>
print(t8)
# (10, 11, 12, 13, 14)


############# TRAVERSE

t1=(6,5,4,3,2,1)
print(t1[0]) #6
print(t1[-1]) #1
print(t1[-3]) #3
print(t1[2:5]) #(4, 3, 2)

# t1[2]=10
# #TypeError: 'tuple' object does not support item assignment


for i in t1:
    print(i,end=" ")
#6 5 4 3 2 1
# 
print()    



