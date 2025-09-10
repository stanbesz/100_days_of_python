import random as rand

def presentation():
    print(""" __          __  _                            _          _   _            _   _                 _                  _____                     _                                          _ 
 \ \        / / | |                          | |        | | | |          | \ | |               | |                / ____|                   (_)                                        | |
  \ \  /\  / /__| | ___ ___  _ __ ___   ___  | |_ ___   | |_| |__   ___  |  \| |_   _ _ __ ___ | |__   ___ _ __  | |  __ _   _  ___  ___ ___ _ _ __   __ _    __ _  __ _ _ __ ___   ___| |
   \ \/  \/ / _ \ |/ __/ _ \| '_ ` _ \ / _ \ | __/ _ \  | __| '_ \ / _ \ | . ` | | | | '_ ` _ \| '_ \ / _ \ '__| | | |_ | | | |/ _ \/ __/ __| | '_ \ / _` |  / _` |/ _` | '_ ` _ \ / _ \ |
    \  /\  /  __/ | (_| (_) | | | | | |  __/ | || (_) | | |_| | | |  __/ | |\  | |_| | | | | | | |_) |  __/ |    | |__| | |_| |  __/\__ \__ \ | | | | (_| | | (_| | (_| | | | | | |  __/_|
     \/  \/ \___|_|\___\___/|_| |_| |_|\___|  \__\___/   \__|_| |_|\___| |_| \_|\__,_|_| |_| |_|_.__/ \___|_|     \_____|\__,_|\___||___/___/_|_| |_|\__, |  \__, |\__,_|_| |_| |_|\___(_)
                                                                                                                                                      __/ |   __/ |                       
                                                                                                                                                     |___/   |___/ """)
    print("I am thinking of a number between 1 and 100. try to guess it!")
    choice = input("Choose a difficulty! Type 'easy' or 'hard': ").lower()

    guesses = 0

    if choice == "easy":
        guesses = 10
    elif choice == "hard":
        guesses = 5
    else:
        print("Please learn to type!!!")
        return
    
    return guesses

def game():
    try:
        choices = int(presentation())
    except TypeError:
        print("Inavlid choice!")
        return
    
    number_to_guess = rand.randint(1,100)
    number_guess = 0
    won_game = False
    while choices > 0:
        number_guess = input("Make a guess: ")
        
        try:
            number_guess = int(number_guess)
        except ValueError:
            print("That is not an int!")
            break

        if number_guess > number_to_guess:
            print("Too High! Try again!")
            choices-=1
        elif number_guess < number_to_guess:
            print("Too small! Try again!")
            choices-=1
        else:
            print("Congrats you found the number!")
            won_game = True
            break

        print(f"You have {choices} left!")

    if choices == 0 and not won_game:
        print("""You Lost!""")
game()