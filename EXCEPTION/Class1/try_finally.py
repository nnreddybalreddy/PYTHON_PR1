try:
    a=10
    print(a)
except NameError:
    print("variables is not defined")
except Exception as e:
    print("Exception occured",e)
else:
    print("This will excute if there is no exception")
finally:
    print("This will execute always")
                    