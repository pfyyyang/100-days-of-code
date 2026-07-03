states_of_america = ["Delaware", "Pennsylvania", "Georgia", "Massachusetts"]
# list[offset/index]
print(states_of_america[0])
print(states_of_america[-1])

# change item
states_of_america[1] = "Pencilvania"
print(states_of_america)

# add item
states_of_america.append("Anglaland")
print(states_of_america)

states_of_america.extend(["New York", "Los Angeles"])
print(states_of_america)

# you can read more functions in python documents (docs.python.org)