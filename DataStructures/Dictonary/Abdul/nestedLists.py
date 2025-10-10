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

#name
#james     :[['james', 25, 'NY']]
#Kiran     :[['Kiran', 30, 'DEL']]
#Smith     :[['Smith', 24, 'PAR']]
#Raj       :[['Raj', 27, 'DEL']]

#age
#25        :[['james', 25, 'NY']]
#30        :[['Kiran', 30, 'DEL']]
#24        :[['Smith', 24, 'PAR']]
#27        :[['Raj', 27, 'DEL']]

#city
#NY        :[['james', 25, 'NY']]
#DEL       :[['Kiran', 30, 'DEL'], ['Raj', 27, 'DEL']]
#PAR       :[['Smith', 24, 'PAR']]




