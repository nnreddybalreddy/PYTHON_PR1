# sorted(iterable,/,*,key=None,reverse=False) --> Positinal and Keyword arguments(*)
L1=[1,12,7,-3,8]
print(sorted(L1))
# [-3, 1, 7, 8, 12]

print(sorted(L1,reverse=True))
# [12, 8, 7, 1, -3]

print(sorted(L1,key=abs))
# [1, -3, 7, 8, 12]



############### Reverse
# reverse(iterable) --> Positinal only

L1=[1,12,7,-3,8]
print(reversed(L1))
# <list_reverseiterator object at 0x000001D5518070B8>

rev=reversed(L1)
print(list(rev))
# [8, -3, 7, 12, 1]

###################slice
#slice(start=None,stop=None,step=None) --> Positinal only
#stop compulsory

#s=slice(0,stop,1)

L1=[10,20,30,40,50,60,70]
s=slice(5)
print(L1[s])
# [10, 20, 30, 40, 50]


######## Iter/Next
############ iter(object,sentinel=None) --> Positinal only

L1=[10,20]
it=iter(L1)

print(next(it))
#10
print(next(it))
#2
print(next(it))
# StopIteration