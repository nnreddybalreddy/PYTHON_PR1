L1=[(1,"one"),(2,"two"),(3,"three"),(4,"four")]

# d1=dict(L1)
# print(d1)
# {1: 'one', 2: 'two', 3: 'three', 4: 'four'}

d1={x:y for x,y in L1 }
print(d1)
# {1: 'one', 2: 'two', 3: 'three', 4: 'four'}


L1=[1,2,3,4]
L2=["one","two","three","four"]

# d2=dict(zip(L1,L2))
# print(d2)
#{1: 'one', 2: 'two', 3: 'three', 4: 'four'}

d2={  for x,y in zip(L1,L2)}
print(d2)
# {1: 'one', 2: 'two', 3: 'three', 4: 'four'}


L1=["one","two","three","four"]
# d3=dict(enumerate(L1,start=1))

# print(d3)
# # {1: 'one', 2: 'two', 3: 'three', 4: 'four'}


d4={x:y for x,y in enumerate(L1,start=1)}

print(d4)
{1: 'one', 2: 'two', 3: 'three', 4: 'four'}