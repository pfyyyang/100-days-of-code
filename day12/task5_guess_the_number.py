import random

from art import logo
print(logo)

print("Welcome to the Number Guessing Game!"
      "\nI'm thinking of a number between 1 and 100.")

choice = input("Choose a difficulty. Type 'easy' or 'hard':")



number = random.randint(1, 100)
print(number)

def easy_model():
    choice1 = 0
    attempt = 10
    print("You have 10 attempts remaining to guess the number.")
    while choice1 != number and attempt > 0:
        choice1 = int(input("Make a guess:"))
        if choice1 < number:
            print("Too low.")
            attempt -= 1
            print(f"You have {attempt} attempts remaining to guess the number.")
        elif choice1 > number:
            print("Too high.")
            attempt -= 1
            print(f"You have {attempt} attempts remaining to guess the number.")
        else:
            print("You guessed correctly.")
    if attempt == 0:
        print("You've run out of guesses. Refresh the page to run again.")
        print("\n" * 20)



def hard_model():
    choice1 = 0
    attempt = 5
    print("You have 5 attempts remaining to guess the number.")
    while choice1 != number and attempt > 0:
        choice1 = int(input("Make a guess:"))
        if choice1 < number:
            print("Too low.")
            attempt -= 1
            print(f"You have {attempt} attempts remaining to guess the number.")
        elif choice1 > number:
            print("Too high.")
            attempt -= 1
            print(f"You have {attempt} attempts remaining to guess the number.")
        else:
            print("You guessed correctly.")
    if attempt == 0:
        print("You've run out of guesses. Refresh the page to run again.")
        print("\n" * 20)

if choice == "easy":
    easy_model()
elif choice == "hard":
    hard_model()


