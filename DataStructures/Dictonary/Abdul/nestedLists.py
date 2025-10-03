data=[["james",25,"NY"],["Kiran",30,"DEL"],["Smith",24,"PAR"],["Raj",27,"DEL"]]

header=['name','age','city']


length=len(header)
result=[]

for i in range(length):
    newdict={}
    for row in data:
        if row[i] not in newdict:
            newdict[row[i]]=[row]
        else:
            newdict[row[i]].append(row)    

    result.append(newdict)

# print(result)

# result=[]

# length=len(header)

# for i in range(length):
#     newdict={}
#     for row in data:
#         if row[i] not in newdict:
#             newdict[row[i]]=[row]
#         else:
#             newdict[row[i]].append(row)  
    
#     result.append(newdict)

# print("Dict")


for i in range(length):
    print("\n"+header[i])
    for key,value in result[i].items():
        print(f'{key:<10}:{value}')




