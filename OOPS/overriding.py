class Table:
    def __init__(self,fare):
        self.fare=fare

    def __add__(self,other1):
        #return self.fare + other1.fare #110
        return self.fare *  other1.fare #3000. We can have our own logic for operator

    def __lt__(self,other):
        return self.fare < other.fare

t1=Table(50)
t2=Table(60)


print("Addition:",t1+t2)
print("Real meaning:",3+4)
print("Operator comparision:",t1<t2) #TRUE
#print("Operator comparision:",t1<=t2) #TRUE.TypeError: '<=' not supported between instances of 'Table' and 'Table'
        
