from art import logo
print(logo)

# winner = max(content, key=content.get)
def find_highest_bidder(content):
    winner = ""
    highest_bidder = 0
    for bidder in content:
        bid_amount = content[bidder]
        if content[bidder] > highest_bidder:
            highest_bidder = content[bidder]
            winner = bidder

    print(f"The winner is  {winner}")

content = {}

continued_bidding = True
while continued_bidding:
    user_name = input("What is your name?:\n")
    user_bid = float(input("What is your bid?: $\n"))

    content[user_name] = user_bid
    continued = input("Are there any other bidders? Type 'yes' or 'no':\n")

    if continued == "no":
        continued_bidding = False
        find_highest_bidder(content)

    elif continued == "yes":
        print("\n" * 20)



