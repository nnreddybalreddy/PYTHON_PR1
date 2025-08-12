# #!/bin/python
# import os 

# def get_details_for_each_tomcat(server_xml):
#     global tcf,th
#     tcf=server_xml
#     th=os.path.dirname(os.path.dirname(server_xml))
#     return None 

# def display_details():
#     print(f'The configuration file:{tcf}\n The th home:::{th}')
#     return None

# def main():
#     tomcat7="/home/Automation/tomcat7/conf/server.xml"
#     tomcat9="/home/Automation/tomcat9/conf/server.xml"  
#     get_details_for_each_tomcat(tomcat7)
#     get_details_for_each_tomcat(tomcat9)
#     display_details()
#     display_details()
#     return None 

      

# if __name__=="__main__":
#     main()

######## 2
#!/bin/python
import os 

class Tomcat():
    def get_details_for_each_tomcat(self,server_xml):
        self.tcf=server_xml
        self.th=os.path.dirname(os.path.dirname(server_xml))
        return None 

    def display_details(self):
        print(f'The configuration file:{self.tcf}\n The th home:::{self.th}')
        return None        




def main():

    tomcat7=Tomcat()
    tomcat9=Tomcat()

    tomcat7.get_details_for_each_tomcat("/home/Automation/tomcat7/conf/server.xml")
    tomcat9.get_details_for_each_tomcat("/home/Automation/tomcat9/conf/server.xml")    
    tomcat7.display_details()
    tomcat9.display_details()
    tomcat9.display_details()
    tomcat7.display_details()
    print(tomcat7.tcf) 
    print(tomcat9.tcf)


if __name__=="__main__":
    main()