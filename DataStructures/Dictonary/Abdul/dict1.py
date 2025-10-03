#key and value pair
d1={1:"one",2:"two",3:"Three",4:"four"}
print(d1)
#{1: 'one', 2: 'two', 3: 'Three', 4: 'four'}

print(d1[1])
#one 

# print(d1[5])
# #KeyError

#update
d1[3]="tres"
print(d1)
# {1: 'one', 2: 'two', 3: 'tres', 4: 'four'}


#write
#Assign new value
d1[5]="five"
print(d1)
# {1: 'one', 2: 'two', 3: 'tres', 4: 'four', 5: 'five'}

# Traverse

for i in d1:
    print(i,d1[i])

# 1 one
# 2 two
# 3 tres
# 4 four
# 5 five


#hetro genous
d1={1:3.5,2.5:True,5+6j:"abc"}


d2={1:[10,11],2:(4,5),3:{8,9},4:{1:1,2:2}}
print(d2[4])
# {1: 1, 2: 2}

d3={(1,2):"hi"}
# d4={[1,2,3]:"hi"}
# #list is mutable


d5={'abacus':'a calculator',"bachelor":"unmarried"}
d6={101:"John",102:"smith",103:"mark",104:"David"}








