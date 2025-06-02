# dic1={}
# print(dic1,bool(dic1))

dic1={"fruit":"banana",'animal':"monkey",1:"one","two":2}

# print(dic1.keys())
# print(dic1.items())
# print(dic1.values())

# dic1["fruit"]="Apple"

# print(dir(dic1))

#'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']

# dic1.clear()
# print(dic1)

# print(dic1.get("fruit")) # banana
# print(dic1.get("Fruit"))  #None

keys={"a","e","i","o","u"}

dic2=dic1.fromkeys(keys)
print(dic2)

dic2["a"]="Apple"
print(dic2)







