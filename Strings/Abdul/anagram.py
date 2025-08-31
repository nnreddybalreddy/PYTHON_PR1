#snooze alarms    alas,no more Z's

s1="snooze alarms"
s2="alas,no more Z's2"

# s1=s1.casefold()
# s2=s2.casefold()

# for i in s1:
#     if i.isalnum():
#         if s1.count(i) != s2.count(i):
#             print('no')
#             break
# else:
#     print("Anagram")            

s1=s1.casefold()
s2=s2.casefold()

if len(s1)!=len(s2):
    print("Not a agaram")
    exit()

for i in s1:
    if i.isalnum():
        if s1.count(i) != s2.count(i):
            print("Not a anagram")
            break
else:
    print("Anagram")    
