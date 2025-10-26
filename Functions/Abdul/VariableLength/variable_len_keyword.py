#variabel length arguments--> Positional
# def fun(*args):
#     print(args)

# Variable length arguments--> Keyword

def fun(**kwargs):
    print(kwargs)
    print(type(kwargs))
    # {'a': 5, 'b': 10, 'c': 15}
    # <class 'dict'>


fun(a=5,b=10,c=15)

######################


def fun(**kwargs):
    for item in kwargs.items():
        if item[0]=='b':
            print(item[1])
            #10

        
    


fun(a=5,b=10,c=15)
#dict_items([('a', 5), ('b', 10), ('c', 15)])

###############################################


def fun(**kwargs,a,b):
    print(kwargs)


fun(a=5,b=10,c=15)
# SyntaxError: invalid syntax

############################################

# def fun(a,b,**kwargs):
#     print(kwargs)
#     # print(a,b,kwargs)



# fun(a=5,b=10)    #{}
# fun(a=5,b=10,c=15)  #{'c': 15}
# fun(1,2,c=3)
#    #print(a,b,kwargs)    #1 2 {'c': 3}

# #works for both keyword and positional

#########################################



def fun(*args,a,b,**kwargs):
    print(a,b,kwargs)
    print(args)

fun(1,2,3,4,x=5,y=10)
#TypeError: fun() missing 2 required keyword-only arguments: 'a' and 'b'

fun(1,2,a=3,b=4,x=5,y=10)
 # print(args)  --> (1,2)
 # print(a,b,kwargs) -- 3 4 {'x': 5, 'y': 10}

