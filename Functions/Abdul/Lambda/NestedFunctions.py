def Outer():
    def Inner():
        print("Hello from the Inner function!")
    
    print("Outer")
    Inner()

Outer()
# Inner()
# # NameError: name 'Inner' is not defined

# Result:
# Outer
# Hello from the Inner function!

####################
# Cubiod=2*((l*b)+(b*h)+(h*l))


def totalarea(l,b,h):
    def area(d1,d2):
        return d1*d2
    return 2*((area(l,b))+(area(b,h))+(area(h,l)))

print(totalarea(2,3,4))
# 52

