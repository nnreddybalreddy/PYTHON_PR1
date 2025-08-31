password1=input("Enter password1::")
password2=input("Enter password2::::")

if password1 == password2:
    print("Password changed")
else:
    if password1.casefold()==password2.casefold():
        print("Please try aain with casefold...")
    else:
        print("Password are not same")        
