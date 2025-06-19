"""
This module is a guessing numbers game
"""
import random
from art import logo

def guessing_game():
    print(logo)
    print("Welcome to the Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    number_to_guess = random.randint(1, 100)
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    attempts = 10 if difficulty == 'easy' else 5
    print(f"You have {attempts} attempts to guess the number.")
    while attempts > 0:
        print(f"You have {attempts} attempts remaining.")
        guess = int(input("Make a guess: "))
        
        if guess < number_to_guess:
            print("Too low.")
        elif guess > number_to_guess:
            print("Too high.")
        else:
            print(f"Congratulations! You guessed the number {number_to_guess} correctly!")
            return
        
        attempts -= 1
        if attempts == 0:
            print(f"You've run out of attempts. The number was {number_to_guess}. Better luck next time!")

if __name__ == "__main__":
    guessing_game()