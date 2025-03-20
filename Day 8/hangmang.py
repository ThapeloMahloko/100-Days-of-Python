import random

shapes = [r''' 
  +---+ 
  |   | 
  O   | 
 /|\  | 
 / \  | 
      | 
=========''',
r'''
  +---+ 
  |   | 
  O   | 
 /|\  | 
 /    | 
      | 
=========''',
r'''
  +---+ 
  |   | 
  O   | 
 /|\  | 
      | 
      | 
=========''',
r'''
  +---+ 
  |   | 
  O   | 
 /|   | 
      | 
      | 
=========''',
r'''
  +---+ 
  |   | 
  O   | 
  |   | 
      | 
      | 
=========''',
r'''
  +---+ 
  |   | 
  O   | 
      | 
      | 
      | 
=========''',
r'''
  +---+ 
  |   | 
      | 
      | 
      | 
      | 
==========''']

# List of words
word_list = ["apple", "banana", "cherry", "date", "elderberry"]

# Randomly choosing a word from a list
chosen_word = random.choice(word_list)
place_holder = ""
for position in range(len(chosen_word)):
   place_holder += "_"
print(place_holder)

# Main Guessing Loop 
game_over = False
correct_letter = []
game_lives = 7
while not game_over:
    guess = input("Guess a letter: ").lower()
    display = ""
   # Check if the guessed letter is in the word
    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letter.append(guess)
        elif letter in correct_letter:
            display += letter
        else:
            display += "_"

    print(display)
    
    if guess not in chosen_word:
        game_lives -= 1
        
    print(shapes[game_lives - 1])
    if "_" not in display:
        game_over = True
        print("You win!")
    elif game_lives == 0:
        print("You lose the game!")
        game_over = True
