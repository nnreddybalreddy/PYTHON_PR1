original={"a":1,"b":2,"c":1,"d":2,"e":3,"f":2}
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

for x,y in original.items():
    if y not in inverted:
        inverted[y]=x 
    else:
        inverted[y].add(x)
            


