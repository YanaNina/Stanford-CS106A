from karel.stanfordkarel import * 

"""
File: MidpointKarel.py
----------------------
When you finish writing it, MidpointKarel should
leave a beeper on the corner closest to the center of 1st Street
(or either of the two central corners if 1st Street has an even
number of corners).  Karel can put down additional beepers as it
looks for the midpoint, but must pick them up again before it
stops.  The world may be of any size, but you are allowed to
assume that it is at least as tall as it is wide.
"""

""" Karel steps forward two times and paint corner
    Pre-condition: facing east
    Post-condition: facing east, corner is painted"""
def walk_forward_paintcorner():
    if front_is_clear():
        move()
    if front_is_clear():
        move()
        paint_corner(RED)

""" Karel goes back and moves beeper one cell forward
    Pre-condition: facing east,staying at painted corner
    Post-condition: facing east,beeper is present
"""
def walk_back_move_beeper():
    if corner_color_is(RED):
        turn_around()
        while no_beepers_present():
            move()
        pick_beeper()
        turn_around()
        move()
        put_beeper()

def turn_around():
    turn_left()
    turn_left()

""" Karel finds painted cell and paint it back to blank
    Pre-condition: facing east, beeper present
    Post-condition : facing east, corner is blank
"""
def walk_until_colored():
    if beepers_present():
        while corner_color_is(BLANK):
            move()
        paint_corner(BLANK)

def back_to_final():
    turn_around()
    while no_beepers_present():
        move()

""" Karel places a single beeper at the center of 1st row"""
def main():
    put_beeper()
    while front_is_clear():
        walk_forward_paintcorner()
        walk_back_move_beeper()
        walk_until_colored()
    back_to_final()


# There is no need to edit code beyond this point

if __name__ == "__main__":
    run_karel_program()
