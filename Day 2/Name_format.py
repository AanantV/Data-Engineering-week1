def name_format():

    first_name = str(input("Enter your first name: "))
    last_name = str(input("Enter your last name: "))

    full_name = first_name + " " + last_name
    print(f"Your full name is {full_name}")

    FN_upper = full_name.upper()
    print(f"Your full name in upper case is {FN_upper}")

    FN_lower = full_name.lower()
    print(f"Your full name in lowercase is {FN_lower}")

    FN_title = full_name.title()
    print(f"Your full Name in title case is {FN_title}")

    cap_LN = last_name.capitalize()
    cap_FN = first_name.capitalize()
    indexed = cap_FN[0] + '.' + cap_LN[0]
    print(f"Your name in initialised format is {indexed}")

name_format()

