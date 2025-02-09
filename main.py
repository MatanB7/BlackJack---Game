import art
import random

def draw_card(hand, deck):
    """Deal a card from the deck"""
    index = random.randint(0,len(deck) - 1)
    card = deck[index]
    hand.append(card)

def sum_of_cards(hand):
    if sum(hand) >21 and 11 in hand:
        hand.remove(11)
        hand.append(1)
    return sum(hand)

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
keep_play = True
while keep_play:
    player_choice = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
    if player_choice == "y":
        keep_play =True
    elif player_choice == "n":
        keep_play = False
        break
    else:
        continue # You need to chose 'y' or 'n'.
    ## Restart the game and clean all the data.
    print("\n" * 20)
    print(art.logo)
    Player_cards = []
    Dealer_cards = []
    draw_card(Player_cards,cards)
    draw_card(Player_cards,cards)
    draw_card(Dealer_cards,cards)

    another = "y"
    while another == "y":
        print(f"Your cards: {Player_cards}, current score: {sum_of_cards(Player_cards)}")
        print(f"Computer's first card: {Dealer_cards}")
        another = input("Type 'y' to get another card, type 'n' to pass: ").lower()
        player_went_over = False
        if another == "y":
            draw_card(Player_cards,cards)
            if sum_of_cards(Player_cards) > 21:
                player_went_over = True
                break ## need to go out of the while loop.

    while sum_of_cards(Dealer_cards) < 17 and not player_went_over:
        draw_card(Dealer_cards,cards)

    if sum_of_cards(Dealer_cards) > 21:
        dealer_went_over = True
    else:
        dealer_went_over = False

    print(f"Your final hand: {Player_cards}, final score: {sum_of_cards(Player_cards)}")
    print(f"Computer's final hand: {Dealer_cards}, final score: {sum_of_cards(Dealer_cards)}")
    if player_went_over:
        print("You went over! you lose )=")
    elif dealer_went_over:
        print("Dealer went over! you win (=")
    elif sum_of_cards(Player_cards) > sum_of_cards(Dealer_cards):
        print("You win. You got the higher score (=")
    elif sum_of_cards(Dealer_cards) > sum_of_cards(Player_cards):
        print("You lose. Dealer got the higher score )=")
    else:
        print("It's a drew!")

print("Game Over")

