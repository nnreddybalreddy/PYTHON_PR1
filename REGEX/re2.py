import re
# text="This is a python and it is easy to learn"
# my_pat="is"

# print(re.findall(my_pat,text)) # ['is', 'is', 'is']
# # "is" as  string
# print(len(re.findall(my_pat,text))) # 3

# ############## 2
# #my_pat="i[ts]"
# my_pat="x"
# text="This is a python and it is easy to learn"

# print(re.findall(my_pat,text))

# # ['is', 'is', 'it', 'is'] --> my_pat="i[st]""
# # [] --> my_pat="x"

################ 3
# my_pat="a"
# text="This is a python and it is easy to learn"

# print(re.findall(my_pat,text))
# # ['a', 'a', 'a', 'a']

# my_pat="[is]"
# text="This is a python and it is easy to learn"

# print(re.findall(my_pat,text))
# #['i', 's', 'i', 's', 'i', 'i', 's', 's']

# my_pat="[a-f]" #either a,b,c,d,e,f
# print(re.findall(my_pat,text))
# #['a', 'a', 'd', 'e', 'a', 'e', 'a']

########################33 4

# my_pat="\w"
# text="This is a python and it is easy to learn_"
# print(re.findall(my_pat,text))
# # ['T', 'h', 'i', 's', 'i', 's', 'a', 'p', 'y',
# # 't', 'h', 'o', 'n', 'a', 'n', 'd', 'i', 
# #'t', 'i', 's', 'e', 'a', 's', 'y', 't',
# # 'o', 'l', 'e', 'a', 'r', 'n', '_']

################################# 5

# my_pat="\w\w"
# text="This is a python and it is easy to learn_"
# print(re.findall(my_pat,text))
# #['Th', 'is', 'is', 'py', 'th', 'on', 'an', 'it', 'is', 'ea', 'sy', 'to', 'le', 'ar', 'n_']
# 2 characters
################################# 6

# my_pat="\w\w\w"
# text="This    is a python and it is easy to learn_&"
# print(re.findall(my_pat,text))

# # ['Thi', 'pyt', 'hon', 'and', 'eas', 'lea', 'rn_'] -3 characters

###########################3 7

# my_pat="\W"
# text="This    is a python and it is easy to learn_&####"
# print(re.findall(my_pat,text))

# # [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '&', '#', '#', '#', '#']
# # Disclude the \w (small w)


########################### 8

# my_pat="python\d"
# text="This is a python2 and it is easy to learn python3"
# print(re.findall(my_pat,text))

# #['python2', 'python3']


########################### 9
# my_pat="\d\d"
# text="This is a python2 45 and it is easy to learn python3"
# print(re.findall(my_pat,text))

# # ['45']













