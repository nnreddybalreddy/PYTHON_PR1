class NegativeError(Exception):
    #pass
    def __init__(self,msg):
        self.msg=msg

    def __str__(self):
        return self.msg     


def area(length,breadth):
    if length>=0 and breadth >=0:
        a=length * breadth 
        return a
    else:
        raise NegativeError("-ve Dimention")

print(area(-5,-3))     

########
#######
#######
#
# $ python userdefined.py
# Traceback (most recent call last):
#  File "C:\NNR\PYTHON_PR1\EXCEPTION\Abdul_2\userdefined.py", line 12, in <module>
#    area(-5,-3)
#    ~~~~^^^^^^^
#  File "C:\NNR\PYTHON_PR1\EXCEPTION\Abdul_2\userdefined.py", line 10, in area
#    raise NegativeError("-ve dimention")
# NegativeError: -ve dimention
#





