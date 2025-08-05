a=int(input("Enter the number 1:"))
b=int(input("Enter the number 2:"))
lst=[2,4,6]
n=100
try:
    div=a/b
    print("Div:",div)
    print("lst 3rd Index:",lst[2])
    print(n)
    
except ZeroDivisionError:
    print("Zero division error occured") #  8/0. Zero division error occured

except IndexError:
    print("Index error occured")
    
except NameError:
    print("Name error occured")
    
except Exception as e:
    print("Exception occured:",e.__class__)
else:
    print("No exception occured") # No exception occured
    
finally:
    print("This is always executed ")  # This is always executed . for exception also this is will executed mage: 