class Tomcat(object):
    def __init__(self,home,version):
        self.home=home 
        self.version=version
        return None 

    def display(self):
        print("This is from  tomcat class.....")
        print(self.home)
        print(self.version)
        return None 

class Apache(object):
    def __init__(self,home,version):
        self.home=home 
        self.version=version
        return None 

    def display(self):
        print("This is from  Apache class.....")
        print(self.home)
        print(self.version)
        return None 

tomcat_obj=Tomcat("/home/tomcat9","7.6")
apache_obj=Apache("/etc/httpd","2.4")

tomcat_obj.display()
apache_obj.display()

        
