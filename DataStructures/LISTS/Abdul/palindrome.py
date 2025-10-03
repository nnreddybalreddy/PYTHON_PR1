L1=[5,4,3,3,4,5,6]

############# 1
# i=0
# j=len(L1)-1
# flag=0

# while(i<j):
#     if L1[i]!=L1[j]:
#         flag=1
#         break
#     elif L1[i]==L1[j]:
#         print(i,j)
#         i=i+1
#         j=j-1
# else:
#     print("Given palindrom...")

# print(flag)

############### 2

lst = [5, 4, 3, 3, 4, 5]

rev = lst[::-1]

if lst == rev:
    print('Yes Palindrome')
else:
    print('Not Plaindrome')   

  




