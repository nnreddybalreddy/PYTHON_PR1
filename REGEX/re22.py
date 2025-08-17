import re 
########## 1
# my_pat="is"
# text="This is a python and it is easy to learn"

# print(re.findall(my_pat,text)) 
#         ['is', 'is', 'is']



############## 2

my_pat="i[st]"
text="This is a python and it is easy to learn"
print(re.findall(my_pat,text)) 
# ['is', 'is', 'it', 'is']

# # ###############  3
# # a x  9 
# my_pat="a"
# text="This is a python and it is easy to learn"
# print(re.findall(my_pat,text)) 

# # single character:::::: ['a', 'a', 'a', 'a']


# # ###################### 4
# # [abc] --> a or b or c
# my_pat="[$%^&]"
# text="This is a python and $%^& it is easy to learn$%^&"
# print(re.findall(my_pat,text)) 
# #['$', '%', '^', '&', '$', '%', '^', '&']

########################### 5
# ## # [a-f] --> a or b or c
# my_pat="[a-f]"
# text="This is a python and $%^& it is easy to learn$%^&"
# print(re.findall(my_pat,text)) 
# # ['a', 'a', 'd', 'e', 'a', 'e', 'a']

##################### 6
# ## # [a-f] --> a or b or c
# # [a-zA-Z0-9]
# my_pat="[a-fA-Z0-9]"
# text="This is a python and $%^& 0 2 3 4 5 it is easy to learn$%^&"
# print(re.findall(my_pat,text)) 
# # ['T', 'a', 'a', 'd', '0', '2', '3', '4', '5', 'e', 'a', 'e', 'a']


############################ 7
# # # \w --> Any a-z,A-Z,0-9 _ except space
# my_pat="\w"
# text="This is a python and it is easy to learn"
# print(re.findall(my_pat,text)) 
# # #['T', 'h', 'i', 's', 'i', 's', 'a', 'p', 'y', 't', 'h', 'o', 'n', 'a', 'n', 'd', 'i', 't', 'i', 's', 'e', 'a', 's', 'y', 't', 'o', 'l', 'e', 'a', 'r', 'n']

# #### two \w\w
# my_pat="\w\w"
# text="This is a python and it is easy to learn"
# print(re.findall(my_pat,text)) 
# ['Th', 'is', 'is', 'py', 'th', 'on', 'an', 'it', 'is', 'ea', 'sy', 'to', 'le', 'ar']

############ \w\w\w 

# my_pat="\w\w\w"
# text="This is a python and it is easy to learn _ara $$$$$$$"
# print(re.findall(my_pat,text)) 
# # ['Thi', 'pyt', 'hon', 'and', 'eas', 'lea', '_ar']


# ######################## 8

# #\W -- Matches any characters not part of \w

# my_pat="\W"
# text="This is a python #$%^& *&^%"
# print(re.findall(my_pat,text)) 
# # \w  ---> ['T', 'h', 'i', 's', 'i', 's', 'a', 'p', 'y', 't', 'h', 'o', 'n']
# # \W ---> [' ', ' ', ' ', ' ', '#', '$', '%', '^', '&', ' ', '*', '&', '^', '%']

################################### 9
# # \d --Only numbers
# # my_pat="python\d"
# my_pat="\d\d"
# text="This is a python1 python2 123456"
# print(re.findall(my_pat,text)) 
# # "\d" --> ['1', '2', '3', '4', '5', '6', '7', '8']
# # "python\d" ---> ['python1', 'python2']
# # "\d\d"  --> ['12', '34', '56']


#################3 10
# . matches single character except new line 


# my_pat="\."
# text="This is a python1. python2."
# print(re.findall(my_pat,text)) 

# # . --> ['T', 'h', 'i', 's', ' ', 'i', 's', ' ', 'a', ' ', 'p', 'y', 't', 'h', 'o', 'n', '1']
# #  .. --> ['Th', 'is', ' i', 's ', 'a ', 'py', 'th', 'on']
# #  ...>  ['Thi', 's i', 's a', ' py', 'tho']
# # text="This is a python1. python2"
# # "\." --> ['.', '.']

##########################  11


# my_pat="\d\d\d\.\d\d\d\.\d\d\d\.\d\d\d"
# text="This is a python1. ip : 192.168.255.101 122 323 324 This is "
# print(re.findall(my_pat,text))
# # "\d\d\d\.\d\d\d\.\d\d\d\.\d\d\d" --> ['192.168.255.101']






