from art import logo
"""
Silent Auction Program
This script implements a simple silent auction system where multiple bidders can enter their names and bid amounts.
After all bids are collected, the program determines and announces the highest bidder as the winner.
Features:
- Displays a logo from the 'art' module.
- Collects bidder names and bid amounts in a loop until no more bidders.
- Clears the screen between bidders for privacy.
- Determines and prints the winner with the highest bid.
Variables:
- bidder_info (dict): Stores bidder names as keys and their bid amounts as values.
Usage:
Run the script and follow the prompts to enter bidder information and determine the auction winner.
"""

print(logo)
print("Welcome to the Silent Action Program:")
bidder_info = {}

while True:
    name = input("What is your name? ")
    bidder_info[name] = float(input("How much do you want to bid? R "))
    other_bidder = input("Is there another bidder?(Yes(Y)/No(N)):\n")

    if other_bidder.lower() == "N".lower() or other_bidder.lower() == "No".lower():
        print("\n"*100)
        break
    else:
        print("\n"*100)

for bidder_name, bidder_amount in enumerate(bidder_info):
    if bidder_info[bidder_name] == max(bidder_info.values()):
        print(f"The winner is {bidder_name} with a bid of R {bidder_info[bidder_name]}")
        break