import json
import csv
import os

def book_library():

    filename = "Week 2/Day 2/book.csv"
    fn = "Week 2/Day 2/book.json"
    required_fields = ["title", "author", "year", "genre", "status"]
    book = []
    #read = {}

    def initialise():
        try:
            if not os.path.exists(filename):
                with open(filename, "w", newline = '') as file:
                    writer = csv.DictWriter(file, fieldnames = required_fields) 
                    writer.writeheader()
        except Exception as e:
            print(f"File not created")

    def add_book():
        
        try:
            title = input("Enter the title of the book: ")
            author = input("Name of the author: ")
            year = int(input("Year: "))
            genre = input("Genre: ")
            status = input("status: ")
            with open(filename, "a",newline ='')as file:
                writer = csv.DictWriter(file, fieldnames = required_fields)
                #writer.writeheader()
                writer.writerow({"title" : title, "author": author, "year": year, "genre":genre, "status":status})
            save_json()
    
        except Exception as e:
            print(f"The file is not found: {e}")

    def view_all():
        try:
            with open(fn, "r") as file:
                read = json.load(file)
                for row in read:
                    print(row)

        except Exception as e:
            print(f"Can't read file: {e}")

    def mark():
        try:
            book_name = input("Enter the name of book: ")
            update_status = input("Read or Unread?: ")
            found = False
            with open(fn, "r") as file:
                reader = json.load(file)
                for row in reader:
                    if row["title"] == book_name:
                        row["status"] = update_status
                        found = True
                        break
                if found:
                        with open(fn, "w") as file:
                            json.dump(reader, file, indent = 4)
                        print(f"Status for {book_name} changed to {update_status}")
                else:
                        print(f"{book_name} not found in the file")

        except Exception as e:
            print(f"File not found: {e}")

    

    def save_json():

        try:
            with open(filename, "r") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    book.append(row)
        
        except Exception as e:
            print(f"File not found : {e}")

        try:
            with open(fn, "w", newline ='') as file:
               saved = json.dump(book, file, indent = 4)

        except json.JSONDecodeError:
            print(f"Error: Invalid JSON in '{filename}'")
            return None
        except FileNotFoundError:
            print(f"File not created")
            return None
        
    def genre():
        genre = input("Enter the name of genre: ")
        try:
            with open (fn, "r") as file:
                reader = json.load(file)
                genre_list = list(filter(lambda row:row["genre"] == genre, reader))
                print(f"The list based on {genre} genre is: {genre_list}")

        except Exception as e:
            print(f"Invalid genre: {e}")

    def unread_book():
         try:
             with open(fn, "r") as file:
                 reader = json.load(file)
                 for row in reader:
                     if row['status'] == "unread":
                        print(row['title'])

         except Exception as e:
             print(f"Data not found: {e}")

    initialise()

    

    while True:
        print("LIBRARY MANAGEMENT SYSTEM")
        print("1. Add book")
        print("2. View all books")
        print("3. Mark a book as read or unread")
        print("4. Genre based search")
        print("5. Unread books")
        print("6. Quit")

        choice = input("Enter a valid choice to begin with: ")
        if choice == "1":
            add_book()
        elif choice == "2":
            view_all()
        elif choice == "3":
            mark()
        elif choice == "4":
            genre()
        elif choice == "5":
            unread_book()
        elif choice == "6":
            print("Quitting....")
            break
        else:
            print("Invalid choice please print a valid choice")
            

book_library()