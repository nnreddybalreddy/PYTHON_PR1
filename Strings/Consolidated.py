# # my_str='Hello'
# # my_str1="Hello2"
# # my_str2="""
# # Hello1
# # Hello2
# # Hello3
# # """

# # print(my_str)
# # print(my_str1)
# # print(my_str2)

# #Accessing string
# # my_str="Python"
# # print(my_str[0])
# #  # p 

# # print(my_str[-1])
# #   # n
# # print(my_str[:3])
# #  #Pyt
# # print(my_str[:5])
# #  #Pytho

# #delete string or change string 
# my_str="Hello"
# del my_str 

# my_str="Hello1"

# print(len(my_str))
#  #6 

# my_str="Hello"
# my_str1="World"

# print(my_str+my_str1)

# print(my_str+" "+my_str1)


# my_str="python Programming Language"

# print(my_str.capitalize())
#  # Python programming language

# print(my_str.lower())
#  #python programming language

# print(my_str.upper())
# #PYTHON PROGRAMMING LANGUAGE

# print(my_str.swapcase())
#  # PYTHON pROGRAMMING lANGUAGE

# print(my_str.title())
#  # Python Programming Language

# my_str="Python1"

# print(my_str.isalnum())
#   #True 
# print(my_str.isalpha())
#  #False

# print(my_str.islower())
#  #False

# print(my_str.isupper())
#  #False

# print(my_str.startswith("Py"))
#  #True 

# print(my_str.endswith("n"))
#  #False

# print(my_str.istitle())
#  # True



# my_str="Python"

# print("_".join(my_str))
# # P_y_t_h_o_n

# print(my_str.center(10))
#   #  Python
# print(my_str.ljust(10))
# #Python
# print(my_str.rjust(10))
# #    Python

# print(my_str.zfill(10))
# # 0000Python



# my_str="   Python    "
# print(my_str.strip())

# x="pythonyyyy"

# print(x.lstrip('p').rstrip('y'))
#  #ython

# x="Python is easy"
# print(x.split())
#  # ["Python", "is", "easy"]


# my_str="Python"

# print(my_str.count('p'))
# # 0

# print(my_str.count("P"))
# # 1
# my_str="Python is very easy is a is"
# print(my_str.count("easy"))
#  # 1

# print(my_str.index("easy"))
# # 15
# print(my_str.index("is",2))
# # 7
# print(my_str.index("is",17))
# #20
# # print(my_str.index("is",28))
# #  # ValueError
# print(my_str.find("is",28)) 
#  # -1
# java_version="java_version 1.6"
# print(java_version.find("java"))
# # 0

import os 
my_string="python programming"

size=os.get_terminal_size().columns


print(my_string.center(size).title())
print(my_string.rjust(size))
print(my_string.ljust(size))




















