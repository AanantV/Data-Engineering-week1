def grade_tracker():

    name_list = []
    grade_list = []
    for i in range (5):
        name = str(input("Enter your name: "))
        name_list.append(name)
        grade = int(input(f"Hi {name}, Please enter your mark: "))
        grade_list.append(grade)
        i = i+1


    print(name_list)
    print(grade_list)

    print("Student results are: ")

    for j in range (len(name_list)):
        print(f"Name: {name_list[j]} | mark: {grade_list[j]}")

    max_scorer = max(grade_list)
    min_scorer = min(grade_list)
    avg_score = sum(grade_list)/len(grade_list)

    print(f"The highest scorer is {name_list[grade_list.index(max_scorer)]}")
    print(f"The lowest scorer is {name_list[grade_list.index(min_scorer)]}")
    print(f"The average score of students is {avg_score}")

grade_tracker()