import re

def password_check(password):

    # calculating the length
    length_error = len(password) < 8

    # searching for digits
    digit_number = re.findall(r"\d", password) 
    digit_error = True if len(digit_number) < 2 else False

    # searching for symbols
    symbol_number = re.findall(r"[ !@#$%&* ]", password)
    symbol_error =  True if len(symbol_number) < 2 else False

    # overall result
    password_ok = not ( length_error or digit_error or symbol_error )

    if password_ok:
        return "Strong"
    else:
        return "Weak"

print(password_check(input()))
