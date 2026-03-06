import csv
import os

def set_operations():

    file_a = "Week 2/Day 1/class_a.csv"
    file_b = "Week 2/Day 1/class_b.csv"
    try:
        class_a = set()
        class_b = set()

        with open(file_a , "r") as file:
            reader = csv.reader(file)
            header = next(reader)
            class_a = {tuple(rows) for rows in reader}
            print(class_a)

        with open(file_b, "r") as file:
            reader = csv.reader(file)
            header = next(reader)
            class_b = {tuple(rows) for rows in reader}
            print(class_b)
    
    except Exception as e:
        print(f"List not created: {e}")

    set_a = set(class_a)
    set_b = set(class_b)

    union = set_a | set_b
    only_a = set_a - set_b
    only_b = set_b - set_a
    intersection = set_a & set_b
    stud_left = set_a ^ set_b
    new = set_b ^ set_a

    text = "Week 2/Day 1/report.txt"

    try:

        report = f"""SET OPERATIONS REPORT
Students in Class A: {set_a}
Students in Class B: {set_b}


All students in both classes: {union}
Students only on class A: {only_a}
Students only on Class B: {only_b}
Students in both class: {intersection}
Students who left: {stud_left}
New Student: {new}


"""
        if not os.path.exists(text):
            with open(text, "w", newline = '') as file:
                writer = file.write(report)
    
    except Exception as e:
        print(f"File not created: {e}")

set_operations()