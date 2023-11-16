def belok_kanan():
    turn_left()
    turn_left()
    turn_left()
    
def lompat():
    move()
    turn_left()
    move()
    belok_kanan()
    move()
    belok_kanan()
    move()
    turn_left()

while not at_goal():
    lompat()
