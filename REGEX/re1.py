import re
my_str="Python is simple and it is easy"
print(my_str.split("is"))
# ['Python ', ' simple and it ', ' easy']

print(my_str.split("it"))
#['Python is simple and ', ' is easy']

print(re.split("i[st]",my_str))
#['Python ', ' simple and ', ' ', ' easy']
