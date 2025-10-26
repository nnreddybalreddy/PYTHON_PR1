def Outer():
    def Inner():
        print("Hello from the Inner function!")
    
    return Inner

f=Outer()
f()
# Hello from the Inner function!
