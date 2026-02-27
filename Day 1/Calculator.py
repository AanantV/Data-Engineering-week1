def calculator():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    #Here we are getting input from user
    n = input("select an operation to perform calculation:")
    if n == "add":
        n = num1 + num2
        print(f"the sum is {n}")
    elif n == "sub":
        if num1 > num2:
            n = num1 - num2
            print(f"the difference is {n}")
        else:
            n = num2 -num1
            print(f"the difference is: {n}")
    elif n == "mul":
        n = num1 * num2
        print(f"the product is {n}")
    elif n == "div":
        n = num1/num2
        print(f"the quotient is {n}")
    else:
        print("Invalid operation! please enter a valid operation")

calculator()
#The above command is to inititate the function

        
