import os 
import sys 
import datetime 
age=0

# req_path=input("Enter your the path ")
# if os.path.exists(req_path):
#     print("The path exists")
#     if(os.path.isfile(req_path)):
#         print("The path is a file")
#         sys.exit(1)
#     else:
#         # print("The path is a valid directory")
#         d_f=os.listdir(req_path)
            
# else:
#     print("Pleae provide a valid path")
#     sys.exit(2)   
# today=datetime.datetime.now()

# for each in d_f:
#     d_g=os.path.join(req_path,each)
#     if os.path.isfile(d_g):
#         # print(os.path.getctime(d_g))
#         cre_date=datetime.datetime.fromtimestamp(os.path.getctime(d_g))
#         diff_days=(today-cre_date).days
#         print(diff_days)
#         if diff_days >= age:
#             print(each,diff_days)

path=input("Enter the directory path:")
age=1

if os.path.exists(path):
    if os.path.isfile(path):
        print("Its a file path...")
        sys.exit(0)
    else:
        print(f"Dir path {path}")
        d_f=os.listdir(path)    
else:
    print("Path does not exists...")
    sys.exit(0)    

today=datetime.datetime.now()    

for each in d_f:
    d_g=os.path.join(path,each)
    if os.path.isfile(d_g):
        ctime=os.path.getctime(d_g)
        ctime_d=datetime.datetime.fromtimestamp(ctime)
        diff_days=(today-ctime_d).days
        if(diff_days >= age):
            print(each,diff_days)


        












 