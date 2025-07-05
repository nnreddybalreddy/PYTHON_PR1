# age=23

# if age>30:
#     print("valid age::")
# else:
#     raise ValueError("Age is less than 30 ")   

# assert 3>4

age=33

try:
    assert age<30
    print("Valid age")
except AssertionError:
    print("Raised with assert because age is less than 30")    
except:
    print("Exception occured")    
