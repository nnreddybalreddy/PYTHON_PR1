import uuid 
items=[
    ["laptop",1200],
    ["mouse",20],
    ["keyboard",30],
    ["tablet",200]
]

item_data={}

# for i in items:
#     id=uuid.uuid5(uuid.NAMESPACE_OID,i[0])
#     key=id.hex[:6]
#     item_data[key]=i



# for k,v in item_data.items():
#     print(f'{k}{v}')

for i in items:
    id=uuid.uuid5(uuid.NAMESPACE_OID,i[0])
    key=id.hex[:6]
    item_data[key]=i

print(item_data)