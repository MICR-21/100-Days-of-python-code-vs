"""
BlackJack Game
Add up cards without going to 21 ,
> 21 you lose immediately, 
2-10 cards count as per face value,
J,Q,K count as 10,
Ace can count as 1 or 11,
Player can keep drawing cards until they bust or decide to stand,
Dealer must keep drawing cards until they reach 17,
If dealer score is greater than 21, player wins,
If player score is greater than dealer, player wins,
If dealer score is greater than player, dealer wins,
If both dealer and player have same score, it's a draw,
If dealer has score under 17, dealer must take another card,
use choices normal, hard,extra hard, expert to set difficulty level,
"""
import random
import art
print(art.logo)

# Define deck of cards (Ace is 11 initially)
cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 11]

def calculate_total(hand):
    total = sum(hand)
    aces = hand.count(11)

    # If total is over 21 and there's an Ace (11), convert it to 1
    while total > 21 and aces > 0:
        total -= 10  # Convert Ace from 11 to 1
        aces -= 1

    return total

def player_choice():
    card = random.choice(cards)
    player_cards.append(card)

def dealer_choice():
    card = random.choice(cards)
    dealer_cards.append(card)

def blackjack_game():
    global player_cards, dealer_cards  # Access global variables
    player_total = calculate_total(player_cards)
    dealer_total = calculate_total(dealer_cards)

    is_continue = True
    print(f"Your cards: {player_cards} (Current Score: {player_total})")
    print(f"The dealer's first card: {dealer_cards[0]}")

    while is_continue:
        if player_total > 21:
            print(f"You lose with {player_total}, and the dealer wins with {dealer_total}.")
            is_continue = False
        elif dealer_total > 21:
            print(f"Dealer loses with {dealer_total}, and you win with {player_total}.")
            is_continue = False
        else:
            choice = input("Do you want to pick another card? Type 'y' or 'n': ").strip().lower()
            if choice == 'y':
                player_choice()
                player_total = calculate_total(player_cards)
                print(f"Your cards are: {player_cards}, (Current Score: {player_total})")
            else:
                # Dealer's turn: Must keep drawing until at least 17
                while dealer_total < 17:
                    dealer_choice()
                    dealer_total = calculate_total(dealer_cards)

                print(f"Dealer's final hand: {dealer_cards}, (Final Score: {dealer_total})")

                # Game outcome
                if dealer_total > 21:
                    print(f"Dealer busts! You win with {player_total}.")
                elif dealer_total > player_total:
                    print(f"Dealer wins with {dealer_total}, and you lose with {player_total}.")
                elif dealer_total == player_total:
                    print("It's a draw.")
                else:
                    print(f"You win with {player_total}, and the dealer loses with {dealer_total}.")
                
                is_continue = False


    play_again = input("Do you want to play again? Type 'y' or 'n': ").strip().lower()
    if play_again == 'y':
        start_game()
    else:
        print("Goodbye!")
        exit()

def start_game():
    global player_cards, dealer_cards  # Reset hands
    player_cards = []
    dealer_cards = []
    
    player_choice()
    dealer_choice()
    blackjack_game()

game = input("Do you want to play? Type 'y' or 'n': ").lower()
if game == 'y':
    start_game()
else:
    print("Goodbye!")
    exit()
