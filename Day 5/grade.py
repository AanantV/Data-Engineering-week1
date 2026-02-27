import csv
import os

def grade():
    file_name = "grade.csv"
    
    def create_file():
        if not os.path.exists(file_name):
            try:
                with open(file_name, "w", newline='') as file:
                    writer = csv.DictWriter(file, fieldnames=["Name", "Grade"])
                    writer.writeheader()
            except Exception as e:
                print(f"Error creating file: {e}")

    def add_student(n, g):
        with open(file_name, "a", newline='') as file:
            writer = csv.writer(file)
            writer.writerow([n, g])
        return f"Successfully added {n}" # Added return

    def read_students():
        print("\n--- Student List ---")
        with open(file_name, "r") as file:
            reader = csv.reader(file)
            for row in reader:
                print(f"Name: {row[0]}, Grade: {row[1]}")
        return "End of list." # Added return

    def calc_avg():
        scores = []
        try:
            with open(file_name, "r") as file:
                reader = csv.reader(file)
                next(reader) # Skip header
                for row in reader:
                    scores.append(int(row[1]))
            
            if scores:
                average = sum(scores) / len(scores)
                return f"Class Average: {average:.2f}" # Added calculation and return
            return "No scores found."
        except FileNotFoundError:
            return "File not found."

    create_file()

    while True:
        print("\nGrade Tracker Menu")
        print("1. Add student details")
        print("2. Read student details")
        print("3. Calculate class average")
        print("4. Quit")

        choice = input("Enter a choice: ")

        if choice == "1":
            name = input("Enter Name: ")
            g_val = int(input("Enter grade (1-10): "))
            print(add_student(name, g_val))
        elif choice == "2":
            print(read_students())
        elif choice == "3":
            print(calc_avg())
        elif choice == "4":
            print("Quitting...")
            break # Fixed loop exit
        else:
            print("Invalid value")

grade()