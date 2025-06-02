########## Multiple elements access in list ###########################
# x=5
# lst1=[6,7,'8.9','Python','Prgramming',3.6]

# print(lst1)  # [6, 7, '8.9', 'Python', 'Prgramming', 3.6]

################### BOOL of empty and filled list #########################################


# my_list=[]
# my_list1=[3,2,4,"python",5.6]

# print(bool(my_list))  # False 
# print(bool(my_list1)) # True 

###################Accessing elements##########################################################

#“hello”- 0 1 2 3  4
# -5 -4 -3 -2 -1

# my_list=[3,2.4,"python",5.6]

# print(my_list[0]) #3  
# print(my_list[1]) #2.4
# print(my_list[-1]) #4
# print(type(my_list)) # <class 'list'>


# my_list=[3,2,4,"python",5]   

# print(my_list[2],my_list[-3])  # 4  4

# print(my_list[3][1])  # y

#############################



# my_list=[3,2.4,"python",5.6]

# print(my_list)        #[3, 2.4, 'python', 5.6]
# print(my_list[:])      # [3, 2.4, 'python', 5.6]
# print(my_list[0:])     # [3, 2.4, 'python', 5.6]


# print(my_list[1:4])  # [2.4, 'python', 5.6]
# print(my_list[:4])    # [3, 2.4, 'python', 5.6]

#####################
# Lists are mutable where as strings are immutable 

# my_list=[3,2.4,"python",5.6]
# my_list[1]=45
# print(my_list)  # [3, 45, 'python', 5.6]



# my_list=[3,4,5,7,8,5,9,10]

# print(dir(my_list))

# 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']

#############################  index ############################

# my_list=[3,4,5,7,8,5,9,10]

# #Index 
# print(my_list.index(5))  #2
# print(my_list.index(5,3))  #5
# # print(my_list.index(11))  #ValueError: 11 is not in list

# #count
# print(my_list.count(5))  #2
# print(my_list.count(11)) # 0

# my_count_5=my_list.count(5)
# print(my_list)        #[3, 4, 5, 7, 8, 5, 9, 10]

###################################################################################

# my_list.clear()
# print(my_list) # []

# print(my_list.clear())  # None . Can't take output because list modifying by clear. Opeartion cannot take print.

#################################################

# copy 

# my_list=[3,4,5,6,7,8]
# my_new_list=my_list 

# print(id(my_list),id(my_new_list))  # 1978200318536 1978200318536. BOth are same

# my_cpy_list=my_list.copy()
# print(id(my_list),id(my_cpy_list))   # 1978200318536 1978200318600. Copy the list to diff address


###########################################################################

#append,insert,extend modifying data

# my_list=[3,4,5,6,7,8]
# print(my_list)     # [3, 4, 5, 6, 7, 8]


# my_list.append(56)
# print(my_list)        # [3, 4, 5, 6, 7, 8, 56]


# my_list.insert(1,99)
# print(my_list)       # [3, 99, 4, 5, 6, 7, 8, 56]


#Extend

# my_list=[3,4,5,6,7,8]
# my_new_list=[9,10]


# my_list.append(my_new_list)
# print(my_list)  # [3, 4, 5, 6, 7, 8, [9, 10]] # List

# my_list=[3,4,5,6,7,8]
# my_list.extend(my_new_list)
# print(my_list)  # [3, 4, 5, 6, 7, 8, 9, 10]  #list as a normal data

##############################################

#pop/remove 

# my_list=[3,4,5,6,7,8,9]

# my_list.remove(8)
# print(my_list) # [3, 4, 5, 6, 7, 9]


# my_list.remove(11) # ValueError: list.remove(x): x not in list

#######################################################################################


# my_list=[3,4,5,6,7,8,9]
# my_list.pop()
# print(my_list)  #[3, 4, 5, 6, 7, 8]

############################################################################################

# print(my_list.pop(6))

# print(my_list) # IndexError: pop index out of range

##############################################################

# my_list=[3,4,5,6,7,8,9]
# print(my_list.pop(4))  # 7 index

# print(my_list)  # [3, 4, 5, 6, 8, 9]

#####################################################################

# Reverse / Sort 

# my_list=[3,4,5,6,7,8,9]

# my_list.reverse()
# print(my_list)  # [9, 8, 7, 6, 5, 4, 3]


# my_list=[3,4,5,6,7,8,9]
# my_list.sort()
# print(my_list) #[3, 4, 5, 6, 7, 8, 9] # Ascneding

# my_list.reverse() #  Descending 
# print(my_list) #[9, 8, 7, 6, 5, 4, 3]

# my_list=[3,4,5,6,7,8,9]
# my_list.sort(reverse=True)
# print(my_list) #[9, 8, 7, 6, 5, 4, 3] ---> Ascending at a time


















































