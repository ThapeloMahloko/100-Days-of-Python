"""
Random List Picker
======================================================
Create a program that asks the user for five favorite foods and stores them in a list. 
Then, randomly pick one item from the list and display it
"""
# Import the random module to generate a random index
import random

# Create an empty list to store the user's favorite foods
favorite_foods = []

# Ask the user for five favorite foods and store them in the list
food_1 = input("Enter your first favorite food: ")
food_2 = input("Enter your second favorite food: ")
food_3 = input("Enter your third favorite food: ")
food_4 = input("Enter your fourth favorite food: ")
food_5 = input("Enter your fifth favorite food: ")

# Add the user's favorite foods to the list
favorite_foods.append(food_1)
favorite_foods.append(food_2)
favorite_foods.append(food_3)
favorite_foods.append(food_4)
favorite_foods.append(food_5)

# Use the random module to generate a random index
random_index = random.randint(0, len(favorite_foods) - 1)

# Display the randomly picked food
print("Your randomly picked favorite food is: ", favorite_foods[random_index])