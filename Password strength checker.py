import re 

def check_password_strength(password):
    strength = 0

    if len(password):
        strength += 1
    if re.search("[a-z]", password)and re.search("[A-Z]", password):
        strength += 1
    if re.search("[0-9]", password):
        strength += 1
    if re.search("[@#$%^&+=*!]", password):
        strength += 1
    
    if strength == 4:
        return "Strong Password"
    elif strength == 3:
        return "Medium Password"
    else:
        return "Weak Password"

password = input("Enter your password: ")
result = check_password_strength(password)
print(result)