####
# Prog 1:


a=10
b=0


try:
    c=a//b
    print(c)
except:
    print("B should not be 0")

print("End of program")

# Output 
#  B should not be 0
#  End of program


##### Prog 2
a=10
b-0

if b!=0:
    c=a//b
    print(c)
else:
    print("B should not be 0")
print("End of program")   


# Output:
# B should not be 0
# End of program

# Prog 3:

def div(a,b):
    if b!=0:
        c=a//b
        return c
    else:
        return -1

print(div(10,0))

print("End of program:::") 


# print(div(10,0))
# Output
# -1
# End of program:::


# print(div(10,5))
# output:
# 5

######## Prog 3:
def div(a,b):
    if b!=0:
        c=a//b
        return c
    else:
        return -1

print(div(10,0))

print("End of program:::")   

# Output:
#### -1
# End of program:::

### Output
# print(div(10,-10))
# -1
# End of program:::


# Prog 4: 
def div(a,b):
    if b!=0:
        c=a//b
        return c
    else:
        raise ZeroDivisionError

try:
    res=div(10,0)
    print(res)
except:
    print("Division by Zero2   ")

print("End of program:::") 

# Division by Zero2   
# End of program:::




