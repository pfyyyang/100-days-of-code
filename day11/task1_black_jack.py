import random
from art import logo

question_1 = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
if question_1 == 'y':

    print(logo)

    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card_1 = random.choice(cards)
    card_2 = random.choice(cards)
    computer_1 = random.choice(cards)
    computer_2 = random.choice(cards)
    computer_3 = random.choice(cards)
    your_cards = [card_1, card_2]
    computer_cards = [computer_1, computer_2, computer_3]
    user_sum_cards = card_1 + card_2
    computer_sum_cards = computer_1 + computer_2
    print(f"Your cards: {your_cards}, current score: {user_sum_cards}"
          f"\nComputer's first cards: {computer_1}")

    continued = True


    while continued:
        question_2 = input("Type 'y' to get another card, type 'n' to pass: ")

        if question_2 == 'y':
            card_3 = random.choice(cards)
            your_cards.append(card_3)
            user_sum_cards += card_3
            print(f"Your cards:{your_cards}, current score: {user_sum_cards}")

            if user_sum_cards > 21:
                continued = False
                print(f"Your final hand: {your_cards}, final score: {user_sum_cards}")
                print("You went over. You lose!")


        if question_2 == 'n':
            continued = False
            computer_sum_cards += computer_3
            print(f"Your final hand: {your_cards}, final score: {user_sum_cards}"
                    f"\nComputer's final hand: {computer_cards}, final score: {computer_sum_cards}")

elif question_1 == 'n':
    print("\n" * 20)

