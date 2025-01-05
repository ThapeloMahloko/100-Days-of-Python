"""
Even or Odd Game 
Create a program that generates a random number between
1 and 100. The user must guess if the number is even or 
odd. After their guess, tell them whether they were 
correct or not
"""
# Import the random module
import random

# Random numbers varible 

random_number = random.randint(1,100)

# Check a if the random number is odd or even
if random_number % 2 == 0:
    print(f"The number {random_number} is even.")
else:
    print(f"The number {random_number} is odd.")