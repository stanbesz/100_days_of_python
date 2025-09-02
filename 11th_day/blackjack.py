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

dealer_hand = []
dealer_score = 0
player_hand = []
player_score = 0

while game_active:
    dealer_hand.append(rand.choice(cards))
    print(f"Dealer has the following cards: {dealer_hand}")

    player_hand.append(rand.choice(cards))
    player_hand.append(rand.choice(cards))
    print(f"You have the following cards: {player_hand}")
    choice_option = input("Do you want to hit or stand? Type 'y' for hit, 'n' for stand and 'exit' for exiting the game: ").lower()

    if choice_option == "y":
        player_score = sum(player_hand)
        while choice_option == "y" and player_score <= 21:
            player_hand.append(rand.choice(cards))
            print(f"You have the following cards: {player_hand}")
            choice_option = input("Do you want to hit or stand? Type 'y' for hit, 'n' for stand and 'exit' for exiting the game: ").lower()
    elif choice_option == "n":
        dealer_score = sum(dealer_hand)
        while dealer_score < 17:
            dealer_hand.append(rand.choice(cards))
            dealer_score = sum(dealer_hand)

    elif choice_option == "exit":
        print("Please come again")
        break
    else:
        print("Error with input")
        break

    if dealer_score > player_score:
        print("You have lost :( Sorry!")
    elif dealer_score < player_score:
        print("You have won :) congrats!")
    elif dealer_score == player_score:
        print("It is a draw!!!")