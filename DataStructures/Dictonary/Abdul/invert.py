original={"a":1,"b":2,"c":1,"d":2,"e":3,"f":2}
#original={"a":1,"b":2,"c":1}
inverted={}


# for x,y in original.items():
#     if y not in inverted:
#         inverted[y]={x}
#     else:
#         inverted[y].add(x)
            
# print(inverted)


# for x,y in original.items():
#     if y not in inverted:
#         inverted[y]={x}
#     else:
#         inverted[y].add(x)

# print(inverted)

# for x,y in original.items():
#     if y not in inverted:
#         inverted[y]={x}
#     else:
#         inverted[y].add(x)    

# print(inverted)
#original={"a":1,"b":2,"c":1}
original={"a":1,"b":2,"c":1,"d":2,"e":3,"f":2}
for x,y in original.items():
    if y not in inverted:
        inverted[y]={x} 
        print(inverted)
        #{1: {'a'}}
        # {1: {'a'}, 2: {'b'}}
    else:
        inverted[y].update(x)
        print(inverted)
        # {1: {'c', 'a'}, 2: {'b'}}


print(inverted)   
#{1: {'a', 'c'}, 2: {'d', 'b', 'f'}, 3: {'e'}}
     
        
            


