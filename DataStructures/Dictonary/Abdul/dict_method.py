#update(dictonary)
#fromkeys(sequence,default)
#copy()
#pop(key,alt_value)
#popitem()
#clear()

d1={1:"one",2:"two",3:"three",4:"four"}
d2={5:"five"}

d1.update(d2)
print(d1)
# {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five'}

L1=[1,2,3,4]

d2=dict.fromkeys(L1)
print(d2)
# {1: None, 2: None, 3: None, 4: None}

d3=dict.fromkeys(L1,"Unknown")
print(d3)
# {1: 'Unknown', 2: 'Unknown', 3: 'Unknown', 4: 'Unknown'}


#################### COPY

d5=d1.copy()
print(d1)
print(d5)
# {1: 'one', 2: 'two', 3: 'three', 4: 'four'}
# {1: 'one', 2: 'two', 3: 'three', 4: 'four'}


d5[1]="Oneee"
print(d1)
# {1: 'one', 2: 'two', 3: 'three', 4: 'four'}

# shallow copy

print(d5)
#{1: 'Oneee', 2: 'two', 3: 'three', 4: 'four'}


######## pop
d1={1:"one",2:"two",3:"three",4:"four"}

print(d1.pop(2)) 
#two
print(d1)
# {1: 'one', 3: 'three', 4: 'four'}

# d1.pop(5)
# #     d1.pop(5)
# # KeyError: 5

print(d1.pop(5,"missing"))
# missing

######  popitem()

d1={1:"one",2:"two",3:"three",4:"four"}
print(d1.popitem())
# (4, 'four')

d1.clear()

print(d1)
# {}

del d1
print(d1)
# NameError: name 'd1' is not defined
