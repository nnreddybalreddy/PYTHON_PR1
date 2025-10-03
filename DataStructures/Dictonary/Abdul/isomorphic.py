str1="abccbab"
#str2="gmssmgp"
str2="abccbab"


j=0

flag=True 

if len(str1) != len(str2):
    flag=False 
else:
    map1,map2={},{}
    for c1,c2 in zip(str1,str2):
        if c1 in map1:
            if map1[c1]!=c2:
                flag=False
        else:
            map1[c1]=c2 

        if c2 in map2:
            if map[c2]!=c1:
                flag=False
            else:
                map2[c2]=c1

if flag!=False:
    print("ismorphic")
else:
    print("Not morphic")


                 