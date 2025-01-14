"""
Create a Python program that generates a random password based on user input. The program should:

Ask the user for the following inputs:

The number of letters they want in their password.
The number of symbols they want in their password.
The number of numbers they want in their password.
Generate a list of random characters for each category:

Letters can be uppercase or lowercase (e.g., 'A', 'b').
Symbols can be chosen from a predefined list (e.g., ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+']).
Numbers can be any digit from 0 to 9.
Combine the generated characters into a list, shuffle the list, and then display:

The unshuffled list.
The shuffled list.
The final password as a single string.
"""
import random
import string
password_list = []

num_letters = input("How many letters should be in the password?\n ")
num_digits = input("How many digits should be in the password?\n ")
num_symbols = input("How many symbols should be in the password?\n ")

for i in range(int(num_letters)):
    password_list.append(random.choice(string.ascii_letters))

for i in range(int(num_digits)):
    password_list.append(random.choice(string.digits))

for i in range(int(num_symbols)):
    password_list.append(random.choice(string.punctuation))

print(password_list)
# Shuffle the list
random.shuffle(password_list)
password = "".join(password_list)
print(password)