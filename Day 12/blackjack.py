"""
Blackjack game implementation.This script simulates a simple game of Blackjack.
It allows a player to play against a dealer, following standard Blackjack rules.
The player can hit or stand, and the dealer will hit until reaching a score of 17  
or higher.
The game continues until the player decides to stop playing.
"""
import random 

def deal_card():
    """Returns a random card from the deck."""
    cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]  # J, Q, K are represented as 10 and A as 11
    return random.choice(cards)

def calculate_score(hand):
    """Calculates the score of a hand."""
    score = sum(hand)
    if score == 21 and len(hand) == 2:
        return 0  # Blackjack
    if 11 in hand and score > 21:
        hand.remove(11)
        hand.append(1)  # Convert Ace from 11 to 1
        score = sum(hand)
    return score

def compare(player_score, dealer_score):
    """Compares the scores of the player and dealer."""
    if player_score == dealer_score:
        return "Draw"
    elif dealer_score == 0:
        return "Lose, opponent has Blackjack"
    elif player_score == 0:
        return "Win with a Blackjack"
    elif player_score > 21:
        return "You went over. You lose"
    elif dealer_score > 21:
        return "Opponent went over. You win"
    elif player_score > dealer_score:
        return "You win"
    else:
        return "You lose"

def play_blackjack():
    """Main function to play the Blackjack game."""
    print("Welcome to Blackjack!")
    
    player_hand = [deal_card(), deal_card()]
    dealer_hand = [deal_card(), deal_card()]

    game_over = False

    while not game_over:
        player_score = calculate_score(player_hand)
        dealer_score = calculate_score(dealer_hand)

        print(f"   Your cards: {player_hand}, current score: {player_score}")
        print(f"   Dealer's first card: {dealer_hand[0]}")

        if player_score == 0 or dealer_score == 0 or player_score > 21:
            game_over = True
        else:
            should_continue = input("Type 'y' to get another card, type 'n' to pass: ")
            if should_continue == 'y':
                player_hand.append(deal_card())
            else:
                game_over = True

    while dealer_score != 0 and dealer_score < 17:
        dealer_hand.append(deal_card())
        dealer_score = calculate_score(dealer_hand)

    print(f"   Your final hand: {player_hand}, final score: {player_score}")
    print(f"   Dealer's final hand: {dealer_hand}, final score: {dealer_score}")
    print(compare(player_score, dealer_score))

if __name__ == "__main__":
    while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == 'y':
        play_blackjack()
    print("Thanks for playing!")

