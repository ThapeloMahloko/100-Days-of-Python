"""
Word Shuffle
============================================================
Write a program that takes a sentence as input, splits it into words, 
and shules the words randomly. Print the shuled sentence.
"""
# Import random module
import random
# Get the sentence from the user
sentence = input("Enter a sentence: ")

# Split the sentence into words
words = sentence.split()

# Shuffle the words
random.shuffle(words)

# Join the words back into a sentence
shuffled_sentence = ' '.join(words)

# Print the shuffled sentence
print(shuffled_sentence)