# #add(element)
# #update(iterable)
# #copy()


# #pop() --> Revmove top most element
# #remove(element)
# #discard(element)
# #rclear()


#Add
s1={10,20,30,40,50}
print(len(s1))
#5

s1.add(60)
print(s1)
#{40, 10, 50, 20, 60, 30}

# s1.add(70,80)
# #TypeError: set.add() takes exactly one argument (2 given)

s1.add((70,80))
print(s1)
#{(70, 80), 40, 10, 50, 20, 60, 30}
#as tuple single element


s1.add([70,80])
#TypeError: unhashable type: 'list'


#update(iterable)

s1={10,20,30,40,50}
s1.update((60,70))
print(s1)
#  {40, 10, 70, 50, 20, 60, 30}


s1={10,20,30,40,50}
s1.update('ruby')
print(s1)
#{'b', 40, 10, 'y', 50, 20, 'r', 30, 'u'}


#copy

s1={10,20,30,40,50}
s2=s1.copy()
print(id(s1),id(s2))
# 1967206105160 1967206063240

#pop

s1={10,20,30,40,50}
print(s1.pop())
#40
print(s1)
#{10, 50, 20, 30}

print(s1.pop())
#10
print(s1)
#{50, 20, 30}

#discard
# 
# 
s1={10,20,30,40,50}
print(s1.discard(30))
#None

print(s1)
#{40, 10, 50, 20}
print(s1.discard(100))
#None
#  #no Error
print(s1)   
#{40, 10, 50, 20}

#remove

s1={10,20,30,40,50}
print(s1.remove(30))
#None

print(s1)
#{40, 10, 50, 20}


# print(s1.remove(100))
# #KeyError: 100


# s1.remove(10,20)
# #TypeError: set.remove() takes exactly one argument (2 given)

s1={10,(20,30),40,50}
s1.remove((20,30))
print(s1)
#{40, 10, 50}

#clear

s1={10,20,30,40,50}
s1.clear()
print(s1)   
#set()

#del
s1={10,20,30,40,50}
del s1
print(s1)
#NameError: name 's1' is not defined











