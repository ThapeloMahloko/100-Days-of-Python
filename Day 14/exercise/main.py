"""
Higer Lower game to compare the number of followers of two accounts.
"""


import random
from game_data import data
from art import logo, vs

def choose_random_acc():
    """
    Choose an account at random
    """
    new_acc = random.choice(data)
    return new_acc

def compare_users(user_A: dict, user_B:dict):
    """
    Compare the number of follower between 2 users
    
    Args:
        user_A (dict): Dictionary containing user information
        user_A (dict): Dictionary containing user information

    Return:
        str either it is "A" or "B".
    """
    followers_A = user_A["follower_count"]
    followers_B = user_B["follower_count"]
    if followers_A > followers_B:
        return "A"
    else:
        return "B"

def play_game():
    score = 0
    acc_A = None
    acc_B = None
    for i in range(5):
        print(logo)
        if acc_A == None:
            acc_A = choose_random_acc()
        else: 
            acc_A = acc_B

        if acc_B == acc_A or acc_B == None:
            acc_B = choose_random_acc()
        
        result = compare_users(acc_A, acc_B)

        print(f"Compare A: {acc_A["name"]}, {acc_A["description"], {acc_A["country"]}}")
        print(vs)
        print(f"Against B: {acc_B["name"]}, {acc_B["description"], {acc_B["country"]}}")
        response = input("Who has more followers? Type 'A' or 'B':").upper()
        if result == response:
            score += 1
            print("Correct!!!")
        else:
            print("Inccorrect!!!")
    
    print(f"Your got {score}/5.")

if __name__ == "__main__":
    play_game()