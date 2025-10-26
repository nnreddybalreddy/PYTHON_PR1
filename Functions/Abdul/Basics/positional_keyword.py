#Positional Parameters
# def volume(length,breadth,height):
#     print(length,breadth,height)
#     vol=length*breadth*height
#     return vol 

# v=volume(10,5,3)
# print(v)
# # #Result:
# #     #10,5,3
# #     # 150
# # #Result
# #     #5,10,3
# #     #150



# # # #Keyword Parameters
# def volume(length,breadth,height):
#     print(f'length is : {length}')
#     print(f'breadth is : {breadth}')
#     print(f'height is {height}')
#     vol=length*breadth*height
#     return vol 

# v=volume(length=10,breadth=5,height=3)
# print(v)
#     #length is : 10
#     #breadth is : 5
#     #height is 3
#     #150
# #     # Pass in any order



# #v=volume(breadth=10,height=3,length=5)
# #print(v)
#     # height is : 3
#     # breadth is : 10
#     # height is 3
#     # Pass in any order


# #Case 3
# v=volume(10,5,height=3)
# print(v)
#     #length is : 10
#     #breadth is : 5
#     #height is 3
#     #150

#Case 4
# #v=volume(5,length=10,height=3)
# #print(v)   
#     #  TypeError: volume() got multiple values for argument 'length'
#     # 5 goes in length
#     # Mixed arguments
#     # Either positional or keyword , both not both

# Case 5
# v=volume(length=10,5,3)
# print(v)     
# # # #SyntaxError: positional argument follows keyword argument
# # #posional left , keyword should be right

# v=volume(10,5,height=3)
# print(v)   
#     #height is : 3
#     #breadth is : 5
#     #height is 3

##############

#def volume(l,b,h)


#a.  v=volume(10,b=5,h=3) --Right
#b   v=volume(10,b=5,3)   -- Keyword should be right hand side
#c   v=volume(l=10,5,k=3)  --> "k" must be "h" and keyword should be right
#d   v=volume(10,5,,b=3)  ---> Wrong. positional on Rigt
                              # multiple times of h