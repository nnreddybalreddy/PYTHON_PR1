import os

print(os.path.sep)  # /


path= "C:\\SEQ\\PYTHON_PR\\OS\\Test\\1.py"
print(os.path.dirname(path))  # C:\SEQ\PYTHON_PR\OS\Test
print(os.path.basename(path))  # 1.py


path1="C:\\SEQ\\PYTHON_PR\\OS\\Test"
path2="2.py"

print(os.path.join(path1,path2)) #C:\SEQ\PYTHON_PR\OS\Test\2.py


print(os.path.split(path)) # ('C:\\SEQ\\PYTHON_PR\\OS\\Test', '1.py')

print(os.path.getsize(path)) #25


print(os.path.exists(path)) #True


