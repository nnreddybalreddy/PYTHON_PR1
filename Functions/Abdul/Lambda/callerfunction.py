#Caller Class
    # like Closure function
#Need function
#Return function inner function
#Inner function access outer variabels

class Day:
    def __init__(self):
        self.days={1:"Monday",2:"Tuesday",3:"Wednesday",
                   4:"Thursday",5:"Friday",6:"Saturday",7:"Sunday"}

    def __call__(self,dayno):   
        return self.days[dayno]


d=Day()
print(d(3))
# Wednesday

######### The object of the class is treated as function

# The class which has _call_ method is called caller class

        