def turn_right():
    turn_left()
    turn_left()
    turn_left()

def hurdle():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

def climb_up():
    turn_left()
    move()
    turn_right()

def climb_down():
    turn_right()
    move()
    turn_left()
    
    
while not at_goal():
    if not front_is_clear():
        while wall_in_front():
            climb_up()
        move()
        turn_right()
        while not wall_in_front():
            move()
        turn_left()
    elif front_is_clear():
        move()

