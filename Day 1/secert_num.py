def secret_number():
    print("I am thinking of a number between 1 - 10")

    print("you have 3 guesses left")

    n = 7


    for attempt in range(1,4):
        guess = int(input(f"Attempt{attempt}: Enter your guess: "))

        if guess == n:
            print(f"Congrats, you won on attempt{attempt}")
            break
        elif guess < n:
            print("too low")
        else:
            print("too high")
        if attempt == 3:
            print(f"Game over! the secret number is {n}")

secret_number()
