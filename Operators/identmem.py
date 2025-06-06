# x=4
# y=5


# print(type(x) is type(y)) #True
# print(type(x) is int) #True 

# x=4
# y="Hi"

# print(type(x) is not type(y)) #True 

valid_java=["1.5","1.6","1.7","1.8"]
host_java="1.6"

if (host_java in valid_java):
    print("Valid Java Version") # Valid Java Version
else:
    print("Invalid Java Version")    



db_user=["admin","root","user","guest"]
random_user="root1"

print(random_user not in db_user) # True

if (random_user not in db_user):
    print("User not found") #user not found
else:
    print("User found")    


