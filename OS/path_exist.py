import os 

path="C:\\SEQ\\PYTHON_PR\\OS\\Test\\1.pyc"

# print(os.path.basename(path)) #1.py
# print(os.path.dirname(path))  #C:\SEQ\PYTHON_PR\OS\Test

# if os.path.exists(path):
#     print(f"{path} exists")  #C:\SEQ\PYTHON_PR\OS\Test\1.py exists
# else:
#     print(f"{path} not exists")    

# if os.path.isfile(path):
#     print(f'{path} is a file')
# else:
#     print(f'{path} is not file')    # C:\SEQ\PYTHON_PR\OS\Test\1.pyc is a file 

path="C:\\SEQ\\PYTHON_PR\\OS\\Test"

if os.path.isdir(path):
    print(f'{path} dir exists') # C:\SEQ\PYTHON_PR\OS\Test dir exists
else:
    print(f'{path} dir no exists')    
