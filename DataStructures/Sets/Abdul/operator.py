#  |               --> Union
#  |=             --> Update
#  &               --> Intersection
#  &=              --> Intersection update

#  -              --> Difference
#  -=             --> Difference update
#  ^              --> Symmetric difference
#  ^=             --> Symmetric difference update

#union
s1={1,2,3,5,7}
s2={5,7,9,10,11}

s3=s1 | s2
print(s3)
#Output: {1, 2, 3, 5, 7, 9, 10, 11}

#Update
s1 |= s2
print(s1)
#Output: {1, 2, 3, 5, 7, 9, 10, 11}


#Intersection
s1={1,2,3,5,7}
s2={5,7,9,10,11}

s3=s1 & s2
print(s3)   
#Output: {5, 7}

#Intersection update
s1 &= s2
print(s1)
#Output: {5, 7}

#difference

s1={1,2,3,5,7}
s2={5,7,9,10,11}

s3=s1 - s2
print(s3)
# Output: {1, 2, 3}

#difference update
s1 -= s2
print(s1)
#Output: {1, 2, 3}

#symmetric difference
s1={1,2,3,5,7}  
s2={5,7,9,10,11}
s3=s1 ^ s2
print(s3)
#Output: {1, 2, 3, 9, 10, 11}


#symmetric difference update
s1 ^= s2
print(s1)
#Output: {1, 2, 3, 9, 10, 11}






