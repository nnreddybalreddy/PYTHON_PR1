# set1={4,5,7,2,7,0}
# print(bool(set1))  #True 
# print(set1)         # {0, 2, 4, 5, 7} -- Ascnexing order.Unique data. Dups will not allowed


# set1={4,5,5,8,3,2,4}
# print(set1)

# set1=set({})

# print(type(set1),bool(set1))  # <class 'set'>              False


# lst1=[4,8,7,1,10,12]

# print(set(lst1))  # {1, 4, 7, 8, 10, 12}

# print(dir(set1))
# # 'add', 'clear', 'copy', 'difference', 'difference_update', 'discard',
# # 'intersection', 'intersection_update', 'isdisjoint', 'issubset', 
# #'issuperset', 'pop', 'remove', 'symmetric_difference', 
# # 'symmetric_difference_update', 'union', 'update']

# A={1,2,3,5,6,7,2}
# B={3,4,5,6,7,2,5}

# print(A.difference(B))  # 1 
# print(A.union(B)) # {1, 2, 3, 4, 5, 6, 7}
# print(A.intersection(B)) #{2, 3, 5, 6, 7}


############################################################################################

#   a. Set Properities
#   b. Set Items Accessable
#   c. Add item
#   d. Remove item
#   e. Iterate set item
#   f. Operation on set items

# a. Set Properities


#   Arrays Vs Sets: Sets are unordered,Immutable (unchangle) and no duplicates.
#  Where as in Lists are indexble,changable,duplicates
# Ascneidng order, multiple datatypes in one set is allowed

    #    Set items are unordered,unchangable and no duplicates values.

    #      Unordered: Do not have defined orders
    #      set1={1,2,3} 
    #      print(set1) :
    #          {1,2,3} or {3,2,1}  etc

    #     Unchangable:
    #        set1[2]=6 . Not allowed. 
    #        We cannot change the items after set has been created.

    #    No Duplicates:
    #        {1,2,3,2} print(set1)-->{1,2,3}

# set1={3,2,4,5,6,1,1,2,3,4}
# print(set1)   # {1, 2, 3, 4, 5, 6} --> No dups. Ascending order

# set1[0]=3
# print(set1)  # TypeError: 'set' object does not support item assignment
# Immutable

# set1={1,2,3.6,"Python",bool}
# print(set1)         # {1, 2, 3.6, 'Python', <class 'bool'>}
# Any data type  allowed


# set4={4,2,"a","Python",True,3.5,False}
# print(len(set4))   # 7


#   b. Set Items Accessable

# set1={2,5,6,7,8,2,5,4,4,0,"Python","Abc"}

# for i in set1:
#     print(i,end=" ")

# c.
# print(dir(set1))
# # 'add', 'clear', 'copy', 'difference', 'difference_update', 'discard',
# # 'intersection', 'intersection_update', 'isdisjoint', 'issubset', 
# #'issuperset', 'pop', 'remove', 'symmetric_difference', 
# # 'symmetric_difference_update', 'union', 'update']


# set1={1,2,1,3,2,5,6,7,9}
# set1.add(10)
# print(set1)  #{1, 2, 3, 5, 6, 7, 9, 10}


# set1={1,2,1,3,2,5,6,7,9}
# set1.clear()
# print(set1)  # set()


# set1={1,2,1,3,2,5,6,7,9}
# set2=set1.copy()
# print(id(set1),id(set2))     #1944414084232 1944414134344



# set1={1,2,1,3,2,5,6,7,9}
# set2={1,2,1,4,5,5,6,7,9,10}

# set3=set1.difference(set2)
# print(set1) # {1, 2, 3, 5, 6, 7, 9}
# print(set2)  #{1, 2, 4, 5, 6, 7, 9, 10}
# print(set3)  # {3}
 

# set1.difference_update(set2)
# print(set1) # {3}
# print(set2) # {1, 2, 4, 5, 6, 7, 9, 10}


# set1={1,2,1,3,2,5,6,7,9}
# set2={1,2,1,4,5,5,6,7,9,10}

# set3=set1.intersection(set2)
# print(set1)  #{1, 2, 3, 5, 6, 7, 9}
# print(set2)  #{1, 2, 4, 5, 6, 7, 9, 10}
# print(set3)  # {1, 2, 5, 6, 7, 9}



# set2.intersection_update(set1)
# print(set2)  #{1, 2, 5, 6, 7, 9}
# print(set1)  # {1, 2, 3, 5, 6, 7, 9}

# # pop/remove/union/update 


# set1={1,2,1,3,2,5,6,7,9}
# set2={1,2,1,4,5,5,6,7,9,10}

# print(set1.pop())  #1
# set1.remove(9)
# print(set1)   # {2, 3, 5, 6, 7}

# set1={1,2,1,3,2,5,6,7,9,11}
# set2={1,2,1,4,5,5,6,7,9,10,12}

# set1.union(set2)

# print(set1) #{1, 2, 3, 5, 6, 7, 9, 11}
# print(set2) #{1, 2, 4, 5, 6, 7, 9, 10, 12}


# set1={1,2,1,3,2,5,6,7,9,11}
# set2={1,2,1,4,5,5,6,7,9,10,12}

# set1.update(set2) 
# #To add items from another set into current set by using update() method.

# print(set1)  # {1, 2, 3, 4, 5, 6, 7, 9, 10, 11, 12}
# print(set2)  # {1, 2, 4, 5, 6, 7, 9, 10, 12}













