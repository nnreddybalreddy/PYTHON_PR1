# s1="Hello World"

# print(s1[0])
# # H

# print(s1[-7])
# # o

# s1[0]='w'

# print(s1)
#TypeError: 'str' object does not support item assignment

###### String Slicing-2

# []
# s1[start:stop:step]
# it s like range(start,stop,step)

#indexing and slicing for string lists tuple--> Sequence type

s1="Hello world"
# print(s1[6]) # w
# print(s1[-5]) # w

# print(s1[1:7])
# #ello w
# print(s1[3:7])
# # lo w

# print(s1[:7]) #0,7
# # Hello w

# print(s1[:]) # Entire string
# # Hello world

# print(s1[6:]) # end of string
# # world

# print(s1[-5:])
# #world

# print(s1[-5:-2]) 
# #wor

# print(s1[-11:-2])
# # Hello wor
# # forward direction

# # Step
# print(s1[0:11:1]) # By default step is 1
# #Hello world

# print(s1[0:11:2]) 
# # Hlowrd

# print(s1[::])
# # Hello world

# print(s1[::-1])
# # dlrow olleH

# s1="Hello world"
# s2=s1[::]


# print(s2[::-1])
# # dlrow olleH
s2="Hello world"
print(s2[-3::-1])
# row olleH

s2="Hello world"

print(s2[-3:9:-1])
# no print . forward direction only

print(s2[8:2:-1])
#row ol




