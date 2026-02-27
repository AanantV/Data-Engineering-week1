import csv

# def greet_user(name):
#     print(f"hello, {name}")
# greet_user("john")
# greet_user("sarah")
# greet_user("aanant")

# def calculate_area(len,wid):
#     result = len*wid
#     print(result)
# calculate_area(5,10)

# def power(base, exponent=2):
#     result = base ** exponent
#     print(result)
# power(3,3)

# def age_check():
#     try:
#         age = int(input("enter your age: "))
#         print(age)
#     except ValueError:
#         print("invalid age")
# age_check()

# def div():
#     try:
#         n1 = int(input("Enter num1: "))
#         n2 = int(input("Enter num2: "))
#         result = n1/n2
#         print(result)
#     except ValueError:
#         print("Invalid value")
#     except ZeroDivisionError:
#         print("Invalid input, division by 0")
# div()

# def fruits():
#     try:
#         fruits = ["apple","banana","orange"]
#         num = int(input(f"Enter the index you want to access: "))
#         print(fruits[num])
#     except ValueError:
#         print("invalid value")
#     except IndexError:
#         print("out of range index")
# fruits()

def file():
    file = open("file.txt","w")
    file.write("hello world!\n")
    file.close()

    file = open("file.txt", "r")
    content = file.read()
    print(content)
    file.close()

    with open("file.txt","r") as file:
        content = file.read()
        print(content)

    with open("file.txt", "a") as file:
        writing = input("enter the data to be added tothe file: ")
        file.write(writing)

    with open("file.csv", "w", newline = '') as file:
        writer = csv.writer(file)
        writer.writerow(["name", "age", "grade"])
        writer.writerow(["aanant","23","A"])
    
    with open("file.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)


file()