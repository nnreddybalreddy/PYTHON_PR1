#Union 
s1={1,2,3,5,7}
s2={5,7,9,10,11}

s3=s1.union(s2)
print(s3)
#Output: {1, 2, 3, 5, 7, 9, 10, 11}

#Intersection

s3=s1.intersection(s2)
print(s3)   
#Output: {5, 7}


#intersection update

s1.intersection_update(s2)
print(s1)
#Output: {5, 7}

#calling on S1 will be updated


#Difference
s1={1,2,3,5,7}
s2={5,7,9,10,11}

s3=s1.difference(s2)
print(s3)
#Output: {1, 2, 3}
#s1 will not be updated

#difference update
s1.difference_update(s2)
print(s1)
#Output: {1, 2, 3}



#symmetric difference
s1={1,2,3,5,7}
s2={5,7,9,10,11}

s3=s1.symmetric_difference(s2)
print(s3)
#Output: {1, 2, 3, 9, 10, 11}
#s1 will not be updated

#symmetric difference update
s1.symmetric_difference_update(s2)
print(s1)
#Output: {1, 2, 3, 9, 10, 11}


#update
s1={1,2,3,5,7}
s2={5,7,9,10,11}

s1.update(s2)
print(s1)
#Output: {1, 2, 3, 5, 7, 9, 10, 11}

