import random


def guessing_game():
    secret_number = random.randint(15, 30)

    while True:
        # Get the user's guess as a input
        guess = int(input("Guess a number: "))

        # Check if the guess is correct
        if guess == secret_number:
            print("Congratulations! You guessed the correct number!")
            break
        elif guess < secret_number:
            print("Oops! Too low.")
        else:
            print("Oops! Too high.")


if __name__ == "__main__":
    guessing_game()