print("Welcome to Pizza Delivery Hub")
size = input("What size of pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra_pizza cheese? Y or N: ")
cost = 0

# Initial cost of pizza based on size 
if size.lower() == "s":
    cost = 15
elif size.lower() == "m":
    cost = 20
elif size.lower() == "l":
    cost = 25
else:
    print("Invalid size. Please choose S, M or L")
# Additional cost if pepperoni is added
if  (pepperoni.lower() == "y") and (size.lower() == "s"):
    cost += 2
elif  (pepperoni.lower() == "y") and ((size.lower() == "m") or (size.lower() == "l")):
    cost += 2
else:
    print("No extra cheese")

# Additional cost if extra cheese is added

if (extra_cheese.lower() == "y"):
    cost += 2

print(f"Your Pizza fee is R {cost}.")