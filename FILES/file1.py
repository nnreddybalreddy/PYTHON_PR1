#code 1
# fd=open("filedemo","w")
# print(fd.readable()) # Fase
# print(fd.writable()) # True

# fd.close()

# fd=open("random.txt","w")
# # fd.write("This is the first line")
# # fd.write("This is the second line")
# # #This is the first lineThis is the second line
# fd.close()


#code 2

#fd=open("random.txt","w")
#fd.write("This is the 3rd line \n")
#fd.write("This si the 4th line \n")
#fd.write("This is the 5th line")
#fd.close()

#This is the 3rd line 
#This si the 4th line 
#This is the 5th line


#code 3
#OVERWRITE

# fd=open("random.txt","w")
# fd.write("This is the 6th line \n")
# fd.write("This si the 7th line \n")
# fd.write("This is the 8th line")
# fd.close()

# This is the 6th line 
# This si the 7th line 
# This is the 8th line

# fd.write("This is the 9th line \n")
# fd.write("This si the 10th line \n")
# fd.write("This is the 11th line")
# fd.close()

# #This is the 9th line 
# #This si the 10th line 
# #This is the 11th line

# # Previous data 6th , 7th , 8th line overwritten by 9th ,10th,11th


### code 4
# my_content=["This is data 1\n","This is data line 2\n","This is data line 3\n"]

# fd=open("random.txt",'w')

# fd.writelines(my_content)
# fd.close()

#This is data 1
#This is data line 2
#This is data line 3


# code 5
# my_content=["Loop 1","Loop 2","Loop 3"]

# # for each in my_content:
# #     print(each+"\n")

#  # Loop 1
#  # Loop 2
#  # Loop 3



# CODE 6
# fd=open("with_loop.txt","w")

# for each in my_content:
#     fd.write(each+"\n")
# fd.close()    

# # Loop 1
# # Loop 2
# # Loop 3

# my_content=["Loop 1","Loop 2","Loop 3"]
# fd=open("with_loop.txt","a")

# for each in my_content:
#     fd.write(each+"\n")
# fd.close()  

#Loop 1
#Loop 2
#Loop 3
#Loop 1
#Loop 2
#Loop 3


#CODE 7
#read 
# fd=open("with_loop.txt","r")

# print(fd.read())

# fd.close()

# #Loop 1
# #Loop 2
# #Loop 3
# #Loop 1
# #Loop 2
# #Loop 3


#CODE 8

# fd=open("with_loop.txt","r")

# print(fd.readline())
# Loop 1

# CODE 9 --> Into a list 


fd=open("with_loop.txt","r")
data=fd.readlines()
fd.close()

# print(data)
#['Loop 1\n', 'Loop 2\n', 'Loop 3\n', 'Loop 1\n', 'Loop 2\n', 'Loop 3\n']


# for each in range(3):
#     print(data[each]) #data[0]

#Loop 1
#Loop 2
#Loop 3


print(data[-1]) #Loop 3
















