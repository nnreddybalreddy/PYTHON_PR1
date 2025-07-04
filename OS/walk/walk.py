import os

path="C:\\SEQ\\PYTHON_PR\\OS\\walk_test"

#[('C:\\SEQ\\PYTHON_PR\\OS\\walk_test', ['Hello', 'Hello1'], ['1.txt', '2.txt', '3.txt']), 
#('C:\\SEQ\\PYTHON_PR\\OS\\walk_test\\Hello', [], ['4.txt', '5.txt', '6.txt']),
# ('C:\\SEQ\\PYTHON_PR\\OS\\walk_test\\Hello1', [], ['7.txt', '8.txt'])]


# for each in list(os.walk(path)):
#     print(each)

# ('C:\\SEQ\\PYTHON_PR\\OS\\walk_test', ['Hello', 'Hello1'], ['1.txt', '2.txt', '3.txt'])
# ('C:\\SEQ\\PYTHON_PR\\OS\\walk_test\\Hello', [], ['4.txt', '5.txt', '6.txt'])
# ('C:\\SEQ\\PYTHON_PR\\OS\\walk_test\\Hello1', [], ['7.txt', '8.txt'])


# for each in os.walk(path):
#     print(each)

#('C:\\SEQ\\PYTHON_PR\\OS\\walk_test', ['Hello', 'Hello1'], ['1.txt', '2.txt', '3.txt'])
#('C:\\SEQ\\PYTHON_PR\\OS\\walk_test\\Hello', [], ['4.txt', '5.txt', '6.txt'])
#('C:\\SEQ\\PYTHON_PR\\OS\\walk_test\\Hello1', [], ['7.txt', '8.txt'])


# tpl1=(1,2,3)
# x,y,z=tpl1 

# print(x,y,z) #Unpacking  # 1 2 3


# for r,d,f in os.walk(path):
#     print(r,d,f)


#C:\SEQ\PYTHON_PR\OS\walk_test ['Hello', 'Hello1'] ['1.txt', '2.txt', '3.txt']
#C:\SEQ\PYTHON_PR\OS\walk_test\Hello [] ['4.txt', '5.txt', '6.txt']
#C:\SEQ\PYTHON_PR\OS\walk_test\Hello1 [] ['7.txt', '8.txt']

# for r,d,f in os.walk(path):
#     print(r,f)

#C:\SEQ\PYTHON_PR\OS\walk_test ['1.txt', '2.txt', '3.txt']
#C:\SEQ\PYTHON_PR\OS\walk_test\Hello ['4.txt', '5.txt', '6.txt']
# C:\SEQ\PYTHON_PR\OS\walk_test\Hello1 ['7.txt', '8.txt']



# REmove 7.txt and 8.txt and run


# for r,d,f in os.walk(path):
#     if len(f)!=0:
#         print(r,f)

#C:\SEQ\PYTHON_PR\OS\walk_test ['1.txt', '2.txt', '3.txt']
#C:\SEQ\PYTHON_PR\OS\walk_test\Hello ['4.txt', '5.txt', '6.txt']   

for r,d,f in os.walk(path):
    if len(f)!=0:
        print(r)
        for each_file in f:
            print(os.path.join(r,each_file))
        print("...............")    

#C:\SEQ\PYTHON_PR\OS\walk_test
#C:\SEQ\PYTHON_PR\OS\walk_test\1.txt
#C:\SEQ\PYTHON_PR\OS\walk_test\2.txt
#C:\SEQ\PYTHON_PR\OS\walk_test\3.txt
...............
#C:\SEQ\PYTHON_PR\OS\walk_test\Hello
#C:\SEQ\PYTHON_PR\OS\walk_test\Hello\4.txt
#C:\SEQ\PYTHON_PR\OS\walk_test\Hello\5.txt
#C:\SEQ\PYTHON_PR\OS\walk_test\Hello\6.txt






