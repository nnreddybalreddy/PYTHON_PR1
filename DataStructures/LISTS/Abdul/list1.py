# L1=[1,2,3,4,5,6]
# print(L1)
# # [1, 2, 3, 4, 5, 6]

# L2=[1.8,1.8,3.5,4.6,5.7]
# print(L2)
# #[1.8, 1.8, 3.5, 4.6, 5.7]

# L3=["John","Angle"]
# print(L3)
# #['John', 'Angle']


# #List(iterable)
# L4=list((3,5,7,9))
# print(L4)
# #[3, 5, 7, 9]

# L5=list("abcde")
# print(L5)
# #['a', 'b', 'c', 'd', 'e']


# L6=[]
# print(L6)
# #[]

################ 2
# L1=[6,5,4,2,3,2]

# for i in L1:
#     print(i,end=' ')
# #   6 5 4 2 3 2

##########Hetroenous
L1=[7,3.2,"john",True,5+6j]
for i in L1:
    print(i,end=' ')
# 7 3.2 john True (5+6j)    

# L1[3]=5
# print(L1)
# # [7, 3.2, 'john', 5, (5+6j)]

# L1[2]="Raghu"
# print(L1)
# # [7, 3.2, 'Raghu', 5, (5+6j)]

# L1[2][3]='a'
# print(L1)
# #  TypeError: 'str' object does not support item assignment

################ Mutable
L1=[2,4,6,8,10,12]
L1[2]=16 #Modify
L1.append(25) #Append
print(L1)
# [2, 4, 16, 8, 10, 12, 25]



L1.remove(10)
print(L1)
# [2, 4, 16, 8, 12, 25]

# 	Ordered collection of heterogenous elements 
# 	It’s a mutable
# 	Can have duplicates


