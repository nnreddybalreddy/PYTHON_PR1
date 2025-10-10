# dic1={}
# print(type(dic1),dic1,bool(dic1))  # <class 'dict'>                {}        False

dic1={"fruit":"banana",'animal':"monkey",1:"one","two":2}
# print(dic1)    #  {'fruit': 'banana', 'animal': 'monkey', 1: 'one', 'two': 2}


# print(dic1.keys())  # dict_keys(['fruit', 'animal', 1, 'two'])
# print(dic1.values())  # dict_values(['banana', 'monkey', 'one', 2])
# print(dic1.items()) # dict_items([('fruit', 'banana'), ('animal', 'monkey'), (1, 'one'), ('two', 2)])


# print(dic1["fruit"])  # banana
# print(dic1.get("fruit")) # banana

# print(dic1["three"])  #KeyError: 'three'
# print(dic1.get("three"))  #None

# print(dir(dic1))

# 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values'

#dic1.clear()
#print(dic1)  #{}


# dic1["three"]=3

# print(dic1) #Adding a value 
# #{'fruit': 'banana', 'animal': 'monkey', 1: 'one', 'two': 2, 'three': 3}

# dic1["three"]=56

# print(dic1)  
# #{'fruit': 'banana', 'animal': 'monkey', 1: 'one', 'two': 2, 'three': 56}  #For same key updates

#copy

# dic2=dic1
# print(id(dic1),id(dic2))

# #2122890898384 2122890898384

# dic3=dic1.copy()
# print(id(dic1),id(dic3))   

# # 2717727419344 2717727419416


# new_dic1={"four":4}

# dic1.update(new_dic1)
# print(dic1)

#{'fruit': 'banana', 'animal': 'monkey', 1: 'one', 'two': 2, 'four': 4}


############pop

# print(dic1)
# #{'fruit': 'banana', 'animal': 'monkey', 1: 'one', 'two': 2}

# dic1.pop("two")
# print(dic1)
# #{'fruit': 'banana', 'animal': 'monkey', 1: 'one'}

######  popitem ###########################

# print(dic1)

# #{'fruit': 'banana', 'animal': 'monkey', 1: 'one', 'two': 2}
# print(dic1.popitem())
# #('two', 2)
# print(dic1)
# #  {'fruit': 'banana', 'animal': 'monkey', 1: 'one'}


# from_keys

# keys={"a","e","i","o","u"}

# dic2=dic1.fromkeys(keys)
# print(dic2)

# #{'a': None, 'i': None, 'u': None, 'o': None, 'e': None}

# dic2["a"]="Apple"

# print(dic2)
# #{'a': 'Apple', 'i': None, 'e': None, 'u': None, 'o': None}


########### Set Default


# dic1={}

# dic1.setdefault("k",45)
# print(dic1)

# # {'k': 45}

# dic1.setdefault("m",46)
# print(dic1)

# #{'k': 45, 'm': 46} -- new value will be added 


# dic1.setdefault("k",47)  # any value present with "K" will not added
# print(dic1)

# #{'k': 45, 'm': 46}

#Dictonary now same ordered 

dic1={"fruit":"banana",'animal':"monkey",1:"one","two":2}
print(dic1)
    
#{'fruit': 'banana', 'animal': 'monkey', 1: 'one', 'two': 2} --> Order is same



















