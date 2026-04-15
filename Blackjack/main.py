import random
import os
import time

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def create_deck():
    """
    Creates a standard 52-card deck.
    Card values:
    2-10: Face value
    J, Q, K: 10
    A: 11 (flexible, handled in calculate_hand_value)
    """
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    deck = [(rank, suit) for suit in suits for rank in ranks]
    random.shuffle(deck)
    return deck

def deal_card(deck):
    if not deck:
        # If deck is empty, create and shuffle a new one (or multiple decks)
        print("Reshuffling deck...")
        deck.extend(create_deck()) # Add a new deck to the current empty one
        random.shuffle(deck)
    return deck.pop()

def calculate_hand_value(hand):
    value = 0
    num_aces = 0
    
    for card in hand:
        rank = card[0]
        if rank.isdigit():
            value += int(rank)
        elif rank in ['J', 'Q', 'K']:
            value += 10
        elif rank == 'A':
            num_aces += 1
            value += 11 # Assume Ace is 11 initially

    # Adjust for Aces if value is over 21
    while value > 21 and num_aces > 0:
        value -= 10 # Change an Ace from 11 to 1
        num_aces -= 1
        
    return value

def display_hands(player_hand, dealer_hand, hide_dealer_card=True):
    clear_screen()
    print("--- BLACKJACK --- 🃏")
    
    # Dealer's Hand
    print("\nDealer's Hand:")
    if hide_dealer_card:
        print(f"  [{dealer_hand[0][0]} of {dealer_hand[0][1]}] [Hidden Card]")
    else:
        print(" ".join([f"[{card[0]} of {card[1]}]" for card in dealer_hand]))
        print(f"  Dealer Total: {calculate_hand_value(dealer_hand)}")

    # Player's Hand
    print("\nYour Hand:")
    print(" ".join([f"[{card[0]} of {card[1]}]" for card in player_hand]))
    print(f"  Your Total: {calculate_hand_value(player_hand)}")
    print("-" * 20)

def determine_winner(player_hand, dealer_hand):
    player_total = calculate_hand_value(player_hand)
    dealer_total = calculate_hand_value(dealer_hand)

    print("\n--- RESULTS ---")
    display_hands(player_hand, dealer_hand, hide_dealer_card=False) # Show both hands fully

    if player_total > 21:
        print("You BUSTED! Dealer wins. 😭")
    elif dealer_total > 21:
        print("Dealer BUSTED! You win! 🎉")
    elif player_total == dealer_total:
        print("It's a PUSH! (Tie) 🤝")
    elif player_total == 21:
        print("BLACKJACK! You win! 💰") # This should ideally be checked earlier if 2 cards
    elif dealer_total == 21:
        print("Dealer has BLACKJACK! Dealer wins. 😭") # This too
    elif player_total > dealer_total:
        print("You win! Your score is higher. 😄")
    else:
        print("Dealer wins! Dealer's score is higher. 😔")
    time.sleep(3) # Pause for a moment to show results

def blackjack_game():
    deck = create_deck()
    player_hand = []
    dealer_hand = []

    # Initial deal
    player_hand.append(deal_card(deck))
    dealer_hand.append(deal_card(deck))
    player_hand.append(deal_card(deck))
    dealer_hand.append(deal_card(deck))

    player_total = calculate_hand_value(player_hand)
    dealer_total = calculate_hand_value(dealer_hand)
    
    game_over = False

    # Check for immediate Blackjacks
    if player_total == 21 and dealer_total == 21:
        display_hands(player_hand, dealer_hand, hide_dealer_card=False)
        print("Both players have Blackjack! It's a PUSH! 🤝")
        game_over = True
    elif player_total == 21:
        display_hands(player_hand, dealer_hand, hide_dealer_card=False)
        print("BLACKJACK! You win! 💰")
        game_over = True
    elif dealer_total == 21:
        display_hands(player_hand, dealer_hand, hide_dealer_card=False)
        print("Dealer has BLACKJACK! You lose. 😭")
        game_over = True

    # Player's turn
    while not game_over:
        display_hands(player_hand, dealer_hand, hide_dealer_card=True)
        player_total = calculate_hand_value(player_hand)

        if player_total > 21:
            print("You BUSTED! 💥")
            game_over = True
            break # Exit player turn loop

        choice = input("Do you want to [H]it or [S]tand? ").lower()
        if choice == 'h':
            player_hand.append(deal_card(deck))
        elif choice == 's':
            print("You stand. Dealer's turn.")
            time.sleep(1)
            break # Exit player turn loop
        else:
            print("Invalid choice. Please enter 'H' or 'S'.")
            time.sleep(1)

    # Dealer's turn (only if player hasn't busted or gotten Blackjack)
    if not game_over:
        while calculate_hand_value(dealer_hand) < 17:
            display_hands(player_hand, dealer_hand, hide_dealer_card=False) # Show dealer's revealed card
            print(f"Dealer's current total: {calculate_hand_value(dealer_hand)}. Dealer hits.")
            time.sleep(1.5) # Pause to simulate dealing
            dealer_hand.append(deal_card(deck))
            
    # Determine winner after both turns (or if game was over earlier)
    determine_winner(player_hand, dealer_hand)


# Main game loop to play multiple rounds
# ... (all your function definitions)

def main():
    while True:
        clear_screen()
        print("Welcome to Console Blackjack! ♠️♥️♣️♦️")
        print("Try to get as close to 21 as possible without going over.")
        
        blackjack_game() # Play a single round

        while True:
            play_again = input("\nPlay another round? (yes/no): ").lower()
            if play_again in ['yes', 'y']:
                break
            elif play_again in ['no', 'n']:
                print("Thanks for playing! See you next time! 👋")
                return # Exit the main game loop
            else:
                print("Invalid input. Please enter 'yes' or 'no'.")

if __name__ == "__main__":
    main()
