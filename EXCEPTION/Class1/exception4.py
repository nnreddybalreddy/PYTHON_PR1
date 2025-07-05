# print(a) # NameError: name 'a' is not defined
# print(4+"string") #TypeError: unsupported operand type(s) for +: 'int' and 'str'
# open("1.txt") #FileNotFoundError: [Errno 2] No such file or directory: '1.txt'
# 4/0  $ ZeroDivisionError: division by zero


try:
    #print(a)
    # print(4+"hi") 
    # open("1.txt","r")
    # a=eval(input("Enter the number a:"))
    # b=eval(input("Enter the number b:"))
    # a/b
    # import fabric 
    11
    import math
except NameError:
    print("variable is not defined \n")    
except TypeError:
    print("Adding number and string is not possible \n")
except FileNotFoundError:
    print("File not found error \n")
except ZeroDivisionError:
    print("Division with zero not possible")
except ModuleNotFoundError:
    print("Module not imported")
except Exception as e:
    print(e.__class__)    

else:
    print("No exception")
finally:
    print("its always executed")        


