"""
Lottery Number Generator
Write a program that generates a list of six random numbers between 1 and 49 for a lottery ticket.
Make sure the numbers are unique.
"""
# Import the random module to generate random numbers
import random

# Lottery Numbers 
lottery_numbers = []
# Generate six unique random numbers between 1 and 49
num_1 = random.randint(1,49)
num_2 = random.randint(1,49)
num_3 = random.randint(1,49)
num_4 = random.randint(1,49)
num_5 = random.randint(1,49)
num_6 = random.randint(1,49)

# Lottery List
lottery_numbers = [num_1, num_2, num_3, num_4, num_5, num_6]