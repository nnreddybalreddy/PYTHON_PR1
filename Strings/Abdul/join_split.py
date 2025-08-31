# # replace(old,new,count)

# s1="a-b-c-d-e"
# s2=s1.replace("-",",")
# print(s2)
# #a,b,c,d,e
# print(s1.replace("-",",",3))
# #a,b,c,d-e

# print(s1.replace("k","m"))
# #a-b-c-d-e (No changes on string if no matching "m")

# s1="narendra.nya@gmail.com"
# print(s1.replace("gmail","yahoo"))
# #narendra.nya@yahoo.com


############## 2

# s1="xyz"
# s2="abc"

# print(s1.join(s2))
# #axyzbxyzc


# s1="/"
# s2="abc"

# print(s1.join(s2))
# #a/b/c

##############3 3

#split 

s1="John Smith Ajay"
s2=s1.split()

print(s2)
print(type(s2))
#['John', 'Smith', 'Ajay']
# <class 'list'>

s2=s1.split("h")
print(s2)
#['Jo', 'n Smit', ' Ajay']


s1="John-Smith-Ajay-Khan-James"

print(s1.split(" "))
# ['John-Smith-Ajay-Khan-James']

print(s1.split("-"))
# ['John', 'Smith', 'Ajay', 'Khan', 'James']

print(s1.split("-",3))
#['John', 'Smith', 'Ajay', 'Khan-James']





############## 4






