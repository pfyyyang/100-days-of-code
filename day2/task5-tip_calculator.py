print("Welcome to the calculator!")
bill = float(input("What was the total bill?\n"))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15?\n"))
people = int(input("How many people to split the bill?\n"))
each_pay =round(bill / people * (1 + tip / 100), 2)

print(f"Each person should pay: ${each_pay}")