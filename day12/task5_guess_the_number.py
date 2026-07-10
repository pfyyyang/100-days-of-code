import random

from art import logo
print(logo)

print("Welcome to the Number Guessing Game!"
      "\nI'm thinking of a number between 1 and 100.")

choice = input("Choose a difficulty. Type 'easy' or 'hard':")



number = random.randint(1, 100)
print(number)



if choice == "easy":
    choice1 = 0
    attempt = 10
    print("You have 10 attempts remaining to guess the number.")
    while choice1 != number and attempt > 1:
        choice1 = int(input("Make a guess:"))

        print(f"You have {attempt} attempts remaining to guess the number.")

        if choice1 < number:
            print("Too low.")
            attempt -= 1
        elif choice1 > number:
            print("Too high.")
            attempt -= 1
        else:
            print("You guessed correctly.")


elif choice == "hard":
    print("You have 5 attempts remaining to guess the number.")
    if choice1 < number:
        print("Too low.")






