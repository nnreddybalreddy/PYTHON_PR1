import os

path="/home/ec2-user/a.py"


#if os.path.exists(path):
#    print(f"{path} exists") #/home/ec2-user/a.py exists
#else:
#    print(f"{path} does not exists")


#if os.path.isfile(path):
#    print(f'{path} is a file') #/home/ec2-user/a.py is a file
#else:
#    print(f'{path} is not a file')


#if os.path.isdir(path):
#    print(f'{path} is a directory')
#else:
#    print(f'{path} is not a directory') #/home/ec2-user/a.py is not a directory



path="/home/ec2-user/c.py"

if os.path.islink(path):
    print(f"{path} is a link")# /home/ec2-user/c.py is a link
else:
    print(f"{path} is not a link")

