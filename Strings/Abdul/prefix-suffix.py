# #startswith 

# s1="python is very easy"
# print(s1.startswith("python"))
# #True

# print(s1.startswith("is"))
# #False 

# print(s1.startswith("is",7))
# #True 


# print(s1.endswith("easy"))
# #True 

# s1="abc@gmail.com"

# print(s1.endswith(".com"))
# #True 

########### 2

s1="python is easy"
s2=s1.partition("is")
print(s2)
#('python ', 'is', ' easy')
print(type(s2))
#('python ', 'is', ' easy')
# <class 'tuple'>


############# 3

s1="python is easy"
print(s1.partition("s"))
#('python i', 's', ' easy')




