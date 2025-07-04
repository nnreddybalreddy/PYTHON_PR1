import os
# print(os.system("dir"))
# # Volume in drive C is OS
#  Volume Serial Number is 5A8C-A9C3

#  Directory of C:\SEQ\PYTHON_PR\SUBPROCESS

# 06/29/2025  07:28 PM    <DIR>          .
# 06/29/2025  07:06 PM    <DIR>          ..

# out=os.system("di r")
# print(out)  # 0

# out=os.system("dir1")
# print(out)  # 1

import subprocess
sp=subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,universal_newlines=True)
rc=sp.wait()
out,err=sp.communicate()
print(f'OUTPUT IS: {out}')
print(f'Error is: {err}')






