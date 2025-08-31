# n=5
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         print("*",end=" ")
#     print("\n")
# # * * * * *

# # * * * * *

# # * * * * *

# # * * * * *

# # * * * * *

############### 2

n=5 

for i in range(1,n+1):
    for j in range(1,i+1):
        print("*",end=' ')
    print("\n")

for i in range(1,n+1):
    for j in range(1,n+1):
        if i>=j:
            print("*",end=' ')
    print("\n")  
n=5
for i in range(1,n+1):
    print("*"*i,end=" ")
    print("\n")


# i >=j
# *
# * * 
# * * *
#* * * *
#* * * * *
###################
# n=5
# for i in range(n,0,-1):
#     print(i*"*",end=" ")
#     print("\n")

# for i in range(n,0,-1):
#     for j in range(i):
#         print("*",end=" ")
#     print("\n")    


# * * * * *

# * * * *

# * * *

# * *

##################### 4
n=5

for i in range(n,0,-1):
    for s in range(1,n-i+1):
        print(" ",end=" ")
    for j in range(i):
        print("*",end=" ")
    print("")     

# * * * * *
#   * * * *
#     * * *
#       * *
#         *




for i in range(1,n+1):
    print(" "*(i-1),end=" ")
    print("*"*(n-(i-1)))

#  *****
#   ****
#    ***
#     **

    








