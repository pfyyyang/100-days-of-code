print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/______/_
*******************************************************************************
''')
print("Welcome to Treasure Island. "
      "You mission is to find the treasure. \n")
question_1 = input('You\'re at a cross road. '
                   'Where do you want to go? Type "left" or "right".\n' ).lower()


if question_1 == "left": #游戏继续
    question_2 = input('You\'ve come to a lake. There is an island in the middle of the lake.'
                       'Type "wait" to wait fo a boat. Type "swim" to swim across.\n').lower()
    if question_2 == "wait": #游戏继续
        question_3 = input("You arrive at the island unharmed. "
                           "There have three doors. which one you want to choose? "
                           "Type 'red', 'yellow' or 'green'.\n").lower()
        if question_3 == "yellow":
            print("You win!")
        elif question_3 in ["red", "green"]:
            print("Game Over!")
        else:
            print("Please enter the right choice.")
    elif question_2 == "swim":
        print("Game Over")
elif question_1 == "right":
    print("Game Over")
else:
    print("Please enter the right choice!")

