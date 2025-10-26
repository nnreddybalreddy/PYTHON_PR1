def fib(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

for i in range(8):
    print(fib(i), end=" ")


# 0 1 1 2 3 5 8 13

################################

def fib(n):
    a, b = 0, 1
    for i in range(n+1):
        yield a
        a, b = b, a + b

if __name__ == "__main__":
    for num in fib(7):
        print(num, end=" ")
# 0 1 1 2 3 5 8 13        