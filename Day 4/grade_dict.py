def grade_dict():

    students = []
    
    for student in range (3):
        name = str(input("Enter name: "))
        age = int(input(f"Hi {name} Enter age: "))
        i = 0
        score = []
        for i in range(3):
            scores = int(input(f"hi {name}, please enter your score {i+1}: "))
            score.append(scores)
        student = {"name": name, "age" : age, "scores": score}
        students.append(student)
        average = sum(student["scores"])/len(student["scores"])
        student["average"] = average
    
    highest_student = students[0]
    for student in students:
        if student["average"] > highest_student["average"]:
            highest_student = student
    print(f"Highest student average is {highest_student["average"]} and the student is {highest_student["name"]}")

    print("students sorted by average")
    students.sort(key = lambda x: x["average"], reverse = True)
    print(students)
    


grade_dict()