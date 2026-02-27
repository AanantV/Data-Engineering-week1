def grade():
    mark = int(input("Enter your mark between 0 - 100: "))

    match mark:
        case m if mark>=90 and mark<=100:
                print("your grade is A")
        case m if mark>=80 and mark<=89:
                print("your grade is B")
        case m if mark>=70 and mark<=79:
                print("your grade is C")
        case m if mark>=60 and mark<=69:
                print("your grade is D")
        case m if mark<60:
                print("your grade is F")
        case _:
            print("Invalid mark")

grade()
