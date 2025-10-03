#List comprehensions

#L1=[iterable]
# L=list(iterable)

# L=[exp for item in iterable]
#
#for x in range(1,5):
#    print(x)


L1=[x for x in range(1,5)]    
print(L1)
#[1, 2, 3, 4]


L2=[x**2 for x in range(1,5)]
print(L2)
#[1, 4, 9, 16]

L3=[ x.casefold() for x in "PyThoN"]
print(L3)
#['p', 'y', 't', 'h', 'o', 'n']

L4=[int(x) for x in "12345"]
print(L4)
#[1, 2, 3, 4, 5]

L5=[x for x in "ab*cd7e" if x.isalpha()]
print(L5)
#['a', 'b', 'c', 'd', 'e']


