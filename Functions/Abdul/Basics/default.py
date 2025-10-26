# # L1=[10,20,30,20,40,50,60,50,20]
# # print(L1.index(20))
# # #1

# # print(L1.index(20,2))
# # #3

# # print(L1.index(20,2,4))
# # #3

# # #pop(index)
# # #pop(len(l)-1)


# ######## Default arguments

# # def volume(l,b,h):
# #     v=l*b*h
# #     return v

# # v=volume(10,5,3)
# # print(v)
# # #150



# # def volume(l,b=1,h=1):
# #     v=l*b*h
# #     return v



# # v=volume(10,5)
# # print(v)
# # #50


# v=volume(10)
# print(v)
# # #10


# v=volume() #Error
# #TypeError: volume() missing 1 required positional argument: 'l'


# ############ Case 2

# def volume(l=1,b,h=1):
#     v=l*b*h
#     return v

# v=volume(10,5,3)
# #SyntaxError: non-default argument follows default argument


# ################## Case 3
# def volume(l=1,b=1,h=1):
#     v=l*b*h
#     return v

# v=volume()
# print(v)

# #1


# ##################### Case 4

# # def fun(a,b,c):
# #     print(a,b,c)

# # fun(5,10,15)
# # #5,10,15 

# ############### Case 5

# def fun(a=1,b=2.5,c="hello"):
#     print(a,b,c)
    


# fun(5,10,15) # 5,10,15
# fun()  # 1 2.5 hello

# ###########################

# def fun(a=1,b=2.5,c=[1,2,3]):
#     print(a,b,c)

# fun() #1 2.5 [1, 2, 3]
# fun(5,10,15) #5,10,15
# fun(5,10,[10,11]) #5 10 [10, 11]

# # Function takes any type of argument
# # Pass any type of arguments

# #########

# def func(l=[1,2,3]):
#     l.append(len(l)) #[1,2,3,3]
#     print(l)

# func() #[1,2,3,3]
# func() #[1,2,3,3,4]
# func([10,11])   #[10,11,2]                
# func() #[1,2,3,3,4,5]

# # default arguments are created only first time
