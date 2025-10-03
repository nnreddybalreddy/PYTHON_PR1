# index(element,start,end)

# L1=[10,20,30,40,10,20,30,20]
# print(L1.index(20))
# # 1

# print(L1.index(20,2))
# # 5

# print(L1.index(20,2,6))
# # 5


# # ######### Count
# # #  count

# #count(element)

# L1=[10,20,30,40,10,30,20,40]
# print(L1.count(20))
# # #2

# # ############# reverse

# L1=[10,20,30,40,50,60,70]
# L1.reverse()
# print(L1)
# #[70,60,50,40,30,20,10]

# # ########## sort

# # # #sort(*,key=None,reverse=False)
# # # # key valued values

L1=[70,10,60,20,50,30,40]
L1.sort()
# increasing order
print(L1)
#[10, 20, 30, 40, 50, 60, 70]
# by default increasing order

L1=[70,10,60,20,50,30,40]
L1.sort(reverse=True)
print(L1)
#decreasin order
# [70, 60, 50, 40, 30, 20, 10]

# L1=["coat","python","block","cat"]
# L1.sort()
# print(L1)

# # ['block', 'cat', 'coat', 'python']

# # Sorted order

# L1.sort(key=len)
# print(L1)
# # ['cat', 'coat', 'block', 'python']



# L1=["apple","Bat","cat","Dog"]
# L1.sort()
# print(L1)
# #['Bat', 'Dog', 'apple', 'cat']


# L1.sort(key=str.lower)
# print(L1)
# # ['apple', 'Bat', 'cat', 'Dog']



