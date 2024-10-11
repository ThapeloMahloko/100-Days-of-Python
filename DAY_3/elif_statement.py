"""
Write a program that check the height of the person
"""

print("Welcome to the rollercoaster")

height = int(input("What is your height in cm? "))

if height > 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age < 12:
        print("Please pay R5")
    elif age <=18:
        print("Please pay R12")
    else:
        print("Please pay R15")
else:
    print("Sorry, you need to grow taller! The minimum height requirement is 120cm.")