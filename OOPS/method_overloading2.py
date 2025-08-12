class India():
    def capital(self):
        print("New Delhi")
    def language(self):
        print("Hindi , English")


class USA():
    def capital(self):
        print("Washingon DC")
    def language(self):
        print("English")   
        
        
obj_India=India()
obj_USA=USA()

for country in(obj_India,obj_USA): #Methods classes
    country.capital()     #New Delhi  Hindi , English
    country.language()    # Washingon DC    English . Methods classes overloading