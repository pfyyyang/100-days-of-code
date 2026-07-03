import random

# 1 Option
friends = ["Alice","Bob", "Charlie", "David", "Emanuel"]
print(random.choice(friends))

# 2 Option
friends = ["Alice","Bob", "Charlie", "David", "Emanuel"]
random_index = random.randint(0,4)
print(friends[random_index])

# 3 Option
friends = ["Alice","Bob", "Charlie", "David", "Emanuel"]
pay_person = random.randint(1, 5)

if pay_person == 1:
    print(friends[0])
if pay_person == 2:
    print(friends[1])
if pay_person == 3:
    print(friends[2])
if pay_person == 4:
    print(friends[3])
if pay_person == 5:
    print(friends[4])
