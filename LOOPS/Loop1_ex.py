# path=input("Enter a path: " )
# import os

# if os.path.exists(path):
#     dl_l=os.listdir(path)
# else:
#     print(f"{path} does not exist")
#     exit(1)

# for each in dl_l:
#     f_d=os.path.join(path, each)
#     if os.path.isfile(f_d):
#         print(f"{f_d} is a file")
#     elif os.path.isdir(f_d):
#         print(f"{f_d} is a directory")
#     else:
#         print(f"{f_d} is neither a file nor a directory")  # This case is unlikely but included for completeness

import os 
path=input("Enter a path: ")

if os.path.exists(path):
    dl_l=os.listdir(path)
else:
    print(f"{path} does not exist")
    exit(1)

for each in dl_l:
    f_d=os.path.join(path,each)
    if os.path.isfile(f_d):
        print(f"{f_d} is a file")
    elif os.path.isdir(f_d):
        print(f"{f_d} is a directory")
    else:
        print(f"{f_d} is neither a file nor a directory")  # This case is unlikely but included for completeness