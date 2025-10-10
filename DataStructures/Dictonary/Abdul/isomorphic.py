str1,str2="paper","title"

flag = True

if len(str1) != len(str2):
    flag = False
else:
    map1, map2 = {}, {}
    
    # TODO: Loop through zip(str1, str2) and check Forward and Backward mappings with proper indentation below
    for c1,c2 in zip(str1,str2):
        if c1 in map1:
            if map1[c1]!=c2:
                flag=False
                break
        else:
            map1[c1]=c2
        
        if c2 in map2:
            if map2[c2]!=c1:
                flag=False
                break
        else:
             map2[c2]=c1
print(map1)
print(map2)
            


if flag!=False:
    print("ismorphic")
else:
    print("Not morphic")
#ismorphic    


                 