import re 
# text="python and python2 and python3 and python4"
# pat=r"\bpython[23]?\b"

# print(re.match(pat,text))
# #text="This python and python2 and python3 and python4" --None
# # text="python and python2 and python3 and python4" --> <re.Match object; span=(0, 6), match='python'>

################# 2

# text="This is python and python2 and python3 and python4"
# pat=r"\bpython[23]?\b"

# print(re.findall(pat,text))
#['python', 'python2', 'python3'] --> 3

########################## 3 


# text="This is python and python2 and python3 and python4"
# pat=r"\bpython[23]?\b"

# # print(re.finditer(pat,text))
# #<callable_iterator object at 0x000001E2967B3BA8>

######################### 4

for each_obj in re.finditer(pat,text):
    print(each_obj.start(),each_obj.end(),each_obj.group())

# pat=r"\bpyxthon[23]?\b"    --> No print
# pat=r"\bpython[23]?\b"
    # <re.Match object; span=(8, 14), match='python'>
    #<re.Match object; span=(19, 26), match='python2'>
    #<re.Match object; span=(31, 38), match='python3'>
#     print(each_obj.start(),each_obj.end(),each_obj.group())
#  8 14 python
# 19 26 python2
# 31 38 python3  






    