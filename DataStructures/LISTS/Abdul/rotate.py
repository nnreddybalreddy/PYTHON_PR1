L1=[1,2,3,4,5,6]
n=int(input("No of rotations:::"))

L2=L1[n:]+L1[:n]

print(L2)