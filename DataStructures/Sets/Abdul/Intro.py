S2={1,2,2,3,3,4,5,6}
#Collection of distinct elements
print(S2) #Disnct elements
#Output: {1, 2, 3, 4, 5, 6}

S3={1,2.5,"Jack",True,3+4j}
#heterogeneous elements

# Indexing and Slicing are not allowed in Sets
# S3[2] #TypeError: 'set' object is not subscriptable

#s3[1:4] #TypeError: 'set' object is not subscriptable
#Unordered

#Creation of sets

S1={1,2,3,4,5,6}
print(type(S1))
#<class 'set'>
print(S1)
#Output: {1, 2, 3, 4, 5, 6}

#S2=set(iterable)
S2=set([1,2,3,4,5,6])
print(type(S2))
# {<class 'set'> }
print(S2)
#Output: {1, 2, 3, 4, 5, 6}

S3=set('Python')
print(type(S3))
# <class 'set'>
print(S3)
#Output: {'h', 'P', 'n', 'o', 't', 'y'}

S4={5}
print(type(S4))
#<class 'set'>
print(S4)
#Output: {5}

S5=set()
print(type(S5))
#<class 'set'>
print(bool(S5))
#Output: False
print(S5)
#Output: set()

S6={}
print(type(S6))
#<class 'dict'>


########### Unordered


S1={10,20,30,40,50}
print(S1)
#Output: {40, 10, 50, 20, 30}
print("\n")

for i in S1:
    print(i,end=" ")

print("\n")
#40 10 50 20 30

#Mutable
S1={10,20,30,40,50}

S1.add(60)
print(S1)
#Output: {40, 10, 50, 20, 60, 30}


S1.add("Hi")
print(S1)
#Output: {40, 10, 50, 20, 'Hi', 60, 30}

S1.add((1,2,3))
print(S1)
#{40, 'Hi', 10, (1, 2, 3), 50, 20, 60, 30}

# S1.add([1,2,3])
# print(S1)
#list is mutable
# #TypeError: unhashable type: 'list'

#### REmove


S1={10,20,30,40,50}
S1.remove(30)
print(S1)
#Output: {40, 10, 50, 20}


print(S1.pop())
#Output: 40 Dont know which element will be removed

#Mutable are not hasable


