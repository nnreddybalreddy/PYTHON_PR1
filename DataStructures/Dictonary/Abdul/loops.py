d1={4:"four",5:"five",6:"six",7:"seven"}

for i in d1:
    print(i,d1[i])

# 4 four
# 5 five
# 6 six
# 7 seven

# Methods:
# -------------

for i in d1.keys():
    print(i,end=" ")
#4,5,6,7

for i in d1.values():
    print(i,end=" ")
# four five six seven

for i in d1.items():
    print(i,end=" ")    
# (4, 'four') (5, 'five') (6, 'six') (7, 'seven')         


for x,y in d1.items():
    print(x,y)

# $ python travers.py
# 4 four
# 5 five
# 6 six
# 7 seven



print(d1.get(4))
#four 
print(d1[4])
#four

# print(d1.get(16))
# #None 
# print(d1[16]) # out scope value
# # KeyError: 16

# print(d1.get(5,"missing"))
# #5 

# print(d1.get(16,"missing"))
# #missing


#setdefault 
print(d1.setdefault(5)) #key already there
#five

print(d1.setdefault(16)) #key not there
#None
print(d1)
#{4: 'four', 5: 'five', 6: 'six', 7: 'seven', 16: None}

print(d1.setdefault(17,"Undefined")) 
#Undefined
#  
print(d1)  

#{4: 'four', 5: 'five', 6: 'six', 7: 'seven', 16: None, 17: 'Undefined'}
