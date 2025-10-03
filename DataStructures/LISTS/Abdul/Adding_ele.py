#append --> Insert at end as one value
# extend(iterable) --> Insert at the end of list with more elements 
# insert(index,ele)
#copy --> duplicate the list 

# L1=[1,2,3,4,5]
# L1.append(6)
# print(L1)
# #[1, 2, 3, 4, 5, 6]

# # # L1.append(7,8)
# # # #TypeError: append() takes exactly one argument (2 given)

# L1=[]
# L1.append(10)
# print(L1)
# #10
# L1.append("python")
# print(L1)
# #[10, 'python']
# L1.append([1,2])
# print(L1)
# #[10, 'python', [1, 2]]


# L1=[1,2,3,4,5]
# L1[5:5]=[10]
# print(L1)
# #[1, 2, 3, 4, 5, 10]
# L1[len(L1):]=[12]
# print(L1)
# #[1, 2, 3, 4, 5, 10, 12]

# # ###############
# # #### Extend

# L1=[1,2,3,4]
# L1.extend([5,6,7])
# print(L1)
# #[1, 2, 3, 4, 5, 6, 7]


# L1=[1,2]
# L1.extend("python")
# print(L1) # only iterable

# # [1, 2, 'p', 'y', 't', 'h', 'o', 'n']

# L1=[1,2,3,4]
# L1.extend(range(5,8))
# print(L1)

####################### Insert
##### insert 

# L1=[1,2,3,4]

# L1.insert(0,50)
# print(L1)
# #[50, 1, 2, 3, 4]


# L1.insert(70,"Python")
# #Last index
# print(L1)
# # [50, 1, 2, 3, 4, 'Python']

# L1=[1,2,3,4]
# L1.insert(2,"python")
# print(L1)
# #[1, 2, 'python', 3, 4]


# L1=[1,2,3,4]
# L1[2:2]=[55]
# print(L1)
# # [1, 2, 55, 3, 4]

############## copy

L1=[1,2,3,4]
L2=L1.copy()
#shallow copy
print(L1)
print(L2)
#[1, 2, 3, 4]
#[1, 2, 3, 4]


L2[0]=6
print(L1)
print(L2)
#[1, 2, 3, 4]
#[6, 2, 3, 4]

