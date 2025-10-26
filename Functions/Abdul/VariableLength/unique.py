def unique_number(*args):
    num=set(args)
    return list(num)


num=input("Enter numbers")

# print(num.split())
# ['2', '6', '1', '2', '3', '5', '6', '7']

numbers=[int(n) for n in num.split()]
# print(numbers)
# [1, 2, 0, 3, 5, 4, 3]

unique=unique_number(*numbers)
print(unique)
