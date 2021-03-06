from karel.stanfordkarel import *

"""
File: CollectNewspaperKarel.py
------------------------------
At present, the CollectNewspaperKarel file does nothing.
Your job in the assignment is to add the necessary code to
instruct Karel to walk to the door of its house, pick up the
newspaper (represented by a beeper, of course), and then return
to its initial position in the upper left corner of the house.
"""

""" Karel goes till reach a newspaper and picks it up """
def go_check_newspaper():
    move()
    move()
    turn_right()
    move()
    turn_left()
    move()
    pick_beeper()

def turn_right():
    for i in range(3):
        turn_left()

""" Karel goes back to place """
def back_to_place():
    turn_around()
    move()
    turn_right()
    move()
    turn_left()
    move()
    move()

def turn_around():
    turn_left()
    turn_left()

def main():
    go_check_newspaper()
    back_to_place()

# There is no need to edit code beyond this point

if __name__ == "__main__":
    run_karel_program()
