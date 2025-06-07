import platform 

print(platform.system()) # 'Windows'
print(f'{platform.python_version()}') # '3.7.10'
print(platform.python_version_tuple()) # (3, 7, 10)

print(platform.machine()) # AMD64
print(platform.release()) # 10

print(platform.architecture()) # ('64bit', 'WindowsPE')
print(platform.processor()) # Intel64 Family 6 Model 186 Stepping 3, GenuineIntel
print(platform.node()) # MahiManu
print(platform.uname()) # 
             # uname_result(system='Windows', node='MahiManu', release='10', version='10.0.26100', machine='AMD64', processor='Intel64 Family 6 Model 186 Stepping 3, GenuineIntel')




