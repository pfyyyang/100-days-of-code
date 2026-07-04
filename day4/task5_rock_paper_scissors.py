import random

from PIL.ExifTags import IFD

Rock = '''    
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

Scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

Paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

your_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissor\n"))
game_image = [Rock, Paper, Scissors]
if 0 <= your_choice <= 2:
    print(game_image[your_choice])

# if your_choice == 0:
#     print(Rock)
# elif your_choice == 1:
#     print(Paper)
# elif your_choice == 2:
#     print(Scissors)



computer_choice = random.randint(0,2)
print("computer_choice: ")
print(game_image[computer_choice])

# if computer_choice == 0:
#     print(Rock)
# elif computer_choice == 1:
#     print(Paper)
# elif computer_choice == 2:
#     print(Scissors)

if  your_choice < 0 or your_choice > 2:
    print("Invalid Choice")
elif your_choice == computer_choice:
    print("Draw")
elif your_choice > computer_choice:
    print("You win")
elif your_choice < computer_choice:
    print("You lose")
elif your_choice == 0 and computer_choice == 2:
    print("You lose")
elif your_choice == 2 and computer_choice == 0:
    print("You win")






# your_choice_vs_computer = [your_choice, computer_choice]
#
# if your_choice_vs_computer == [0, 0]:
#     print("draw")
# elif your_choice_vs_computer == [0, 1]:
#     print("lose")
# elif your_choice_vs_computer == [0, 2]:
#     print("win")
# elif your_choice_vs_computer == [1, 0]:
#     print("win")
# elif your_choice_vs_computer == [1, 1]:
#     print("draw")
# elif your_choice_vs_computer == [1, 2]:
#     print("lose")
# elif your_choice_vs_computer == [2, 0]:
#     print("lose")
# elif your_choice_vs_computer == [2, 1]:
#     print("win")
# elif your_choice_vs_computer == [2, 2]:
#     print("draw")
