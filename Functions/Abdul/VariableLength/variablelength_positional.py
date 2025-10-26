# print()
# print(10)
# #10
# print(10,12.5)
# # 10 12 5
# print(10,12.5,"hello",5,True)
# # 10 12.5 hello 5 True

     #print function taking variable length arguments
###########################################

def fun(*args):
    print(args)
    # print(type(args))
    # #<class 'tuple'>
    for i in args:
        print(i,end=" ")
        #5 1.25 hello 15
   


fun(5) 
#(5,)
fun(5,10)
#(5,10)
fun(5,10,15)
# (5,10,15)
fun(5,1.25,"hello",15)

############################


def fun(*args):
    for x in args:
        if type(x)==int:
            print(x)
            #10 15

fun(10,12.5,"hello",True,3+4j,15)

######################################################


def fun(a,b,*args):
    print(a,b,args)


fun(10,20,30)
        #10 20 (30,)
fun(10,20,30,40,50)
    #     10 20 (30, 40, 50)

fun(a=10,b=20,30,40,50)
#  SyntaxError: positional argument follows keyword argument


###########################################################


def fun(*args,a,b):
    print(a,b,args)

fun(10,20,30,40,50)
# TypeError: fun() missing 2 required keyword-only arguments: 'a' and 'b'


########################################################

def fun(*args,a,b):
    print(a,b,args)

fun(10,20,30,a=40,b=50)
# 40 50 (10, 20, 30)

######################################



def fun(*args):
    print(args,len(args))
    

L1=[10,20,30]
fun(L1)
#([10, 20, 30],) 1

L1=[10,20,30]
fun(*L1)
# (10, 20, 30) 3
