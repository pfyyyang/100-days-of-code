import random

words_list = ["apple", "banana", "grape", "pear", "lemon", "orange"]
chosen_word = random.choice(words_list)
print(chosen_word )

guess = input("Guess a letter:").lower()
print(guess)

for letter in chosen_word :
    if letter == guess :
        print("Right")
    else:
        print("Wrong")


