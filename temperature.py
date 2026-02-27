def temperature():
    n = str(input("Celsius or Farenheit?"))
    temp = float(input("Enter the temperature value: "))

    if n == "Celsius" or n == "C":
       value =  (temp * 9/5) + 32
       print(f"The Celsius  to Farenheit value is {value}")
    elif n == "Farenheit" or n == "F":
        value = (temp - 32) * 5/9
        print(f"The Farenheit to Celsius value is {value}")
    else:
        print("Invalid arguement! please enter a valid argurment")
temperature()
