# list is mutable
#Read/Write

#Read
 # Indexing
 # slicing

#Read Indexing 

L1=[3,6,9,12,15,18,21]
print(L1[4])
# 15

print(L1[-3])
#15 

#Slicing
print(L1[::]) #Start,Stop,Step
# [3, 6, 9, 12, 15, 18, 21]
print(L1[:]) #Begin,#End
# [3, 6, 9, 12, 15, 18, 21]



print(L1[2:]) #2 to End
#[9, 12, 15, 18, 21]

print(L1[:6]) #0 to 5
[3, 6, 9, 12, 15, 18]

print(L1[2:6]) #2 to 5
# [9, 12, 15,18]
print(L1[-5:-2]) #-ve indexing
# [9, 12, 15]
#forward print
#9,12,15


print(L1[::])
#[3, 6, 9, 12, 15, 18, 21]
print(L1[::1])
# [3, 6, 9, 12, 15, 18, 21]

print(L1[::2]) #[3, 9, 15, 21]
print(L1[::3]) # [3, 12, 21]


print(L1[::-1]) # [21, 18, 15, 12, 9, 6, 3]
#Reverse,backward,indices also backwards
L1=[3,6,9,12,15,18,21]
print(L1[4::-1]) # [15, 12, 9, 6, 3]
print(L1[4:0:-1]) # [15, 12, 9, 6]

print(L1[-3:-7:-1]) # [15, 12, 9, 6]



