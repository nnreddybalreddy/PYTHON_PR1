def fun(n):
    if(n>0):
        print(n,end=" ")
        fun(n-1)
        #3 2 1
fun(3)   

# fun(3)
# 3   fun(2)
#     2  fun(1)
#         1   fun(0)

# fun(0)-->fun(1)->fun(2)->fun(3)

################333 Factorial

def fact(n):
    if(n<=0):
        return 1
    else:
        return n * fact(n-1)
print(fact(5))        

# fact(5)
# 5   fact(4)
#     4   fact(3)
#         3   fact(2)
#             2  fact(1)
#                 1 fact(0)


