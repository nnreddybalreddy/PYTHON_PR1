class AgeException(Exception):
    pass 

def validate_age(age):
    if age>=10 and age<=60:
        return True 
    else:
        raise AgeException("age should be between 10-60")


name=input("Enter name:::")
age=int(input("Enter age::::"))

try:
    validate_age(age)
    print("You can join here")
except   AgeException as e:
    print(e)  