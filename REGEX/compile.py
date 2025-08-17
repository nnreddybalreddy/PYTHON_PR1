import re
pat=r"\bpython[23]?\b"

text="This is about python. Python is easy to learn andwe have two major versions: python2 and python3"

print(re.findall(pat,text,flags=re.I)) # ['python', 'Python', 'python2', 'python3']
print(re.search(pat,text,flags=re.I)) #<re.Match object; span=(14, 20), match='python'>
print(re.split(pat,text))
#['This is about ', '. Python is easy to learn andwe have two major versions: ', ' and ', '']

#################### 2
pat=r"\bpython[23]?\b"
pat_obj=re.compile(pat,flags=re.I)
print(pat_obj) # re.compile('\\bpython[23]?\\b', re.IGNORECASE)

text="This is about python. Python is easy to learn andwe have two major versions: python2 and python3"


print(pat_obj.findall(text)) #['python', 'Python', 'python2', 'python3']
print(pat_obj.search(text)) #<re.Match object; span=(14, 20), match='python'>
print(pat_obj.split(text)) #['This is about ', '. ', ' is easy to learn andwe have two major versions: ', ' and ', '']


#re.findall(my_pat,my_str) == re.compile(my_pat).findall(my_str)