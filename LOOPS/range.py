# print(list(range(5))) #[0, 1, 2, 3, 4]


# print(list(range(5,15,2)))  # [5, 7, 9, 11, 13]

# print(list(range(2,20,2)))  # [2, 4, 6, 8, 10, 12, 14, 16, 18]
# print(list(range(2,22,2)))  # [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
# print(list(range(10,5))) #[]

# print(list(range(10,5,-1))) #[10, 9, 8, 7, 6]

# print(list(range(10,5,-2))) #[10, 8, 6]


# print(list(range(0,101,2)))  # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98]
# print(list(range(1,101,2))) #   [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97, 99]


# for i in range(10):
#     print(i, end=' ')  # prints numbers from 0 to 9 in a single line separated by space
#                        # Output: 0 1 2 3 4 5 6 7 8 9

# lst1=[5,6,7,"Hi","Python",True,False,3.14]

# for i in range(len(lst1)):
#     print(lst1[i], end=' ')  # prints each element of the list in a single line separated by space
#                             # Output: 5 6 7 Hi Python True False 3.14

# for i in range(len(lst1)):
#     print(f'index: {i} value:{lst1[i]}')  # prints index and value of each element in the list
# Output:   
#index: 1 value:6
##index: 2 value:7
#index: 3 value:Hi
#index: 4 value:Python
#index: 5 value:True
#index: 6 value:False
#index: 7 value:3.14


# lst1=[5, 6, 7, "Hi", "Python", True, False, 3.14]

# for i in range(len(lst1)):
#     print(f'index: {i} value: {lst1[i]}')  # prints index and value of each element in the list

for i in range(1,11):
    if i % 2 == 0:
        print(f"{i} is even")

print(list(range(1,11,2)))  # prints odd numbers from 1 to 10
print(list(range(2,11,2)))  # prints even numbers from 2 to
