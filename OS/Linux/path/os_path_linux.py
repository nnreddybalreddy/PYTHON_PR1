import os

path="/home/ec2-user/a.py"
print(os.sep) # /

print(os.path.dirname(path)) #/home/ec2-user
print(os.path.basename(path)) #a.py


path1="/home/ec2-user"
path2="b.py"

print(os.path.join(path1,path2)) #('/home/ec2-user/b.py
print(os.path.split(path)) #('/home/ec2-user','a.py')

print(os.path.getsize(path)) #0
