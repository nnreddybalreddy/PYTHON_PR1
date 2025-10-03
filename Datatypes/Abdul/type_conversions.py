print(int(16.59))
print(type(int(16.59)))
#<class 'int'>
#16
print(int(True))
#1
print(int("125"))
#125

print(int('0b1010',2))
#10

print(int("0xA",16))
#10

# print(int("Alexa"))
#ValueError: invalid literal for int() with base 10: 'Alexa'

# print(int(3+1j))
#TypeError: can't convert complex to int
############# Float

# print(float(125))
# #125.0
# print(float(True))
# #1.0
# print(float("12.75"))
# #12.75


#################### bool

print(bool(10))
#True

print(bool(-12))
#True

print(bool(-1.2E-3))
#True

print(bool(3+4j))
#True

print(bool("False"))
#True

print(bool())
#False
print(bool(0))
#False
print(bool(False))
#False

##################### Complex

print(complex(10))
#(10+0j)
print(complex(-12.5))
#(-12.5+0j)
print(complex(True))
#(1+0j)

print(complex(False))
#0J
print(complex("3+4j"))
#3+4j

################# string

print(str(10))
#10
print(str(-12))
#-12
print(str(-1.2E-3))
# -0.0012
print(str(False))
#False
print(str(3+4j))
#3+4j