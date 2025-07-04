# import os
# import sys
# path=input("enter a path:   ")
# extension=input("Enter the extension to search for (e.g., .txt): ")

# if os.path.exists(path):
#     print(f"{path} exists")
#     if os.path.isdir(path):
#         print(f"{path} is a directory")
#         d_f=os.listdir(path)
#         if len(d_f) == 0:
#             print(f"{path} is empty")
#             exit(0)
#         for i in d_f:
#             if i.endswith(extension):
#                 print(i)
# else:
#     print(f"{path} does not exist")
#     exit(1)        

# import os 
# import sys 
# path=input("Enter a path: ")
# extension=input("Enter the extension to search for (e.g., .txt): ")

# if os.path.exists(path):
#     print(f"{path} exists")
#     if os.path.isdir(path):
#         print(f"{path} is a directory")
#         d_f=os.listdir(path)
#         if len(d_f) == 0:
#             print(f"{path} is empty")
#             exit(0)
#         for each in d_f:
#             if each.endswith(extension):
#                 print(each)
# else:
#     print(f"{path} does not exist")
#     exit(1)       


import os 
import sys 

path = input("Enter a path: ")
extension = input("Enter the extension to search for (e.g., .txt): ")


if os.path.exists(path):
    print(f"{path} exists")
    if os.path.isdir(path):
        print(f"{path} is a directory")
        d_f = os.listdir(path)
        if len(d_f) == 0:
            print(f"{path} is empty")
            exit(0)
        else:
            for each in d_f:
                if each.endswith(extension):
                    print(each)



    
    
