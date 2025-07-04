# #read a path and identify all files and directory
# import os
# path=input("Enter the path:")

# if os.path.exists(path):
#     print(f"{path} exists")
#     df_l=os.listdir(path)
# else:
#     print(f"{path} does not exist")
#     exit(1)

# for each in df_l:
#     f_d=os.path.join(path,each)
#     if os.path.isfile(f_d):
#         print(f"{f_d} is a file")
#     elif os.path.isdir(f_d):
#         print(f"{f_d} is a directory")
#     else:
#         print(f"{f_d} is neither a file nor a directory")  # This case is unlikely but included for completeness

import os 
import sys

path=input("Enter the path: ")
if os.path.exists(path):
    print(f"{path} exists")
    df_l=os.listdir(path)
    if len(df_l) == 0:
        print(f"{path} is empty")
        exit(0)
    else:
        for each in df_l:
            f_d=os.path.join(path,each)
            if os.path.isfile(f_d):
                print(f"{f_d} is a file")
            elif os.path.isdir(f_d):
                print(f"{f_d} is a directory")
            else:
                print(f"{f_d} is neither a file nor a directory")
            
else:    
    print(f"{path} does not exist")
    exit(1)


