from karel.stanfordkarel import *
"""
File: ExtensionKarel.py
------------------------
"""

""" Karel paints perimeter
    Pre-condition: facing east , staying in the bottom left corner of the world
    Post-condition: facing east , staying in the bottom left corner of the world
"""
def paint_outerperimeter():
    for i in range(4):
        paint_each_side()
        turn_left()

""" Karel paints each side of the perimeter
    Pre-condition: staying in the not-colored corner
    Post-condition: staying in the not-colored corner 
    facing the same direction as when started
"""
def paint_each_side():
    while front_is_clear():
        paint_corner(LIGHT_GRAY)
        move()
        if front_is_clear():
            paint_corner(BLACK)
            move()

""" Karel paints 2 x inner perimeters"""
def paint_inner_perimetr():
    for i in range(4):
        paint_each_side_black()
        turn_left_innerperimeter()
    for i in range(4):
        paint_each_side_orange()
        turn_left_innerperimeter()

""" Karel paints bigger perimeter of two in black"""
def paint_each_side_black():
    while corner_color_is(BLANK):
        paint_corner(BLACK)
        move()

""" Karel turns left in the corner"""
def turn_left_innerperimeter():
    turn_left()
    turn_left()
    move()
    turn_right()
    move()

""" Karel paints smaller perimeter of two in orange"""
def paint_each_side_orange():
    while corner_color_is(BLANK):
        paint_corner(ORANGE)
        move()

def turn_right():
    for i in range(3):
        turn_left()

""" Karel goes from outer perimetr to inner"""
def change_perimeter():
    turn_left()
    move()
    turn_right()
    move()

""" Karel paints world into black-orange square inside gray-black -colored rim"""
def main():
    paint_outerperimeter()
    change_perimeter()
    while corner_color_is(BLANK):
        paint_inner_perimetr()


# There is no need to edit code beyond this point

if __name__ == "__main__":
    run_karel_program()
