#abs(x,/) --> Positinal only

print(abs(-70))
#70
print(abs(-70.12))
#70.12
print(abs(3+4j))
#5.0
#SQRT(a**a + b**b) = Hypotenuse

#pow(base,exp,mod=None,/) --> Positinal only

print(pow(2,3))
#8
print(pow(10,2))
#100

print(pow(10,2,3))
# (10*2)%3 = 1 

#round
# round(number,ndigits=None)

print(round(4.4))
#4
print(round(4.6))
#5
print(round(4.5))
#4
print(round(5.5))
#6 --> Close to even number

print(round(3.5421))
#4
print(round(3.5421,2))
#3.54

#divmod
#divmod(a,b,/) --> Positinal only


print(divmod(10,3))
#(3,1)
#10/3= 3.3333  
#10%3 = 1

print(divmod(61,7))
#(8,5)

######### min
#min(iterable, *,key=None,default=None) --> Keyword arguments(*)

print(min(10,3,7,2,5))
#2

print(-10,3,7,-2,-5)
#-10

print(min(-10,3,7,-2,-5,key=abs))
#-2

print(min([],default="Empty List"))
#Empty List

################### max
#max(iterable, *,key=None,default=None) --> Keyword arguments(*)

words=["apple","banana","kiwi","grape"]

max(words,key=len)
#'banana'

############################
############ sum
#sum(iterable,start=0)

print(sum([1,2,3,4,5]))
#15

# print(sum([1,2,3,4,5],start=20))
# #35

################ EVAL
#eval(expression,globals=None)
#expression-string

print(eval("10+20*4-5"))
#85 

global_dict={"x":15,"y":20}
locals_dict={"a":5}

eval("x + y + a",global_dict,locals_dict)
#35--> 15+20+5


