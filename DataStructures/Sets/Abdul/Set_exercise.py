# #Scrambled words
word_set={"plea","medical","listen","leap","decimal","silent","pale","enlist"}

print(sorted("plea"))
print(sorted("leap"))
#['a', 'e', 'l', 'p']
#['a', 'e', 'l', 'p']


result=set()
print("scrambed word pairs are:")

for word1 in word_set:
    for word2 in word_set:
        if word1!=word2 and sorted(word1)==sorted(word2):
            pair=tuple(sorted((word1,word2)))

# ('pale', 'plea')
#('leap', 'plea')
#('enlist', 'listen')
#('listen', 'silent')
#('enlist', 'listen')
#('enlist', 'silent')
#('decimal', 'medical')
#('pale', 'plea')
#('leap', 'pale')
#('decimal', 'medical')
#('leap', 'plea')
#('leap', 'pale')
#('listen', 'silent')
#('enlist', 'silent')
            
            result.add(pair)
            # print(result)
#{('leap', 'pale')}
#{('leap', 'pale'), ('leap', 'plea')}
#{('leap', 'pale'), ('enlist', 'listen'), ('leap', 'plea')}
#{('leap', 'pale'), ('enlist', 'listen'), ('listen', 'silent'), ('leap', 'plea')}
#{('leap', 'pale'), ('enlist', 'listen'), ('listen', 'silent'), ('leap', 'plea')}
#{('leap', 'pale'), ('pale', 'plea'), ('enlist', 'listen'), ('listen', 'silent'), ('leap', 'plea')}
#{('leap', 'pale'), ('pale', 'plea'), ('enlist', 'listen'), ('listen', 'silent'), ('leap', 'plea')}
#{('leap', 'pale'), ('pale', 'plea'), ('enlist', 'listen'), ('enlist', 'silent'), ('listen', 'silent'), ('leap', 'plea')}
#{('leap', 'pale'), ('pale', 'plea'), ('enlist', 'listen'), ('decimal', 'medical'), ('enlist', 'silent'), ('listen', 'silent'), ('leap', 'plea')}
#{('leap', 'pale'), ('pale', 'plea'), ('enlist', 'listen'), ('decimal', 'medical'), ('enlist', 'silent'), ('listen', 'silent'), ('leap', 'plea')}
#{('leap', 'pale'), ('pale', 'plea'), ('enlist', 'listen'), ('decimal', 'medical'), ('enlist', 'silent'), ('listen', 'silent'), ('leap', 'plea')}
#{('leap', 'pale'), ('pale', 'plea'), ('enlist', 'listen'), ('decimal', 'medical'), ('enlist', 'silent'), ('listen', 'silent'), ('leap', 'plea')}
#{('leap', 'pale'), ('pale', 'plea'), ('enlist', 'listen'), ('decimal', 'medical'), ('enlist', 'silent'), ('listen', 'silent'), ('leap', 'plea')}
#
# {('leap', 'pale'), ('pale', 'plea'), ('enlist', 'listen'), ('decimal', 'medical'), ('enlist', 'silent'), ('listen', 'silent'), ('leap', 'plea')}
for pair in result:
    print(pair)


#scrambed word pairs are:
# ('decimal', 'medical')
# ('pale', 'plea')
# ('enlist', 'listen')
# ('enlist', 'silent')
# ('listen', 'silent')
# ('leap', 'pale')
# ('leap', 'plea')

##### Plagiarism check

# import re

# str1 = ('Time is the most valuable thing we have,'
#         ' and once lost, it never returns.')

# str2 = ("We never get time back once it's "
#     "gone—it's truly the most valuable resource.")

# words1 = re.findall(r'\w+', str1.lower())

# words2 = re.findall(r'\w+', str2.lower())

# wset1 = set(words1)
# wset2 = set(words2)

# common = wset1 & wset2
# unique = wset1 | wset2

# ratio = len(common) / len(unique)

# print(f"Jaccard Similarity:{ratio:.2f}")


            

