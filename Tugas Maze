def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def maze():
    if not wall_in_front():
        move()
        if at_goal():
            done
        elif not wall_on_right():
            turn_right()
    else:
        turn_left()    
       
while not at_goal():
    maze()
