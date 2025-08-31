# Reverse a number 
# n = 1257
# r = 7521 

n=1257 
rev=0
while n>0:
    r= n%10 
    rev=rev*10+r 
    n=n//10 
print(rev)  # Output: 7521

if (n==rev):
    print("Palindrome")



