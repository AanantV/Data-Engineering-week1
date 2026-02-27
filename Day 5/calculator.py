def calculator():
    def add(n1,n2):
        return n1+n2
    def sub(n1,n2):
        return n1-n2
    def mul(n1,n2):
        return n1*n2
    def div(n1,n2):
        try:
            return n1/n2
        except ZeroDivisionError:
            print("division by zero")
    def logs(op,num1,num2,result):
        print("Logged calculations")
        with open("calculator_logs.txt", "a") as file:
            file.write(f"{num1} {op} {num2} = {result}\n")

    while True:
        print("calculator: please select an operation to perform")
        print("1. add")
        print("2. sub")
        print("3. mul")
        print("4. div")
        print("5. logs")
        print("6. quit")

        choice = input("Enter your choice: ")

        if choice == "6":
            print("quitting...")
            False
        if choice == "5":
            print("The calculator logs are: ")
            with open("calculator_logs.txt") as file:
                history = file.read()
                if history:
                    print(history)
                else:
                    print("No logs found")
        
        try:
            num1 = int(input("enter number 1: "))
            num2 = int(input("Enter number 2: "))
        except ValueError:
            print("Invalid value")

        
        if choice == "1":
            result = add(num1,num2)
            logs("+",num1,num2,result)
            print(f"Result: {num1} + {num2} = {result}")
        elif choice == "2":
            result = sub(num1,num2)
            logs("-",num1,num2,result)
            print(f"Result: {num1} - {num2} = {result}")
        elif choice == "3":
            result = mul(num1,num2)
            logs("*",num1,num2,result)
            print(f"Result: {num1} * {num2} = {result}")
        elif choice == "4":
            result = div(num1,num2)
            logs("/",num1,num2,result)
            print(f"Result: {num1} / {num2} = {result}")

calculator()