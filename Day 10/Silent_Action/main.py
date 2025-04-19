from art import logo


print(logo)
print("Welcome to the Silent Action Program:")
bidder_info = {}

while True:
    name = input("What is your name? ")
    bidder_info[name] = "How much do you want to bid? R"
    other_bidder = input("Is there another bidder?(Yes(Y)/No(N)):\n")

    if other_bidder.lower() == "N".lower():
        break
    else:
        print("\n"*100)

             