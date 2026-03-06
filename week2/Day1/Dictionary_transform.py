def dict_transform():

    students = [{"name": "John", "scores": [85, 90, 88]}, {"name": "Sarah", "scores": [90, 90, 100]}, {"name": "Jane", "scores": [87, 98, 98]}]
    stud_dict = {student['name'] : f"{sum(student["scores"])/len(student["scores"]):.2f}" for student in students}

    def grade(scores):
        if scores>90:
            return "A"
        elif scores>80:
            return "B"
        elif scores>70:
            return "C"
        elif scores>60:
            return "D"
        elif scores>50:
            return "E"
        else:
            return "Invalid"
        
    grading = {student['name']: grade(sum(student['scores'])/len(student['scores'])) for student in students}
    above_80 = {name : avg for name,avg in stud_dict.items() if float(avg) > 90}
    doubled = {name : float(avg)*2 for name,avg in stud_dict.items()}
    group = {name : grade(float(avg)) for name, avg in stud_dict.items()}
    
    
    print(group)

dict_transform()