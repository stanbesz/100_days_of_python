import random as rand

cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]

print("""
 _     _            _    _            _    
| |   | |          | |  (_)          | |   
| |__ | | __ _  ___| | ___  __ _  ___| | __
| '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
| |_) | | (_| | (__|   <| | (_| | (__|   < 
|_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\ 
                       _/ |                
                      |__/ 

                   .------.------.------.------.
                   |A_  _ |A /\  |A _   |A .   |
                   |( \/ )| /  \ | ( )  | / \  |
                   | \  / | \  / |(_x_) |(_,_) |
                   |  \/ A|  \/ A|  Y  A|  I  A|
                   `------^------^------'------'     
      """)

game_active = True


def end_conditions(player_score,dealer_score):
    if player_score > 21:
        print("You have busted... You lose")
        return

    if dealer_score > 21:
        print("The dealer has busted... You win")
        return

    if dealer_score > player_score:
        print("You have lost :( Sorry!")
    elif dealer_score < player_score:
        print("You have won :) congrats!")
    elif dealer_score == player_score:
        print("It is a draw!!!")

def score_calculation_player(player_hand,choice_option):
    while choice_option == "y":
            add_hand = rand.choice(cards)
            player_hand.append(add_hand)
            if add_hand == 11 and sum(player_hand) > 21:
                player_hand.pop()
                player_hand.append(1)
                player_score = sum(player_hand)
            else:
                player_score = sum(player_hand)

            if player_score > 21:
                return player_score
            else:
                print(f"You have the following cards: {player_hand}")
                choice_option = input("Do you want to hit or stand? Type 'y' for hit, 'n' for stand and 'exit' for exiting the game: ").lower()
    return player_score

def score_calculation_dealer(dealer_hand):
        dealer_score = sum(dealer_hand)
        while dealer_score < 17:
            add_hand = rand.choice(cards)
            dealer_hand.append(add_hand)
            if add_hand == 11 and sum(dealer_hand) > 21:
                dealer_hand.pop()
                dealer_hand.append(1)
                dealer_score = sum(dealer_hand)
            else:
                dealer_score = sum(dealer_hand)


            if dealer_score > 21:
                return dealer_score
        return dealer_score

while game_active:
    dealer_hand = []
    dealer_score = 0
    player_hand = []
    player_score = 0

    dealer_hand.append(rand.choice(cards))
    print(f"Dealer has the following cards: {dealer_hand}")

    player_hand.append(rand.choice(cards))
    player_hand.append(rand.choice(cards))
    print(f"You have the following cards: {player_hand}")
    choice_option = input("Do you want to hit or stand? Type 'y' for hit, 'n' for stand and 'exit' for exiting the game: ").lower()

    if choice_option == "y":
        player_score = score_calculation_player(player_hand,choice_option)

    elif choice_option == "n":
        dealer_score = score_calculation_dealer(dealer_hand)

    elif choice_option == "exit":
        print("Please come again")
        break
    else:
        print("Error with input")
        break

    player_score = sum(player_hand)

    end_conditions(player_score,dealer_score)
