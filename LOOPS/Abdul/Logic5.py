# # Find Max Element 
# n=5 
# i=0
# max=0

# while i<n:
#     i=i+1
#     num=int(eval(input("Enter a number: ")))
#     if num>max:
#         max=num
# print(max)        

########## max / min of n numbers
n=5 
i=0
max=float('-inf')  # Initialize max to the smallest possible value  
min=float('inf')  # Initialize min to the largest possible value



while i<n:
    i=i+1
    num=int(eval(input("Enter a number: ")))
    if num>max:
        max=num
    if num<min:
        min=num
print(max) 
print(min)