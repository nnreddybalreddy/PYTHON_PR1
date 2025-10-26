# def fun(a,b,c,d):
#     print(a,b,c,d)

# fun(5,10,15,20)
# fun(a=5,b=10,c=15,d=20)


#Case 1
#a,b positional only
#c,d positinal/keyword

def fun(a,b,/,c,d):
    print(a,b,c,d)

fun(5,10,c=15,d=20)

fun(a=15,b=10,c=15,d=20)
#TypeError: fun() got some positional-only arguments passed as keyword

fun(5,10,c=15,d=20)
fun(5,10,15,d=20)

fun(5,b=10,c=15,d=20)
##TypeError: fun() got some positional-only arguments passed as keyword




