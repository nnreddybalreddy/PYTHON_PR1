# s1="Hello"
# print(s1.isalpha())
# #True

# s1="hello"
# print(s1.islower())
# #True 

# s1="Hello"
# print(s1.isupper())
# #False 

# s1="Hello how are you"
# print(s1.istitle())
# #False 

########## 

s=" "
print(s.isspace())
#True 

s=""
print(s.isspace())
#False
s=""
print(len(s)) 
# 0
################# 
s="\n\r\r\f"

print(s.isspace())
#True --> Whitespaces

###### printable 
s="\n"
print(s.isprintable())
#False--> Escape seq
# \n\r\f\b\a esc'

# isidentifier
s1="1abc"
print(s1.isidentifier())
#False

s2="abc1"
print(s2.isidentifier())
#Valid variable name






