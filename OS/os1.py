import os

print(os.sep) #  /
print("C:\\SEQ\\PYTHON_PR\\OS\\Test")  # C:\SEQ\PYTHON_PR\OS\Test

path = "C:\\SEQ\\PYTHON_PR\\OS\\Test"

os.chdir(path)

# print(os.getcwd())  # C:\SEQ\PYTHON_PR\OS\Test 
# print(os.listdir())   # []

# print(os.getcwd())  # C:\SEQ\PYTHON_PR\OS\Test

# os.mkdir("Test1")
# print(os.listdir())   # ['Test1']

# os.makedirs("Test2\\Test3")
# print(os.listdir())   # ['Test1', 'Test2']

# os.removedirs("Test2\\Test3")

# print(os.listdir())   # ['Test1']

# print(os.listdir())   # ['Test1']

# os.rmdir("Test1")
# print(os.listdir())   # []

# os.mkdir("Test2")
# os.mkdir("Test3")

# os.rename("Test2", "Test4")
# print(os.listdir())   # ['Test3', 'Test4']

print(os.environ)  # {'...': '...', ...}




















