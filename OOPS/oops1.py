class computer:
    color="Black"

    def __init__(self,computer,ram,cpu):
        self.computer=computer 
        self.ram=ram
        self.cpu=cpu 

    def description(self,hd):
        print("com config: com Name:",self.computer,"CPU :",self.cpu,"RAM::",self.ram)
        print('Hard Disk:',hd)  #Instance method. so not to use self.   


c1=computer('Dell',8,'I7')  # Object creation
c2=computer("Lenova",16,'I5') #Object creation     

print("Before------------")
print("c1 attributes:",c1.computer,c1.ram,c1.cpu) # Dell 8 17
print("c2 attributes:",c2.computer,c2.ram,c2.cpu) # Lenova,16 I5


print("After-------------------")
c1.computer="Inspiron"
c2.ram=24

print("c1 attributes:",c1.computer,c1.ram,c1.cpu)  #Inspiron 8 17 
print("c2 attributes:",c2.computer,c2.ram,c2.cpu)  #Lenova,24,I5


c1.description(500)   #Com Config: Com Name: Inspiron Ram size: 8 cpu: I7  ard Disk: 500
c2.description(1000)  #Com Config: Com Name: Lenova Ram size: 24 cpu: I5 and Hard Disk: 1000
















