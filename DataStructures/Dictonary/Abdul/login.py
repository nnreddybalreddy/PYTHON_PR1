users=["john","bob","alex","alice","charlie","john","alex","john","alex"]

d4={}


# for i in users:
#     if i in d4:
#         d4[i]+=1
#         print(i,d4[i])
#     else:
#         d4[i]=1
#         print(i,d4[i])

# print(d4) 

# for i in users:
#     if i in d4:
#         d4[i]+=1
#     else:
#         d4[i]=1
# print(d4)  

for i in users:
    if i in d4:
        d4[i]+=1
    else:
        d4[i]=1
print(d4)            
#{'john': 3, 'bob': 1, 'alex': 3, 'alice': 1, 'charlie': 1}




