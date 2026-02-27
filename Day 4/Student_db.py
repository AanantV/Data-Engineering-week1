def student_db():
    student_list = {}

    student_list["name"] = str(input("Enter name: "))
    student_list["age"] = int(input("Enter age: "))
    student_list["grade"] = str(input("Enter grade(A to F): "))
    subject = (input("Enter the subjects with ',': "))
    student_list["subject"] = subject.split(", ")

    print("Student information: ")
    print(f"Name: {student_list['name']}")
    print(f"Age: {student_list['age']}")
    print(f"Grade: {student_list['grade']}")
    print(f"Subject: {', '.join(student_list['subject'])}")

    print("Would you like to update any field? if Yes type the field number as shown below or press q to quit")
    print("1. Name")
    print("2. Age")
    print("3. Grade")
    print("4. Subject")

    choice = int(input("Enter your choice"))
    
    if choice == 1:
        student_list['name'] =  input("Enter the name: ")
    elif choice == 2:
        student_list["age"] = input("Enter the age: ")
    elif choice == 3:
        student_list["grade"] = input("Enter the grade: ")
    elif choice == 4:
        subject = input("Enter the subject: ")
        student_list["subject"] = subject.split(", ")
    else:
        print("invalid choice")
    
    print("Updated list: ")
    print(f"Name: {student_list['name']}")
    print(f"Age: {student_list['age']}")
    print(f"Grade: {student_list['grade']}")
    print(f"Subject: {', '.join(student_list['subject'])}")
    

    #print(student_list)

student_db()