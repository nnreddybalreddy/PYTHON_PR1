import csv 
import os 

req_file="C:\\SEQ\\PYTHON_PR\\CSV\\new_info.csv"

fp=open(req_file,"r")

content=csv.reader(fp,delimiter="|")

head=next(content)
print(f'header:{head}')
for each in content:
    print(each)

fp.close()


req_file="C:\\SEQ\\PYTHON_PR\\CSV\\demo.csv"
fo=open(req_file,'w',newline="")


csv_writer=csv.writer(fo,delimiter=",")


# csv_writer.writerow(['S_No',"Name",'Age'])
# csv_writer.writerow([1,"John",24])
# csv_writer.writerow([2,"Cliton",25])

my_data=[['S_No',"Name",'Age'],[1,"John",23],[2,"Cliton",24]]
csv_writer.writerows(my_data)

fo.close()



