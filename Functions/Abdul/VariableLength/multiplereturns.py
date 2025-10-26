def fun(a,b,c):
    sum=a+b+c
    prod=a*b*c
    return sum,prod 

print(fun(5,10,15))
    #(30,750)
print(type(fun(5,10,15)))   
    # <class 'tuple'>

#########################################


def result(marks1,marks2,marks3):
    total=marks1+marks2+marks3
    average=total/3

    if average >= 45:
        grade="Pass"
    else:
        grade="Fail"

    return total,average,grade   

print(result(50,60,70))
#(180, 60.0, 'Pass')
         

