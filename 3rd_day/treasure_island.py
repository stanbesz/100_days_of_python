print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/______/_
*******************************************************************************
''')
print("Welcome to treasure island!")
print("Your mission is to find the treasure")

check_dead = False

direction = input("You are at a crossroad. Where do you want to go? ")
swim_direction = ''
door_color = ''

if direction.lower()=="left":
    swim_direction = input("You've come to a lake. There is an island in the middle of the lake. \n Type 'wait' to wait for a boat. Type 'swim' to swim accross. ")
else:
    print("Not all right paths are the 'right' paths. You wander until you die of exhaustion and thirst.")
    check_dead = True

if check_dead:
    print("You are already dead!")
else:
    if swim_direction.lower()=="wait":
        door_color = input("You've successfully reached the island. There are 3 houses, each with a distinct colour. One is red, one is blue and last one is yellow. \n Which one do you choose? ")
    else:
        print("You drowned... Congrats!")
        check_dead = True

if check_dead:
    print("You are already dead!")
else:
    if door_color.lower()=="yellow":
        door_color = input("You've successfully found the treasure! Congrats! ")
    else:
        print("You chose wrong... You are dead!")
        check_dead = True
