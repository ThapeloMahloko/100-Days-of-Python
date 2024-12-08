"""
Random Number Guessing
===============================================
Write a program that generates a random number between 1 and 20.
The users has to guess the number, and the program gives hints like
"Too high" or "Too Low" until the user guesses the number correctly.
"""
# Get the number that user guessed
user_guess = int(input("Guess a number between 1 and 20: "))
# Generate a random number between 1 and 20
import random
random_number = random.randint(1, 20)

# Check if the user guessed the number correctly
if user_guess == random_number:
    print("Congratulations, you guessed the number correctly!")
elif user_guess <= random_number:
    print("Too low, try again!")
else:
    print("Too high, try again!")