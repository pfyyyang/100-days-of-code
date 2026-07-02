# Nested if / else
# if condition:
#     if another condition:
#         do this
#     else:
#         do this
# else:
#     do this

height = int(input("What is your height in cm?"))

if height > 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age?"))
    if age <= 12:
        print("You should pay $5.")
    elif age <= 18:
        print("You should pay $7.")
    else:
        print("You should pay $12.")

else:
    print("Sorry, you cannot ride the rollercoaster!")