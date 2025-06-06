# usr_str=input("enter your string:")
# usr_conf=input("Do yes/no")

# if usr_conf=="yes":
#     print(usr_str.title())
# else:
#     print(usr_str)

usr_str = input("Enter your string: ")
usr_conf = input("Do you want to convert your string into lower case? (yes/no): ")

if usr_conf == "yes":
    print(usr_str.title())
else:
    print(usr_str)    