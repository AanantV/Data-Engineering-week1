import re

def email_val():
    mail = str(input("Enter your Email address: "))

    mail_split = re.split(r"[@.]", mail)
    print(mail_split[0])

    at_index = mail.find("@")
    dot_index = mail.find(".")

    if ("@" and ".") in mail and len(mail_split[0]) >=6 and dot_index > at_index:
        print(f"Your email {mail} is valid")
    else:
        print(f"Your email {mail} is invalid because it didn't follow the criteria")

email_val()