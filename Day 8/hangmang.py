import random


# List of words
word_list = ["apple", "banana", "cherry", "date", "elderberry"]

# Randomly choosing a word from a list
chosen_word = random.choice(word_list)
print(chosen_word)
print("_ " * len(chosen_word))


display = "_"
attempts = 10

while '_' in display and attempts > 0:
    guess = input("Guess the letter in the word: ").lower()
    for letter in chosen_word:
        if letter == guess:
         display += letter
        else:
            display += "_"
    print(display)