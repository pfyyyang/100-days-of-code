import random

words_list = ["apple", "banana", "grape", "pear", "lemon", "orange"]
chosen_word = random.choice(words_list)
print(chosen_word)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print(placeholder)




guess = input("Guess a letter:").lower()
print(guess)

for letter in chosen_word :
    if letter == guess :
        print("Right")
    else:
        print("Wrong")

display = ""
for letter in chosen_word:
    if letter == guess:
        display += letter
    else:
        display += "_"
print(display)