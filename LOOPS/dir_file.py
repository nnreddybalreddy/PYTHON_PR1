# Read a path and check if it is a file or directory
import os 
import sys 

path=input("Enter a path:")

if os.path.exists(path):
    if os.path.isfile(path):
        print(f"{path} is a file")
    else:
        print(f"{path} is a directory")
else:
    print(f"{path} does not exist")
    sys.exit(1) 
                


           
