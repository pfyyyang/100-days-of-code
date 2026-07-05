# For
# for item in list_of_items:
    # Do something to each item
# for number in ranger(a, b):
    # print(number)
# While
# while something_is_ture:
    # Do something repeatedly


def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()


while at_goal() != True:
# While not at_goal():
    jump()