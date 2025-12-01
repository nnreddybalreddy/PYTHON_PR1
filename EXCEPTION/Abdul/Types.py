# Syntax Error
# a=input("Enter A:")
# b=input("Enter B)

# Output:     b=input("Enter B)
            ^
# SyntaxError: unterminated string literal (detected at line 6)


# 2. 
# Logical Error

a=input("Enter A:")
b=input("Enter B:")

if a>b:
    print(a)
else:
    print(a)


# a=10
# b=20

#Output:
# 10 (But the answer should be 20)

# else:
#     print(a)




# 3. 
# Runtime Error:
     # Type Error
     # Zero Division Error

a=input("Enter A:")
b=input("Enter B:")

c=a//b 

print(c)

#output:
# Enter A:5
# Enter B:ERROR!
# 10
# Traceback (most recent call last):
#   File "<main.py>", line 7, in <module>
# TypeError: unsupported operand type(s) for //: 'str' and 'str'

a=input("Enter A:")
b=input("Enter B:")

c=a//b

print(c)


#output 1:
# Enter A:10
# Enter B:5
# 2

#output 2:
# Enter A:10
# Enter B:0
# ERROR!
# Traceback (most recent call last):
#   File "<main.py>", line 7, in <module>
# ZeroDivisionError: integer division or modulo by zero

