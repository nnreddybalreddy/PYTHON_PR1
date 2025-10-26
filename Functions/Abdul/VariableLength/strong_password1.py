
def is_strong(password):
    msg = 'Password must contain at least'
    if len(password) < 8:
        return False, msg + " 8 characters"

    has_upper=any( c.isupper() for c in password)
    has_lower=any(c.islower() for c in password)
    has_digit=any(c.isdigit() for c in password)
    special_chars = set("!@#$%^&*-_+=")
    has_special=any(c in special_chars for c in password)

    if not has_upper:
        return False, msg + " upper"
    
    if not has_lower:
        return False,msg + "lower"
    
    if not has_digit:
        return False,msg + "digit"
    
    if not has_special:
        return False,msg+ "special"
    
    return True, "Password is strong!"




password = input("Enter your password: ")
valid, message = is_strong(password)
print(message)