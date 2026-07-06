import random
import  hangman_art
from  hangman_words import words_list # more light
from hangman_art import logo

# from hangman_art import stages, logo

print(logo)

lives = 6

chosen_word = random.choice(words_list)
print(chosen_word)

placeholder = ""
word_length = len(chosen_word)

for position in range(word_length):
    placeholder += "_"
print(placeholder)


game_over = False
correct_letters = []

while not game_over:
    print(f"*********************************<{lives}/6 LIVES LEFT>*********************************")
    guess = input("Guess a letter:").lower()

    if guess in correct_letters:
        print(f"You're already guessed {guess}")

    display = ""
    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:     #虽然 a 不是我这一次猜的字母，但是 a 是我以前猜对过的字母，所以也要显示出来。
            display += letter
        else:
            display += "_"
    print(display)

    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life! ")
        lives -= 1
        if lives == 0:
            game_over = True
            print(f"*********************************IT WAS '{chosen_word}', You Lose!*********************************")


    if "_" not in display:
        game_over = True
        print("*********************************YOU WIN!*********************************")
    print(hangman_art.stages[lives])