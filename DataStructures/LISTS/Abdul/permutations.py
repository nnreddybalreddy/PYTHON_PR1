import itertools as it 

lst=["A","B","C","D"]

# #permutations(iterable,r=None)
# #combinations(iterable,r=None)
# #product(iterable,repeat=1)



# perms=it.permutations(lst,r=2)
# print(type(perms))
# #<class 'itertools.permutations'>

# perms=list(perms)
# for i in perms:
#     print(i,end=" ")
# # ('A', 'B') ('A', 'C') ('A', 'D') ('B', 'A') ('B', 'C') ('B', 'D') ('C', 'A') ('C', 'B') ('C', 'D') ('D', 'A') ('D', 'B') ('D', 'C')

# combi=it.combinations(lst,r=2)
# combi=list(combi)

# for i in combi:
#     print(i)

product=it.product(lst,repeat=2)

product=list(product)

for i in product:
    print(i,end=" ")
#('A', 'A') ('A', 'B') ('A', 'C') ('A', 'D') ('B', 'A') ('B', 'B') ('B', 'C') ('B', 'D') ('C', 'A') ('C', 'B') ('C', 'C') ('C', 'D') ('D', 'A') ('D', 'B') ('D', 'C') ('D', 'D')
