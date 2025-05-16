import os
size=os.get_terminal_size().columns
print(size)
  # 80
given_string=input("Enter your string::")
 

print(given_string.center(size).title())
print(given_string.ljust(size).title())
print(given_string.rjust(size).title())
#                     Python Programming
#Python Programming
#                                               Python Programming


#80
#Enter your string::Python programming
#                               Python Programming
#Python Programming
#                                                              Python Programming


