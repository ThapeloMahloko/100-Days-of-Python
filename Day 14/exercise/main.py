"""
Higher Lower game to compare the number of followers of two accounts.
"""

import random
from game_data import data
from art import logo, vs

def choose_random_acc():
    """
    Choose an account at random
    """
    return random.choice(data)

def compare_users(user_A: dict, user_B: dict):
    """
    Compare the number of followers between 2 users

    Args:
        user_A (dict): Dictionary containing user A's information
        user_B (dict): Dictionary containing user B's information

    Returns:
        str: Either "A" or "B", depending on who has more followers.
    """
    if user_A["follower_count"] > user_B["follower_count"]:
        return "A"
    else:
        return "B"

def play_game():
    score = 0
    acc_A = None
    acc_B = None

    for i in range(5):
        print(logo)

        if acc_A is None:
            acc_A = choose_random_acc()
        
        acc_B = choose_random_acc()
        while acc_B == acc_A:
            acc_B = choose_random_acc()
        
        print(f"Compare A: {acc_A['name']}, {acc_A['description']}, from {acc_A['country']}")
        print(vs)
        print(f"Against B: {acc_B['name']}, {acc_B['description']}, from {acc_B['country']}")

        result = compare_users(acc_A, acc_B)
        response = input("Who has more followers? Type 'A' or 'B': ").upper()

        if response == result:
            score += 1
            print("Correct!!!")
            acc_A = acc_B  # move forward with B
        else:
            print("Incorrect!!!")
            break  # exit early on wrong guess

    print(f"You got {score}/5.")

if __name__ == "__main__":
    play_game()
