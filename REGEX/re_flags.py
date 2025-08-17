import re
# text="This is a string this is a new starting THIS"
# my_pat=r'this'

# #print(re.findall(my_pat,text)) # this 
# print(re.findall(my_pat,text,re.I)) # ['This', 'this', 'THIS']

############ 2

text="""this is a multiline END
This is also a find END
This also a end
this ia an end"""

# # case 1
my_pat=r"this"

print(re.findall(my_pat,text)) # ['this', 'this']

# #case 2
my_pat=r"^this" # start of the string 
print(re.findall(my_pat,text)) #['this']
print(re.findall(my_pat,text,re.M)) #['this', 'this']
print(re.findall(my_pat,text,re.M|re.I)) # ['this', 'This', 'This', 'this']
my_pat=r"end$"
print(re.findall(my_pat,text,re.M|re.I)) #['END', 'END', 'end', 'end']