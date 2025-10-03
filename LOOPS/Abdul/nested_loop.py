# for i in range(1,4):
#     for j in range(1,4):
#         print(i,'-',j)
# 1 - 1
# 1 - 2
# 1 - 3
# 2 - 1
# 2 - 2
# 2 - 3
# 3 - 1
# 3 - 2
# 3 - 3

#################33 2

# #prime numbers 1-100
n=int(eval(input("Enter number")))

for i in range(1,n+1):
    count=0
    for j in range(1,i+1):
        if i % j == 0:
            count=count+1
    if count==2:
        print(i,end=' ')

#########
      



