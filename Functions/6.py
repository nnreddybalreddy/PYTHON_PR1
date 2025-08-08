# a=eval(input("Enter a number: "))
# b=eval(input("Enter a number: "))
# result=a+b 
# print(f'Result: {result}')

# def add(p,q):
#     result=p+q 
#     print(f'Result: {result}')
#     return None

# def main():
#     a=eval(input("Enter a number: "))
#     b=eval(input("Enter a number: "))
#     add(a,b)
#     return None

# main()

###### output
# Enter a number: 6
# Enter a number: 5
# Result: 11

######## 2


# def add(p,q):
#     result=p+q 
#     return result

# def main():
#     a=eval(input("Enter a number: "))
#     b=eval(input("Enter a number: "))
#     result=add(a,b)
#     print(f'Result: {result}')
#     return None

# main()

# Enter a number: 5
# Enter a number: 6
# Result: 11

############ 3

# def multiply(p):
#     # result=p*10 
#     # return result
#     return p * 10


# def main():
#     num=eval(input("Enter a number: "))
#     result=multiply(num)
#     print(f'Result: {result}')


# main()

def add(p, q):
    return p*q


def main():
    num=eval(input("Enter a number: "))
    result=add(num, 10)
    print(f'Result: {result}')

main() 


