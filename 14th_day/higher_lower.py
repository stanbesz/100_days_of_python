from game_data import data
import random as rand

game_running = True
current_score = 0

def printout(initial_entry,second_entry):
        
        print("""
  _    _ _       _                  
 | |  | (_)     | |                 
 | |__| |_  __ _| |__   ___ _ __    
 |  __  | |/ _` | '_ \ / _ \ '__|   
 | |  | | | (_| | | | |  __/ |      
 |_|  |_|_|\__, |_| |_|\___|_|      
      | |   __/ |                   
      | |  |___/___      _____ _ __ 
      | |    / _ \ \ /\ / / _ \ '__|
      | |___| (_) \ V  V /  __/ |   
      |______\___/ \_/\_/ \___|_|   
                                    
                                    """)
        global game_running,current_score
        if game_running and current_score>0:
            print(f"You're right! Current score: {current_score}")
        elif not game_running:
            print(f"Sorry that is wrong! Final score: {current_score}")
            return

        print(f"Compare A: {initial_entry['name']}, a {initial_entry['description']}, from {initial_entry['country']}")

        print("""
 __      __    
 \ \    / /    
  \ \  / /__   
   \ \/ / __|  
    \  /\__ \_ 
     \/ |___(_)
        """)

        print(f"Compare B: {second_entry['name']}, a {second_entry['description']}, from {second_entry['country']}")

def correct_choice(initial_entry,second_entry,choice):
        
        global game_running,current_score

        if choice == 'a':
            if initial_entry['follower_count'] > second_entry['follower_count'] :
                current_score = current_score + 1
                return second_entry
            else:
                print(f"Sorry that is wrong. Final score: {current_score}")
                game_running = False
                
        elif choice == 'b':
            if initial_entry['follower_count']  < second_entry['follower_count'] :
                current_score = current_score + 1
                return second_entry
            else:
                print(f"Sorry that is wrong. Final score: {current_score}")
                game_running = False
                
        else:
            print("Wrong input!")
            game_running = False

        return

def game_logic():
    global game_running,current_score

    initial_entry = rand.choice(data)
    second_entry = 0
    while game_running:
        second_entry = rand.choice(data)
        printout(initial_entry,second_entry)

        choice = input("Who has more followers? Type 'A' or 'B': ").lower()

        initial_entry = correct_choice(initial_entry,second_entry,choice)
    printout(initial_entry,second_entry)

game_logic()