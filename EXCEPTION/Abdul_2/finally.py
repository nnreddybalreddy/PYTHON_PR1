# print("before try")

# try:
#     a=int(input("Enter a"))
#     b=int(input("Enter b"))
#     c=a//b
# except Exception  as e:
#     print(e)
# else:
#     print("Division by zero")
# finally:
#     print("ALways prints")       


### Prog 2

def fun():
    try:
        x=int("abc")
    except Exception as e:
        print(e)
    else:
        return x
    finally:
        print("ALways print")  

res=fun()
print(res)


# $ python finally.py
# invalid literal for int() with base 10: 'Abc'
# ALways print
# None


######## Prog 3

def div(a,b):
    try:
        c=a//b
        return c
    except Exception as e:
        print(e)
    finally:
        print("Finally Block")
z=div(3,0)
print(z)   


# $ python finally.py
# invalid literal for int() with base 10: 'abc'
# ALways print
# None
#  division by zero
# Finally Block
# None


    
    
