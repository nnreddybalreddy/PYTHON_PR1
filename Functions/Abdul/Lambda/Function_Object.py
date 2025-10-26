print(print)
#<built-in function print>
print(print.__doc__)
#print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)

#Prints the values to a stream, or to sys.stdout by default.
#Optional keyword arguments:
#file:  a file-like object (stream); defaults to the current sys.stdout.
#sep:   string inserted between values, default a space.
#end:   string appended after the last value, default a newline.
# flush: whether to forcibly flush the stream.

print(print.__name__)
#print

show=print
show("Hello World")
#Hello World


take=input
name=take("Enter your name: ")
print("Welcome",name)
#Enter your name: Abdul
#Welcome Abdul

def fun():
    print("My Function1")

f=fun 
f()
#My Function1
