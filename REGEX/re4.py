import re
# text="This is a pythonn and python3"
# my_pat=r"python"


# print(re.findall(my_pat,text))
# # my_pat=r"python" --> ['python', 'python']

############ 2
# text="This is a pythonnnn and python3"
# my_pat=r"python{4}"


# print(re.findall(my_pat,text))
# # ['pythonnnn']

############# 3
text="xaz xaaz xaaaz xaaaaz xaaaaaz"
# my_pat=r"xa{2}"  # atleast 2 times
# my_pat=r"xa{3,5}" # 3 , 4 ,5
# my_pat=r"xa{2,}" # 2 or more
# my_pat=r"xa+"  # one or more 
# my_pat=r"xa*" # zero or more
my_pat=r"xa?z" # one or none
print(re.findall(my_pat,text))

# my_pat=r"xa{2}" -> ['xaa', 'xaa', 'xaa', 'xaa']
# my_pat=r"xa{3,5}"['xaaa', 'xaaaa', 'xaaaaa']
# my_pat=r"xa{2,}" --> ['xaa', 'xaaa', 'xaaaa', 'xaaaaa']

# my_pat=r"xa+" ---> ['xa', 'xaa', 'xaaa', 'xaaaa', 'xaaaaa']
# r"xa*" --> ['xa', 'xaa', 'xaaa', 'xaaaa', 'xaaaaa']
# my_pat=r"xa?z" --> ['xaz']