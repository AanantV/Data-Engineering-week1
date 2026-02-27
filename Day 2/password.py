import re

def password():
    password = str(input("Enter your password: "))
    pass_len = len(password)

    upper_check = re.search(r"[A-Z]", password)
    lower_check = re.search(r"[a-z]", password)
    digit_check = re.search(r"[0-9]", password)

    special_check = re.search(r"[^a-zA-Z0-9]", password)

    if (upper_check and lower_check and digit_check and special_check and (len(password) >=8)):
        print("Your password is strong")
    elif((upper_check and lower_check and digit_check and (len(password) >=8)) or (upper_check and lower_check and special_check and (len(password) >=8))):
        print("Your password is medium")
    else:
        print("Your password is weak")

password()