# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.



a=10
b=2
c=a//b
print(c)

#5 

###############        1
a=10
b=0

c=a//b
print(c)


#  File "<main.py>", line 12, in <module>
# ZeroDivisionError: integer division or modulo by zero



################  2. 

a=10
b='x'

c=a//b

print(c)

# TypeError: unsupported operand type(s) for //: 'int' and 'str'


######### 3

L1=[3,6,9,12,15]
print(L1[0])
# 3

print(L1[6])

# IndexError: list index out of range





############### 4
d={1:"one",2:"two",3:"three"}

print(d[5])

#KeyError: 5


############## 5

int('xyz')
#ValueError: invalid literal for int() with base 10: 'xyz'


######################### 6

int('xyz)
#SyntaxError: unterminated string literal (detected at line 67)


############################# 7




