#s={iterable}
#s={exp for item in iterable if condition}

S1={x for x in range(1,5)}
print(S1)
#{1, 2, 3, 4}
print(type(S1))
#<class 'set'>


S2={x*x for x in {-2,-1,0,1,2}}
print(S2)
#   {0, 1, 4}
print(type(S2))
#<class 'set'>

S3={x.lower() for x in "PHILIPins"}
print(S3)   
#  {'h', 'i', 'p', 'l', 'a', 's', 'n'}
print(type(S3)) 
#<class 'set'>

#Set comprehension with no dups
#{}--> flower braces

#[]--> List
#[]-->Allow dups






