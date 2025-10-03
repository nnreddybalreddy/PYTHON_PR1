L1=[1,2,3,4,5,6,8,9]
L_odd=[]
L_even=[]

# for i in L1:
#     if i%2 == 0 :
#         L_odd.append(i)
#     else:
#         L_even.append(i)

# print(L_odd)
# print(L_even)

odd=[x for x in L1 if x%2==0]
even=[x for x in L1 if x%2!=0]

print(odd)
print(even)