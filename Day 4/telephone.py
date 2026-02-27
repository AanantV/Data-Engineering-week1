def phone():

    phone_book = {}

    while True:
        print("phone book menu")
        print("1. add")
        print("2. view")
        print("3. search")
        print("4. delete")
        print("5. quit")
        key = int(input("welcome to phone directory, Enter choice 1 to 7: "))


        if key == 1:
            name = input("Enter your name: ")
            phone_number = int(input(f"Hi {name}, Enter your phone number: "))
            phone_book[name] = phone_number
            print(f"Contact {name} added successfully")

        elif key == "2":
            if phone_book:
                print(phone_book)
            else:
                print("phone book is empty")

        elif key == "3":
            name = input(f"Enter the name you want to search: ")
            if name in phone_book:
                print(f"{name}: {phone_book[name]}")
            else:
                print(f"{name} is not found in phone book")
        
        elif key == "4":
            name = input("Enter the name of the contact you want to delete: ")
            if name in phone_book:
                del phone_book[name]
            else:
                print(f"{name} is not found in phone book")

        elif key == "5":
            print("bye..")
            break

        else:
            print("invalid choice")


phone()