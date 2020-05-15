from karel.stanfordkarel import *
"""
File: TripleKarel.py
--------------------
When you finish writing this file, TripleKarel should be
able to paint the exterior of three buildings in a given
world, as described in the Assignment 1 handout. You
should make sure that your program works for all of the 
Triple sample worlds supplied in the starter folder.
"""

"""Karel paints three sides of one building
    Pre-condition : there is a wall to his left
    Post-condition: there is wall to his left """
def painting_one_building():
    for i in range(2):
        go_along_the_wall()
        corner_turn()
    go_along_the_wall()
    turn_right()

def turn_right():
    for i in range(3):
        turn_left()

""" Karel moves along the wall and puts beepers"""
def go_along_the_wall():
    while left_is_blocked():
        put_beeper()
        move()

""" When Karel reach corner he turns left"""
def corner_turn():
    turn_left()
    move()

"""Karel paints the exterior of three building using beepers """
def main():
    for i in range(3):
        painting_one_building()
    turn_left()


# There is no need to edit code beyond this point

if __name__ == "__main__":
    run_karel_program()
