import random

scissors = '''
   ____
  / __ \\
 ( (__) |___ ___
  \________,'   """""----....____
   _______<  () dd       ____----'
  / __   __`.___-----""""
 ( (__) |
  \____/
'''

paper = '''
      _.--._  _.--._
,-=.-":;:;:;\':;:;:;"-._
\\\:;:;:;:;:;\:;:;:;:;:;\\n
 \\\:;:;:;:;:;\:;:;:;:;:;\\n
  \\\:;:;:;:;:;\:;:;:;:;:;\\n
   \\\:;:;:;:;:;\:;::;:;:;:\\n
    \\\;:;::;:;:;\:;:;:;::;:\\n
     \\\;;:;:_:--:\:_:--:_;:;\\n 
      \\\_.-"      :      "-._\\n
       \`_..--""--.;.--""--.._=>
        "

'''

rock = '''                              R|O|C|K|
        \                              /\| | | |
         \                            / /|_|_|_|
          \                           \        |
            (  ( ) ) ( )  )            \_______/
           ( ( ( ( )  )  ) )           /______/
          ( ( )) ) (   ) ( ( )        /       /
          ( (__.-.___.-.__) )        /       /
          / ---._.---._.---\        /       /
          \||    '/  '   ||/       /       /
            |||  (_     |||       /       /
             || ///\\\  ||\______/       /
        ___/ ||||\__/|||||/             /
       /   \   ||||||||  /             /
      /     \   ||||||  /        _____/
'''

active_game = True
available_option = [rock,scissors,paper]
player_choice = int(input("What do you want to chose? 0 for rock, 1 for scissors, 2 for paper and anything else to lose instantly: "))

comp_choices = [0,1,2]

random_choice = random.choice(comp_choices)

game_result = 0

if not active_game:
    print("You have alread lost....")
else:
    if random_choice == 0:
        if player_choice == 0:
            game_result = 0
        elif player_choice == 1:
            game_result = 1
        elif player_choice == 2:
            game_result = 2
        else:
            print("There was an error with the game! :(")
    elif random_choice == 1:
        if player_choice == 0:
            game_result = 2
        elif player_choice == 1:
            game_result = 0
        elif player_choice == 2:
            game_result = 1
        else:
            print("There was an error with the game! :(")
    elif random_choice == 2:
        if player_choice == 0:
            game_result = 1
        elif player_choice == 1:
            game_result = 2
        elif player_choice == 2:
            game_result = 0
        else:
            print("There was an error with the game! :(")
    else:
        print("There was an error with the comp choice! :(")       

if game_result == 2:
    print("You chose.... \n")
    print(available_option[player_choice])
    print("Computer chose....\n")
    print(available_option[random_choice])
    print("Congratulations! You won!!!")
    
elif game_result == 1:
    print("You chose.... \n")
    print(available_option[player_choice])
    print("Computer chose....\n")
    print(available_option[random_choice])
    print("Sorry! You lose!")
    
elif game_result == 0:
    print("You chose.... \n")
    print(available_option[player_choice])
    print("Computer chose....\n")
    print(available_option[random_choice])
    print("It is a draw!")
else:
    print("Error with game!!")