a=int(input("Enter the number1:"))
b=int(input("Enter the number 2:"))
lst=[10,20,30]
try:
    div=a/b
    print('The division is :',div)
    print("List 3rd index:",lst[2])
    print(n)
except NameError:
    print("Name error handled") # print(n) . Undefined n is handled here
    
except ZeroDivisionError:
    print("Zero division error handled") #8/0 . Zero division error handled 

except IndexError:
    print("Index error  handled") #lst[3] . Index error handled 
    
except Exception as e:
    print("Exception occured",e.__class__) #Base class all exceptions 
	