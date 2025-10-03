my_str="Hello"
print(my_str.isalnum()) 
 # True
print(my_str.isalpha())
 # True

print(my_str.islower())
  # False

my_str="HELLO"
print(my_str.isupper())
 # True

print(my_str.startswith("P"))
    # False 

print(my_str.startswith("HEL"))
    # True

print(my_str.endswith("LLO"))
  # True 
my_str="Hello How are you"
print(my_str.istitle())     
    # False

print(my_str.isspace())
 # False 

my_str=" "
print(my_str.isspace())
 # True 

my_str="Hello "
print(my_str.isalpha())
  # False 

print(my_str.isnumeric())
 # False

my_str="123456"
print(my_str.isnumeric())
    # True


my_str="Python"

print(my_str.istitle()) #True

