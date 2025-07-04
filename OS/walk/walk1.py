import os

path="C:\\SEQ\\PYTHON_PR\\OS\\walk_test"

# print(list(os.walk(path)))
#[('C:\\SEQ\\PYTHON_PR\\OS\\walk_test', [], [])]

#After creating Hello1 and files 1.txt,2.txt,3.txt

# [('C:\\SEQ\\PYTHON_PR\\OS\\walk_test', ['Hello1'], ['1.txt', '2.txt', '3.txt']),
#   ('C:\\SEQ\\PYTHON_PR\\OS\\walk_test\\Hello1', [], [])]

# Hello2

#[('C:\\SEQ\\PYTHON_PR\\OS\\walk_test', ['Hello1', 'Hello2'], ['1.txt', '2.txt', '3.txt']),
# ('C:\\SEQ\\PYTHON_PR\\OS\\walk_test\\Hello1', [], ['3.txt', '4.txt', '5.txt']),
#  ('C:\\SEQ\\PYTHON_PR\\OS\\walk_test\\Hello2', [], [])]

# for r,d,f in os.walk(path):
#     print(r,d,f)

#C:\SEQ\PYTHON_PR\OS\walk_test ['Hello1', 'Hello2'] ['1.txt', '2.txt', '3.txt']
#C:\SEQ\PYTHON_PR\OS\walk_test\Hello1 [] ['3.txt', '4.txt', '5.txt']
#C:\SEQ\PYTHON_PR\OS\walk_test\Hello2 [] []


for r,d,f in os.walk(path):
    if len(f)!=0:
        print(r)
        for each_file in f:
            print(os.path.join(r,each_file))
        print("..............")    

#C:\SEQ\PYTHON_PR\OS\walk_test
#C:\SEQ\PYTHON_PR\OS\walk_test\1.txt
#C:\SEQ\PYTHON_PR\OS\walk_test\2.txt
#C:\SEQ\PYTHON_PR\OS\walk_test\3.txt
..............
#C:\SEQ\PYTHON_PR\OS\walk_test\Hello1
#C:\SEQ\PYTHON_PR\OS\walk_test\Hello1\3.txt
#C:\SEQ\PYTHON_PR\OS\walk_test\Hello1\4.txt
#C:\SEQ\PYTHON_PR\OS\walk_test\Hello1\5.txt


