import csv
import os

def phone_book():

    def initialize(pb):
        try:
            if not os.path.exists(pb):
                with open(pb, "a", newline = '') as file:
                    writer = csv.DictWriter(file, fieldnames = ["Name","Contact"])
                    writer.writeheader()
        except Exception as e:
                print(f"Error creating file: {e}")
    
    def load_contacts(pb):
        with open(pb, "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                print(f"Name: {row['Name']}, Contact : {row['Contact']}")

    def add_contact(pb):
        name = input("Enter the name: ")
        contact = input(f"Enter the contact of {name}: ")
        try:
            with open(pb, "a", newline = '') as file:
                columns = ["Name","Contact"]
                writer = csv.DictWriter(file, fieldnames = columns)
                writer.writerow({"Name": name, "Contact" : contact})
                print("Contact added successfully")
        except Exception as e:
                print(f"Invalid value: {e}")

            

    def search_contact(pb):
        name_find = input("enter the name to be found: ")
        try:
            with open(pb, "r") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    if name_find == row["Name"]:
                        print(f"The contact of {name_find} is {row['Contact']}")
        except Exception as e:
            print(f"Contact not found: {e}")

    def delete_contact(pb):
        name_delete = input("Enter the record to be deleted: ")
        updated_list = []
        found = False
        try:
            with open(pb, "r") as file:
                reader = csv.DictReader(file)
                fieldnames = reader.fieldnames
                for row in reader:
                    if name_delete == row["Name"]:
                        found = True
                    else:
                        updated_list.append(row)
                if found:
                    with open(pb, "w", newline ='') as file:
                            writer = csv.DictWriter(file, fieldnames)
                            writer.writeheader()
                            writer.writerows(updated_list)
                else:
                    print("Data not found")
                
        except Exception as e:
            print(f"Data not found: {e}")

    phone_book = "phone_book.csv"

    initialize(phone_book)


    while True:
        print("Phone Directory")
        print("1. load all contacts")
        print("2. add a contact")
        print("3. search contact")
        print("4. delete contact")
        print("5. quit")

        choice = input("Enter a choice between 1 to 5: ")

        if choice == "1":
            load_contacts(phone_book)
        elif choice == "2":
            add_contact(phone_book)
        elif choice == "3":
            search_contact(phone_book)
        elif choice == "4":
            delete_contact(phone_book)
        elif choice == "5":
            print("quitting...")
            break
        else:
            print("Invalid choice")


phone_book()