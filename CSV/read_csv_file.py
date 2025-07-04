# import csv 
# import os 

# req_file="C:\\SEQ\\PYTHON_PR\\CSV\\new_info2.json"

# print(os.path.exists(req_file))

# fo=open(req_file,"r")

# content=csv.reader(fo,delimiter="|")
# for each in content:
# 	print(each)

# fo.close()

import csv 
import os 

req_file="C:\\SEQ\\PYTHON_PR\\CSV\\new_info2.json"

fo=open(req_file,"r")
content=csv.reader(fo,delimiter="|")

for each in content:
	print(each)

fo.close()




