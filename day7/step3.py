import random

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
    if "_" not in display:
        game_over = True
        print("You win!")


# for loop
# 第一轮猜 a：
# a 走 if
# p 走 else
# p 走 else
# l 走 else
# e 走 else
# 显示：
# a____
# 并且：
# correct_letters = ["a"]
# 第二轮猜 p：
# a 走 elif   因为 a 之前猜中过
# p 走 if     因为这次猜的是 p
# p 走 if
# l 走 else
# e 走 else
# 显示：
# app__