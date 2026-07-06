import random

stages = ['''
      _______
     |/      |
     |      (_)
     |      \|/
     |       |
     |      / \
     |
  ___|___
''', '''
      _______
     |/      |
     |      (_)
     |      \|/
     |       |
     |      /
     |
  ___|___
''', '''
      _______
     |/      |
     |      (_)
     |      \|/
     |       
     |      
     |
  ___|___
''', '''
      _______
     |/      |
     |      (_)
     |      \|
     |       
     |      
     |
  ___|___
''', '''
      _______
     |/      |
     |      (_)
     |       |
     |       
     |      
     |
  ___|___
''', '''
      _______
     |/      |
     |      (_)
     |       
     |       
     |      
     |
  ___|___
''', '''
      _______
     |/      |
     |      
     |      
     |       
     |      
     |
  ___|___
''']


lives = 6

words_list = ["apple", "banana", "grape", "pear", "lemon", "orange"]


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
    guess = input("Guess a letter:").lower()


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
        lives -= 1
        if lives == 0:
            game_over = True
            print("You Lose!")


    if "_" not in display:
        game_over = True
        print("You win!")
    print(stages[lives])