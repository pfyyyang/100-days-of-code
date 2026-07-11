import random

from art import logo
print(logo)

print("Welcome to the Number Guessing Game!"
      "\nI'm thinking of a number between 1 and 100.")

choice = input("Choose a difficulty. Type 'easy' or 'hard':")

number = random.randint(1, 100)

def play_game(attempts):
    guess = 0

    while guess != number and attempts > 0:
        print(f"You have {attempts} attempts remaining.")
        guess = int(input("Make a guess: "))

        if guess < number:
            print("Too low.")
            attempts -= 1
        elif guess > number:
            print("Too high.")
            attempts -= 1
        else:
            print("You guessed correctly!")

    if attempts == 0:
        print(f"You've run out of guesses. The number was {number}.")


if choice == "easy":
    play_game(10)
elif choice == "hard":
    play_game(5)