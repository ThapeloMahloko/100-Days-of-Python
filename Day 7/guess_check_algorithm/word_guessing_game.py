"""
Word Guessing Game

This script implements a simple guessing game where the user tries to guess a predefined word.
"""

def word_guessing_game():
    predefined_word = "python"
    guess = ""
    
    print("Welcome to the Word Guessing Game!")
    print("Try to guess the predefined word.")

    while guess != predefined_word:
        guess = input("Enter your guess: ").lower()
        if guess == predefined_word:
            print("Congratulations! You've guessed the word!")
        else:
            print("Incorrect guess. Try again.")

# Uncomment the following line to play the word guessing game
if __name__ == "__main__":
    word_guessing_game()
