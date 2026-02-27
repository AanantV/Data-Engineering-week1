def secret_list():

    print("I am thinking of a number between 1 - 10")

    print("you have 3 guesses left")

    correct = 7

    guess_list = []
    for i in range(1,4):
        guess = int(input(f"Enter your guess {i} here: "))
        guess_list.append(guess)

        if guess  == correct:
            print(f"Congrats! the correct answer is {correct}, your have guessed it correct at guess {i}")
            break

        elif guess > correct:
            print("You have entered a value that's higher than correct number")

        elif guess < correct:
            print("You have entered a value lower than the correct number")

        if i == 3:
            print("Game Over...")

    print(f"Your guesses were {guess_list}")

secret_list()
