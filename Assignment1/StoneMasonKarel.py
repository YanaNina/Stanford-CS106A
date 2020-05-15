from karel.stanfordkarel import *

"""
File: StoneMasonKarel.py
------------------------
When you finish writing code in this file, StoneMasonKarel should 
solve the "repair the quad" problem from Assignment 1. You
should make sure that your program works for all of the 
sample worlds supplied in the starter folder.
"""

""" Pre-condition: karel facing east at bottom
    Post-condition: karel facing east at bottom
Karel builds a column """
def build_column():
    turn_left()
    going_up()
    going_down()
    turn_left()

""" Karel goes up and places beepers where they needed"""
def going_up():
    while front_is_clear():
        if no_beepers_present():
            put_beeper()
        move()
    if no_beepers_present():
        put_beeper()

"""Karel returns down to bottom """
def going_down():
    turn_around()
    while front_is_clear():
        move()

"""Karel turns around"""
def turn_around():
    for i in range(2):
        turn_left()

""" Karel walks from current column to next column"""
def walk_beetween_columns():
    for i in range(4):
        move()

""" Karel rebuilds a wall. Missing stones in the columns should be replaced by beepers.
The columns are always exactly four corners apart"""
def main():
    while front_is_clear():
        build_column()
        walk_beetween_columns()
    build_column()

# There is no need to edit code beyond this point

if __name__ == "__main__":
    run_karel_program()
