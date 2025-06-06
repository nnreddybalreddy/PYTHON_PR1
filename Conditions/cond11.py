import os 

t_w=os.get_terminal_size().columns
usr_str=input("Enter a string: ")
usr_conf=input("Please enter yes / no: ")

if usr_conf=="yes":
    print(usr_str.center(t_w).title())
    print(usr_str.ljust(t_w).title())
    print(usr_str.rjust(t_w).title())