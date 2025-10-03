import random as rd 
print(rd.random())
#0.052026860293764465

print(rd.randint(1,100))
#93
print(rd.randint(1,100))
#94
print(rd.randrange(1,10,2))
#1

print(rd.randrange(1,10,2))
#3

for i in range(5):
    print(rd.randint(1,100),end=" ")
#42 30 68 42 16 -> 1st run
# 37 67 3 22 26  --> 2nd Run
#     

print("\n")
rd.seed(10)

for i in range(5):
    print(rd.randint(1,100),end=" ")
# 74 5 55 62 74   - Run1
# 74 5 55 62 74  -- Run2
# 74 5 55 62 74  -- Run3
# 74 5 55 62 74  -- Run4

L1=[1,2,3,4,5,6,7]
rd.shuffle(L1)
print(L1)
# [2, 4, 6, 3, 7, 5, 1]
# [3, 1, 2, 7, 6, 5, 4]
# [4, 5, 1, 6, 3, 7, 2]
# [6, 1, 2, 7, 5, 3, 4]

