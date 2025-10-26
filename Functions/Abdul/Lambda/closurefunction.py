# Nested Function
# Return Function
# Inner Function access to outer variables

msg="welcome"
def inner():
    print("+" * 10)
    print(msg)
    print("+" * 10)

inner()

# ++++++++++
# welcome
# ++++++++++




###########################3
def Outer():
    msg="welcome"
    def inner():
        print("+" * 10)
        print(msg)
        print("+" * 10)
    return inner

f=Outer()
f()

# ++++++++++
# welcome
# ++++++++++

##################################

def Outer():
    # msg="welcome"
    def inner():
        print("+" * 10)
        print(msg)
        print("+" * 10)
    return inner

f=Outer("Welcome")
f()
# ++++++++++
# welcome   
# ++++++++++

#############################################


count=0
def Counter():
    global count
    count +=1
    return count


print(Counter())
#1
print(Counter())
#2
print(Counter())
#3

#################################


def get_counter():
    count=0    
    def Counter():
        nonlocal count
        count +=1
        return count
    return Counter

c1=get_counter()
c2=get_counter()

print(c1(),c1(),c1())
# 1 2 3
print(c2(),c2(),c2())
# 1 2 3
    
