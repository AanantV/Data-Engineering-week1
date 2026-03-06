import os
import csv
import json

def multi_file():

    st = "Week 2/Day 2/multi_file/students.json"
    gd = "Week 2/Day 2/multi_file/grades.json"
    at = "Week 2/Day 2/multi_file/attendance.json"
    filename = "Week 2/Day 2/multi_file.csv"

    def initialise(filename):
        if not os.path.exists(filename):
            with open(filename, "w", newline='') as file:
                writer = csv.DictWriter(file, fieldnames = ['student_id', 'name', 'age', 'grade', 'attendance'])
                writer.writeheader()
                print(f"file created on path {filename}")

    def file():
        try:
            grades = [
                        {
                            "student_id": 101,
                            "subject": "Mathematics",
                            "grade": "A"
                        },
                        {
                            "student_id": 101,
                            "subject": "Physics",
                            "grade": "B+"
                        },
                        {
                            "student_id": 102,
                            "subject": "Mathematics",
                            "grade": "B"
                        },
                        {
                            "student_id": 103,
                            "subject": "History",
                            "grade": "A-"
                        }
                    ]
            
            students = [
                        {
                            "id": 101,
                            "name": "Alice Thompson",
                            "age": 15
                        },
                        {
                            "id": 102,
                            "name": "Brian Okoro",
                            "age": 16
                        },
                        {
                            "id": 103,
                            "name": "Chloe Zhao",
                            "age": 15
                        }
                    ]
            
            attendance = [
                            {
                                "student_id": 101,
                                "days_present": 45,
                                "days_absent": 2
                            },
                            {
                                "student_id": 102,
                                "days_present": 40,
                                "days_absent": 7
                            },
                            {
                                "student_id": 103,
                                "days_present": 47,
                                "days_absent": 0
                            }
                        ]
            
            with open(st, "w") as file:
                writer = json.dump(students,file, indent = 4)

            with open(gd, "w") as file:
                writer = json.dump(grades,file,indent =4)
            
            with open(at, "w") as file:
                writer = json.dump(attendance,file,indent=4)

        except Exception as e:
            print(f"JSON error: {e}")

    def merge():
        try:
            class_students = []
            with open(st, "r") as file:
                student_list = json.load(file)
            with open(gd, "r") as file:
                grades_list = json.load(file)
            with open(at, "r") as file:
                attendance_list = json.load(file)

            for sl in student_list:
                st_info = {
                    'student_id': sl['id'],
                     'name' : sl['name'],
                     'age' : sl['age'],
                     'grade': {},
                     'attendance' : {}
                }
                for gl in grades_list:
                    if gl['student_id'] == sl['id']:
                        st_info['grade'] = {
                            'subject' : gl['subject'],
                            'grade' : gl['grade']
                        }

                for al in attendance_list:
                        if al['student_id'] == sl['id']:
                            st_info['attendance'] = {
                                'days_present': al['days_present'],
                                'days_absent' : al['days_absent']
                        }
                class_students.append(st_info)
            
            with open("Week 2/Day 2/merged.json", "w") as file:
                    json.dump(class_students,file,indent =4)

        
        except Exception as e:
            print(f"JSON error: {e}")

    mn = "Week 2/Day 2/merged.json"

    def max_attendance():
        try:
            with open(mn, "r") as file:
                reader = json.load(file)
                present = []
                for row in reader:
                    att = {'name': row['name'],'present': row['attendance']['days_present']}
                    present.append(att)
                for pt in present:
                    p_top = pt['present']
                    highest = 0
                    if highest<p_top:
                        highest = p_top
                        p_name = pt['name']
                print(f"The student with highest attendance is {p_name} and no. of days present is {p_top}")

        except Exception as e:
            print(f"JSON error: {e}")
    
    initialise(filename)

    while True:
        print("\n--- Multiple file merger ---")
        print("1. Load all files")
        print("2. merge all files")
        print("3. highest attendance")
        print("4. Quit")

        choice = input("Enter choice: ")

        if choice == "1":
            file()
        elif choice == "2":
            merge()
        elif choice == "3":
            max_attendance()
        elif choice == "4":
            break
        else:
            print("Invalid choice.")

multi_file()