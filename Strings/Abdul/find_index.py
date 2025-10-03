# find (sub,start,end)
s1="Hello how are you"
# print(s1.find('o'))
# #4 
# print(s1.find("how"))
# #6
# print(s1.find('k'))
# # -1 

# print(s1.find('o',5))
# #7
# print(s1.find('o,5,7'))
# #-1
# print(s1.find("how",0,5))
# # -1 

# print(s1.find("how",0,9))
# #6

# rfind
# rfind(sub,start,end)
# print(s1.rfind('o'))
# #15 

# print(s1.rfind('o',0,15))
# #7

# print(s1.rfind('kite'))
# #-1






#index(sub,start,end)
print(s1.index('o'))
#4 
print(s1.index("how"))
#6 

# print(s1.index('k'))
# #ValueError: substring not found



# #rindex(sub,start,end)
print(s1.rindex('o'))
#15
print(s1.rindex('o',0,15))
#7


# count(sub,start,end)
print(s1.count('o'))
#3 

print(s1.count("me"))
#0 

