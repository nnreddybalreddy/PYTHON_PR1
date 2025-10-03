# # my_str="  Python    "
# # print(my_str.strip())
# # # Python 

# # my_str="Python"

# # print(my_str.strip("n"))
# #  # only remove at end or starting
# #  # Pytho
# # print(my_str.strip("t")) 
# # # Python

# # my_str="Python is easy"

# # print(my_str.strip('easy'))
# #   #Python is

# # my_str="  Python  "
# # print(my_str.rstrip())
# # #    Python

# # print(my_str.lstrip())
# # #Python

# my_str="python1./i"
# my_str=my_str.strip('./i')
# print(my_str)
#  # python1

# x="pythonyyy"
# print(x.strip('p').rstrip('y'))
#  #ython


# x="Python is easy"
# print(x.split())

x="python is easy and it is very popular"
# print(x.split('is'))
# # ['python ', ' easy and it ', ' very popular'] -> List 

x=x.split(' ')
x1=[]

for i in x:
    if x.count(i)>1:
        print(i,x.count(i))
