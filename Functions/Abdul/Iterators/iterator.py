# L1=[5,6,10,11,15]

# for i in L1:
#     print(i,end=" ")
#     # 5 6 10 11 15

############ Iterators

# L1=[5,6,10,11,15]
# it=iter(L1)
# print(it)
# #<list_iterator object at 0x000001F90C4C2358>

# print(next(it))
# #5
# print(next(it))
# #6
# print(next(it))
# #10
# print(next(it))
# #11
# print(next(it))
# #15
# print(next(it))
# #StopIteration

# #####################################
# L1=[5,6,10,11,15]
# for i in range(len(L1)+1):
#     print(next(it),end=" ")
#     # 5 6 10 11 15
#     # StopIteration

# #iter(iterable) ---> gives an iterator on iterable

# #######################################################
# # Tuples
# T1=(5,6,7)

# it=iter(T1)

# for i in range(len(T1)):
#     print(next(it),end=" ")
#     #5 6 7



# # SETS
# S1={5,6,7}
# it=iter(S1)

# for i in range(len(S1)):
#     print(next(S1),end=" ")
# #   TypeError: 'set' object is not an iterator



# # Dictonary
# d1={1:"one",2:"two",3:"three"}
# it=iter(d1)


# for i in range(len(d1)):
#     print(next(it),end=" ")
#     # 1 2 3



# #Strings
# s1="NNR"

# it=iter(s1)

# for i in range(len(s1)):
#     print(next(it),end=" ")
#     #N N R


# ##### range

# r=range(3,6)

# it=iter(r)

# for i in range(len(r)):
#     print(next(it),end=" ")
#     #3 4 5


# #next(iterator) gives an element and moves next

# #################### GENERATORS
# # r=range(4) #0 1 2 3
# # it=iter(r)
# # print(it)
# # <range_iterator object at 0x0000029199F5C610>

# # range is example of generators
# # iterator is builtin
# # range is generators

# # n=4
# # def myrange(n):
# #     i=0
# #     while i<n:
# #         yield i
# #         i=i+1

# # m=myrange(n)

# # for i in range(n):
# #     print(next(m),end=" ")
# #     # 0 1 2 3

# # print(next(m))    
# # #StopIteration

# #######################################





def mylist(d):
    i=0
    while True:
        yield d[i]
        i=(i+1)%7

d=["Sun","Mon","Tue","Wed","Thu","Fri","Sat"]
m=mylist(d)

for i in range(len(d)+5):
    print(next(m),end=" ")




