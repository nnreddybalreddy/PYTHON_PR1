import sys 
#usr_str=input("Enter a string: ")
#usr_action=input("Enter an action: lower/upper/title:")

#if usr_action == "lower":
#    print(usr_str.lower())
#elif usr_action == "upper":    
#    print(usr_str.upper())
#elif usr_action == "title":
#    print(usr_str.title())  
#else:
#    print("Invalid action. Please enter lower, upper, or title::::")

# if len(sys.argv) != 3:
#     print("Usage: python sys_argv.py <string> <action>")
#     sys.exit(1)

# usr_str=sys.argv[1]
# usr_action=sys.argv[2]

# if usr_action == "lower":
#     print(usr_str.lower())
# elif usr_action == "upper":    
#     print(usr_str.upper())
# elif usr_action == "title":
#     print(usr_str.title())  
# else:
#     print("Invalid action. Please enter lower, upper, or title::::")


# usr_str=input("Enter a string: ")
# usr_action=input("Enter an action: lower/upper/title:")

if len(sys.argv) != 3:
    print("Usage: python sys_argv.py <string> <action>")
    sys.exit(1)
    
usr_str=sys.argv[1]
usr_action=sys.argv[2]


if usr_action == "lower":
    print(usr_str.lower())  
elif usr_action == "upper":
    print(usr_str.upper())
elif usr_action == "title":
    print(usr_str.title())
else:              
    print("Invalid action. Please enter lower, upper, or title::::")        
    
