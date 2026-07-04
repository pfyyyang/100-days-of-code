import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm','n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '（', '）', '*', '+']


print("Welcome to Password Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# easy level
# password = ""
# for char in range(0, nr_letters):
#     password += random.choice(letters)
#     # random_char = random.choice(letters)
#     # password += random_char
#
# for sym in range(1, nr_symbols + 1):
#     password += random.choice(symbols)
#     # random_sym = random.choice(symbols)
#     # password += random_sym
#
# for num in range(1, nr_numbers + 1):
#     password += random.choice(numbers)
#     # random_num = random.choice(numbers)
#     # password += random_num
# print(password)


# hard level
password_list = []
for char in range(0, nr_letters):
    password_list.append(random.choice(letters))
    # random_char = random.choice(letters)
    # password += random_char

for sym in range(1, nr_symbols + 1):
    password_list.append(random.choice(symbols))
    # random_sym = random.choice(symbols)
    # password += random_sym

for num in range(1, nr_numbers + 1):
    password_list.append(random.choice(numbers))
    # random_num = random.choice(numbers)
    # password += random_num
print(password_list)
random.shuffle(password_list)
print(password_list)

password = ""
for char in password_list:
    password += char

print(f"Your password is: {password}")
