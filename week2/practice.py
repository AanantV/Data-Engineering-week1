import json

def practice():

    # person = {
    #     "name": "John",
    #     "age": 25,
    #     "city": "New York"
    # }

    # json_string = json.dumps(person)
    # print(json_string)
    # print(type(json_string))

    # pretty_json = json.dumps(person, indent =4)
    # print(pretty_json)

    json_data = '{"name": "Sarah", "age": 30, "city" : "Boston"}'
    person = json.loads(json_data)
    # print(person)
    # print(type(person))
    # print(person['name'])
    # print(person['age'])

    student = {
        "name" : "Mike",
        "age" : 20,
        "grade" : "A",
        "subjects" : ["Math", "Science", "English"]
        }
    
    with open("Week 2/Day 2/student.json", "w") as file:
         json.dump(student, file, indent = 4)

    employee = {"name":"Aanant", "age":24, "grade": "PA"}

    with open("Week 2/Day 2/my_info.json", "w") as file:
        json.dump(employee, file, indent=4)

    with open("Week 2/Day 2/my_info.json", "r") as file:
        data = json.load(file)

    # print("Loaded data: ",data)
    # print(f"Employee Name: {data['name']}")
    # print(f"Employee Age: {data['age']}")

    students = [
        {"name" : "John", "age" : 20, "grade" : "A"},
        {"name" : "Sarah", "age" : 23, "grade" : "B"},
        {"name" : "Mike", "age" : 21, "grade" : "A"}
    ]

    with open("Week 2/Day 2/class_info.json", "w") as file:
        json.dump(students, file, indent =4)

    with open("Week 2/Day 2/class_info.json", "r") as file:
        status = json.load(file)

    for student in status:
        print(f"{student['name']} - Grade: {student['grade']}")

    with open("Week 2/Day 2/class_info.json", "r") as file:
        students = json.load(file)

    new_student = {"name": "Mark", "age": 20, "grade": "B"}
    students.append(new_student)

    fl = "Week 2/Day 2/fl.json"

    with open("Week 2/Day 2/class_info.json", "w") as file:
        json.dump(students, file, indent=4)
    
    with open("Week 2/Day 2/class_info.json", "r") as file:
        filtering = json.load(file)

    a_student = [x for x in filtering if x['age'] == 20]

    with open("Week 2/Day 2/20_age.json", "w") as file:
        json.dump(a_student, file, indent=4)

    company = {
        "name" : "Techcorp",
        "location": {
            "city" : "san francisco",
            "state" : "CA",
            "zip" : "94102"
        },
        "employees" : 500
    }

    with open("Week 2/Day 2/company.json", "w") as file:
        json.dump(company, file, indent = 4)

    with open("Week 2/Day 2/company.json", "r") as file:
        details = json.load(file)

    # print("Company: ", details)
    # print(f"City: {details['location']['city']}")
    # print(f"Zip: {details['location']['zip']}")

    s1 = {
        "name" : "alex",
        "age" : 20,
        "scores" : {
            "math" : [85, 90, 88],
            "science" : [92, 95, 90],
            "english" : [78, 82, 85]
        }
    }

    with open("Week 2/Day 2/s1.json", "w") as file:
        json.dump(s1,file,indent =4)
    
    for subject, scores in s1['scores'].items():
        avg = sum(scores)/len(scores)
        print(f"{subject.title()}: {avg:.2f}")

    school = {
    "name": "Central High",
    "classes": [
        {
            "name": "Math 101",
            "teacher": "Mr. Smith",
            "students": [
                {"name": "John", "grade": 85},
                {"name": "Sarah", "grade": 92}
            ]
        },
        {
            "name": "Science 101",
            "teacher": "Ms. Johnson",
            "students": [
                {"name": "Mike", "grade": 88},
                {"name": "Emma", "grade": 95}
            ]
        }
    ]
    }
    with open("Week 2/Day 2/school.json", "w") as file:
        schoold = json.dump(school,file,indent =4)

    all_students = []
    for cls in school['classes']:
        c_name = cls['name']
        c_teacher = cls['teacher']
        print(f"Name: {c_name}, teacher: {c_teacher}")
        all_students.extend(cls['students'])
    
    for std in all_students:
        max_student = max(all_students, key = lambda std:std['grade'])
        
    print(f"Topper: {max_student}")

    grade = []
    for std in all_students:
        count = len(std['name'])
        grade.append(std['grade'])
    print(grade)
        
    average = sum(grade)/len(grade)
    print(average)

    def validate_student(st):
        

        required_field = ["name", "age", "grade"]

        for field in required_field:
            if field not in st:
                return False, f"Missing required field: {field}"
            
        if not isinstance(st["age"], int):
            return False, "Age must be a number"
        
        if st["age"] < 0 or st["age"] > 100:
            return False, "Age must be between 1-100"
        
        return True, "valid student"
    student1 = {"name":"John", "age": 20, "grade": "A"}
    student2 = {"name":"Emma", "age": "twenty"}
    
    valid, message = validate_student(student1)
    valid, message = validate_student(student2)

    print(f"Student 1: {message}")
    print(f"Student 2: {message}")
    print(student2)


practice()