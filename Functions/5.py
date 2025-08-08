# def get_result():
#     result=num*10
#     print(f'Result: {result}')
#     return None

# num=eval(input("Enter a number: "))    
# get_result()

#output:
#  Enter a number: 6
#  Result: 60

###### 2
# def get_result():
#     result=num*10
#     print(f'Result: {result}')
#     return None

# def main():
#     num=eval(input("Enter a number: "))
#     get_result()
#     return None

# main()

# output:
#   result=num*10
#    NameError: name 'num' is not defined

############ 3

# def get_result(num):
#     result=num*10
#     print(f'Result: {result}')
#     return None

# def main():
#     num=eval(input("Enter a number: "))
#     get_result(num)
#     return None

# main()

# Enter a number: 6
# Result: 60

############## 4

# def get_result(value):
#     result=value*10
#     print(f'Result: {result}')
#     return None

# def main():
#     num=eval(input("Enter a number: "))
#     get_result(num)
#     return None

# main()

# Enter a number: 6
# Result: 60


####### 5 


# def get_result(value):
#     result=value*10
#     print(f'Result: {result}')
#     return None

# def main():
#     num=eval(input("Enter a number: "))
#     get_result(num)
#     return None

# main()

# Enter a number: 6
# Result: 60


######### 6

# a=eval(input("Enter a number: "))
# b=eval(input("Enter a number: "))

# result=a+b 
# print(f'Result: {result}')
# result=a-b 
# print(f'Result: {result}')
# result=a*b
# print(f'Result: {result}')
# result=a/b
# print(f'Result: {result}')


def add(p,q):
    print(f'Addition: {p+q}')
    return None

def subtract(m,n):
    print(f'Subtraction: {m-n}')
    return None 


def main():
    a=eval(input("Enter a number: "))
    b=eval(input("Enter a number: "))
    add(a,b)  # 11 
    subtract(a,b) # -1
    subtract(b,a) # 1 --> Positional argument 
    subtract(10,5) # 5 --> Positional argument
    return None 

main()     #5,6 










