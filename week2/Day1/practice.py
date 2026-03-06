def practice():

    # name = ['John', 'Sarah', 'Mike']
    # ages = [25,30,28]

    # students = {name:ages for name,ages in zip(name,ages)}

    # numbers = [1,2,3,4,5]
    # squares = {n:n**2 for n in numbers}
    prices = {"apple" : 1.50, "banana": 0.80, "orange":2.00}
    doubled = {name : price*2 for name,price in prices.items()}
    with_tax = {name:f"{price*0.15:.2f}" for name,price in doubled.items()}

    scores = {"john": 85, "Sarah": 92, "Mike": 78, "Emma": 95}
    high_scores = {name : score for name,score in scores.items() if score > 80}
    s_names = {name:score for name,score in scores.items() if name.startswith("S")}
    
    def grades(score):
        if score >=90:
            return "A"
        elif score >=80:
            return "B"
        elif score >=70:
            return "C"
        elif score <69:
            return "Fail"
        else: 
            return "Invalid"

    a_students = {grades(score): name for name, score in scores.items() if grades(score) == "A"}

    #SETS
    number = [1,2,2,3,3,3,4,5,5]
    unique  = set(number)

    text = "hello world"
    text_list = [word for word in text]
    text_set = set(text_list)
    sentence = "The cat and the dog and the bird"
    words = sentence.lower().split()
    #print(words)
    word = set(words)
    set_a = {1,2,3,4,5}
    set_b = {4,5,6,7,8}

    union = set_a | set_b
    common = set_a & set_b
    only_a = set_a - set_b
    sym_diff = set_a ^ set_b

    class_a = ["John", "Sarah", "Mike", "Emma"]
    class_b = ["Sarah", "Mike", "Alex", "Tom"]

    set_ca = set(class_a)
    set_cb = set(class_b)

    both = set_ca & set_cb
    only_ca = set_ca - set_cb
    only_cb = set_cb - set_ca
    all_students = set_ca | set_cb
    print(set_ca)
    square = lambda x: x**2
    double = lambda d:d*2
    ten = lambda t:t+10
    even_ = lambda e:e%2==0
    students = [{"name": "John", "grade": 85}, {"name": "Sarah", "grade": 92}, {"name": "Mike", "grade": 78}]
    sorted_grade = sorted(students, key = lambda students: students["grade"])
    sorted_name = sorted(students, key = lambda students: students["name"])
    sorted_desc = sorted(students, key = lambda students: students['grade'], reverse = True)

    employees = [{"name": "John","age" : 20,  "grade": 85}, {"name": "Sarah","age" : 19, "grade": 92}, {"name": "Mike","age" : 21, "grade": 78}]
    top_student = max(employees, key=lambda employees: employees['grade'])
    youngest = min(employees, key =lambda employees: employees['age'])
    oldest = max(employees, key = lambda employees:employees['age'])

    numbers = [1,2,3,4,5,6,7,8,9,10]

    squared = list(map(lambda x:x**2, numbers))
    doubled = list(map(lambda x: x*2, numbers))
    strings = list(map(lambda x: str(x), numbers))
    add_five = list(map(lambda x:x+5, numbers))

    even_ = list(filter(lambda x:x%2 ==0, numbers))
    odd = list(filter(lambda x:x%2!=0, numbers))
    div_by_3 = list(filter(lambda x: x%3 == 0 , numbers))

    triple_odds_1 = list(map(lambda x:x**3, filter(lambda x:x%2!=0, numbers)))
    triple_odds_2 = [x**3 for x in numbers if x%2!=0]
    #print(triple_odds_2)

    classs = [{"name": "John", "score": [85,90,88]}, {"name": "Sarah", "score": [92,95,98]}, {"name": "Mike", "score": [78,75,72]}]
    avg = {student['name']: f"{sum(student['score'])/len(student['score']):.2f}" for student in classs}
    high_performers = list(filter(lambda student : sum(student['score'])/len(student['score']) >= 90 , classs))
    upper_names = list(map(lambda student : student['name'].upper(), classs))
    sorted_students = sorted(classs, key = lambda student: sum(student['score'])/len(student['score']),reverse=True)
    data = [" john ", "SARAH", " mike", "Emma ", "", " "]
    cleaned = list(map(lambda x : x.lower().strip().title(), filter(lambda x: x != '' and x != ' ' ,data)))
    #print(cleaned)

    number = list(range(1,101))

    evens = list(filter(lambda x:x%2 == 0, number))
    squares_div5 = list(map(lambda x:x**2, filter(lambda x:x%5==0, number)))
    even_odd_dict = {num: ("even" if num%2 == 0 else "odd") for num in number}
    str_num = str(number)
    all_digits = {digit for num in number for digit in str(num)}

    print(sorted(all_digits))
practice()