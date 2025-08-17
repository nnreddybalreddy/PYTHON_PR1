#^ starting 

import re
# text="its is a python andlearn it is easy to learn "
# my_pat="^i[st]"


# print(re.findall(my_pat,text))
# #"i[st]"---> ['it', 'is', 'it', 'is']
# # "^i[st]" --> ['it']

############ 2
# # $ ---> End of the string ( and new line character in case multi string)
# text="its is a python andlearn it is easy to learn"
# my_pat="learn$"

# print(re.findall(my_pat,text))
# # ['learn']

################ 3

# \b --> Empty string at the begining or end of a word
# backspace
# text="its is a python andlearn it learnis easy to learn"
# # my_pat="\\blearn"
# # my_pat=r"\blearn"
# my_pat=r"\blearn\b"
# print(re.findall(my_pat,text))

# # case 1:
# text="its is a python andlearn it learn is easy to learn"
# my_pat=r"\blearn"
# print(re.findall(my_pat,text))
# # output:
# #      ['learn', 'learn']

# case 2:
# text="its is a python andlearn it learnis easy to learn"
# my_pat=r"\blearn\b"
#['learn']

# \B 
# text="its is a python andlearn it itlearnis easy to learn"
# my_pat=r"\Blearn\B"
# print(re.findall(my_pat,text))

#output:
# ['learn'] --> Withtou spaces "itlearnis"

# \t 
# \n 
my_pat=r"\n"
text='  Hello    Hello1  \n   Hello2'

print(re.findall(my_pat,text))
# ['\n']


   
