import getpass
# db_password = getpass.getpass() # this will not echo the password to the console
# print(f'{db_password}')


# db_password = getpass.getpass(prompt='Enter your database password: ')  # this will not echo the password to the console
# print(f'{db_password}')  # this will print the password to the console, but it is not recommended to do so in production code

# db_password=getpass.getpass("Enter you db password: ")  # this will not echo the password to the console
# print(db_password)


print(getpass.getuser())  # naren

#$ env | grep USERNAME
#USERNAME=naren
