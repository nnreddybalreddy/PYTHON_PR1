import re 
# text="This is about python and python is very easy and we having python vers and Python3 vers"
# pat=r"python[23]?"

# print(re.split(pat,text))
#print(re.split(pat,text)) --> # ['This is about ', ' and ', ' is very easy and we having ', 'w vers and ', ' vers']


# text="This is about python and python is very easy and we having pythonw vers and Python3 vers"
# pat=r"python[23]?"

################ 2
print(re.sub(pat,"Jython",text,flags=re.I))
print(re.sub(pat,"Jython",text,count=1,flags=re.I))

# Case 1: 
print(re.sub(pat,"Jython",text,flags=re.I))
original "This is about python and python is very easy and we having pythonw vers and Python3 vers"
sub:  This is about Jython and Jython is very easy and we having Jythonw vers and Jython vers


print(re.sub(pat,"Jython",text,count=1,flags=re.I))
#original: text="This is about python and python is very easy and we having pythonw vers and Python3 vers"
#sub: count=1 (only one time)
#This is about Jython and python is very easy and we having pythonw vers and Python3 vers


############ 3 
# subn


text="This is about python and python is very easy and we having pythonw vers and Python3 vers"
pat=r"python[23]?"

print(re.subn(pat,"jython",text,count=2,flags=re.I))
# ('This is about jython and jython is very easy and we having pythonw vers and Python3 vers', 2)

print(re.subn(pat,"jython",text,flags=re.I))
# ('This is about jython and jython is very easy and we having jythonw vers and jython vers', 4)
