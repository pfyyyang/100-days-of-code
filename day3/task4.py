height = int(input("What is your height in cm?"))
bill = 0
if height > 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age?"))
    if age <= 12:
        bill = 5
        print("You should pay $5.")
    elif age <= 18:
        bill = 7
        print("You should pay $7.")
    else:
        bill = 12
        print("You should pay $12.")
    wants_photo = input("Do you want to have a photo take? Type y for Yes and n for No.")
    if wants_photo == "y":
        bill += 3

    print(f"Your final bill is: {bill}")
# The indentation is really important.

else:
    print("Sorry, you cannot ride the rollercoaster!")