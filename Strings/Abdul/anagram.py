#snooze alarms    alas,no more Z's

s1="snooze alarms"
s2="alas,no more Z's"

s1=s1.casefold()
s2=s2.casefold()

# if len(s1)!=len(s2):
#     print("Not a agaram")
#     exit()

for i in s1:
    if i.isalnum():
        if s1.count(i) != s2.count(i):
            print('no')
            break
else:
    print("Anagram")       

     
# s1 = input('Enter a String')
# s2 = input('Enter second String')

# if len(s1) != len(s2):
#     print('Not Anagram')
# else:

#     for x in s1:
#         if x not in s2:
#             print('Not Anagarm2')
#             break;
#     else:
#         print('Anagram')
 

