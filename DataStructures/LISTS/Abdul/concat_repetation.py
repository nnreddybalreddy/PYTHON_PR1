# # #concatation

# # L1=[1,2,3]
# # L2=[8,9,10]

# # print(L1+L2)
# # #[1, 2, 3, 8, 9, 10]

# # # print(L1+4)
# # # # TypeError: can only concatenate list (not "int") to list

# # print(L1+[4])
# # # [1, 2, 3, 4]

# L1=[1,2,3]
# L1.extend([4,5,6])
# print(L1)
# # [1, 2, 3, 4, 5, 6]



##### Repetation

# L1=[1,2,3]
# L2=L1*3
# print(L2)
# # [1, 2, 3, 1, 2, 3, 1, 2, 3]

# L2=L1*2.5
# #    L2=L1*2.5
# # TypeError: can't multiply sequence by non-int of type 'float'


################## Membership
#in , not in

# L1=[1,2,3,4,5]

# print(3 in L1)
# #True

# L1=[[1,2],[3,4],5]
# print(3 in L1)
# #False

# print([3,4] in L1)
# #True 

# L1=["Red","Green","Blue"]

# for x in L1:
#     print(x,end=" ")
# # Red,Green,Blue    

############# 

# List comparision

# L1=[1,2,3]
# L2=[1,2,3]
# L3=[3,2,1]

# print(L1==L2)
# #True 
# print(L1<L3)
# #True 

# L1=[1,2,3]
# L2=[1,2,3,4]
# L3=[1,2,1]

# print(L1<L2)
# #True 

# print(L1<L3)
# #False

# L1=[2]
# L3=[1,2,1]

# print(L1>L3)
# #True 

