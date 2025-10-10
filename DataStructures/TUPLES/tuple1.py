# tpl1=()
# tpl2=(2,4,6)

# print(tpl1,bool(tpl1))  # () False
# print(tpl2,bool(tpl2))   # (2, 4, 6) True


# tpl1=(2,3,[4,5,6],7,8)
# print(tpl1[2])     # [4, 5, 6]
# print(tpl1[2][2])      # 6


##################################################

# tpl1=(2,3,4,5)
# tpl1[1]=50

# print(tpl1) # TypeError: 'tuple' object does not support item assignment

# tpl1=(2,3,[4,5,6],7,8)
# tpl1[2][2]=22
# print(tpl1)
# #   (2, 3, [4, 5, 22], 7, 8)

# # tuples and strings are immutable. so less operations

# print(dir(tpl1))   #index,count 

#######################################################


tpl1=(2,4,6,8,10,"Python",8)
# print(tpl1.count(5))  # 0
# print(tpl1.count(8))  # 2

# print(tpl1.index(10))  # 0

# print(tpl1.index(2,3)) #ValueError: tuple.index(x): x not in tuple
print(tpl1.index(8,4))  #6

#########################################


# x=[4,5,6,7,8]

# print(len(x)) #5

# ##########################

# x="hi"
# print(len(x))  #2

# x=[2,3,6]
# print(len(x)) #3

# #string,list,tuple the len function is same

# #########################################################

# # index based

# tpl1=(2,3,5,6,7,8)
# print(tpl1[:]) # (2, 3, 5, 6, 7, 8)
# print(tpl1[0:]) # (2, 3, 5, 6, 7, 8)
# print(tpl1[3:]) #(6, 7, 8)

# #####################################################################

# print(tpl1[3:5]) # 6,7



# x=5,
# print(type(x)) #<class 'tuple'>

# x=5,8,9
# print(type(x)) #<class 'tuple'>

# Data changing take list, data changing not required --> tuple









