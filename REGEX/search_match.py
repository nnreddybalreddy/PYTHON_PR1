import re 
# text="This is for python and there are two major vers python2 and python3 in future python4"

# my_pat=r"\bpython[23]?\b"
# # print(re.findall(my_pat,text))
# # ['python', 'python2', 'python3']

# text="This is for python2 and there are two major vers python2 and python3 in future python4"
# match_obj=re.search(my_pat,text)
# #print(match_obj)
# # <re.Match object; span=(12, 19), match='python2'>
# if match_obj:
#     print(match_obj.group()) # python2  
#     print(match_obj.start()) #12
#     print(match_obj.end()-1) #18
#     print("length:",match_obj.end()-match_obj.start()) # 7
# else:
#     print("No match found")    

#python2
#12
#18
#length: 7

############## 2
# text="""This is for
# python2 and there are two major vers
# python2 and
# python3 in future python4"""

# my_pat=r"\bpython[23]?\b"
# match_obj=re.search(my_pat,text)
# #print(match_obj)
# # <re.Match object; span=(12, 19), match='python2'>
# if match_obj:
#     print(match_obj.group()) # python2  
#     print(match_obj.start()) #12
#     print(match_obj.end()-1) #18
#     print("length:",match_obj.end()-match_obj.start()) # 7
# else:
#     print("No match found") 

# Match line
# starting index 

#python2
#12
#18
#length: 7

#################### 3

# text="""This is for
# python2 and there are two major vers
# python2 and
# python3 in future python4"""

# pat=r"\bpython[23]?\b"
# print(re.match(pat,text)) #only first line  --> None 

######################### 4
text="""python2 is for
python2 and there are two major vers
python2 and
python3 in future python4"""
pat=r"\bpython[23]?\b"
match_obj=re.match(pat,text)
#print(match_obj)
# <re.Match object; span=(12, 19), match='python2'>
if match_obj:
    print(match_obj.group()) # python2  
    print(match_obj.start()) #12
    print(match_obj.end()-1) #18
    print("length:",match_obj.end()-match_obj.start()) # 7
else:
    print("No match found") 
#python2
#0
#6
#length: 7
    




