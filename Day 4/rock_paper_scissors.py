"""
Rock, Papers, Scissors Game
"""
# Import random module
import random

# Objects for the game
rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

# List of the objects
game_objects = [rock, paper, scissors]

# Get the player's input
player_choice = int(input("Enter a choice (rock = 0, paper = 1, scissors = 2): "))

# Random choice generator 
computer_choice = random.randint(0, 2)

# Conditions for the game
if (player_choice == 0) and (computer_choice == 1):
    print(game_objects[player_choice])
    print("Computers Choice:")
    print(game_objects[computer_choice])
    print("You lost and computer won!")
elif (player_choice == 1) and (computer_choice == 2):
    print(game_objects[player_choice])
    print("Computers Choice:")
    print(game_objects[computer_choice])
    print("You lost and computer won!")
elif (player_choice == 2) and (computer_choice == 0):
    print(game_objects[player_choice])
    print("Computers Choice:")
    print(game_objects[computer_choice])
    print("You lost and computer won!")
elif ((player_choice == 0) and (computer_choice == 0)) or ((player_choice == 1) and (computer_choice == 1)) or ((player_choice == 2) and (computer_choice == 2)):
    print(game_objects[player_choice])
    print("Computers Choice:")
    print(game_objects[computer_choice])
    print("It is draw!")
elif ((player_choice != 0) and (player_choice != 1) and (player_choice != 2)):
    print("You have entered an invalid number. You lost!")
else:
    print(game_objects[player_choice])
    print("Computers Choice:")
    print(game_objects[computer_choice])
    print("You won and computer lost!") 