#pop(index)
#remove(element)
#clear()
# del


# L1=[1,2,3,4,5,6]
# print(L1.pop())
# #6

# print(L1)
# # [1,2,3,4,5]


# L1=[1,2,3,4,5,6]
# print(L1.pop(2))
# #3

# print(L1)
# #[1,2,4,5,6]



# L1=[]
# L1.pop()
# # IndexError: pop from empty list

################ Remove

# L1=[1,2,3,4,5,3]
# L1.remove(3)

# print(L1)
# #[1, 2, 4, 5, 3]


# L1.remove(3)

# print(L1)
# #[1, 2, 4, 5]

################### Clear

L1=[1,2,3,4,5]
L1.clear()
print(L1)
#[]


L1=[1,2,3,4,5,6]
del L1[3]
print(L1)
#[1, 2, 3, 5, 6]



L1=[1,2,3,4,5,6]
del L1[1:4]
print(L1)
# [1,5,6]

L1=[1,2,3,4,5,6]

del L1

print(L1)
# NameError: name 'L1' is not defined









