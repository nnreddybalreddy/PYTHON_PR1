class WeakPasswordError(Exception):
    pass 

def is_strong(password):
    msg="Password msut contain at least"

    if len(password) < 0:
        return False,msg + " 8 characters"

    has_upper=any(c.isupper() for c in password) 
    has_lower=any(c.islower() for c in password)
    has_digit=any(c.isdigit() for c in password)
    special_chars=set("!@#$%^&*()_+=")
    has_speical=any(c in special_chars for c in password)

    if not has_upper:
        raise WeakPasswordError(msg +  "one upper char")
    
    if not has_lower:
        return False,msg + "One lower letter"
    
    if not has_digit:
        return False,msg + "One digit" 

    if not has_speical:
        return False,msg + "One special"  

    return True, "Password is strong" 


try:
    pwd = is_strong("admin#123Net")
except WeakPasswordError as e:
    print(e)   
else:
    print(pwd)
finally:
    print("Finally")           
    

