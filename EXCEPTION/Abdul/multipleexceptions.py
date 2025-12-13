L=[10,20,30,40,50]

try:
    index=int('abc')
    print(L[index])
except (IndexError,TypeError) as msg:
    print(msg)

print("End of program")
    