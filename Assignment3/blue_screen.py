"""
File: bluescreen.py
----------------
Not part of the assignment. This was a lecture demo!
This is a fun algorithm to implement. It is not in the
assignment, but feel free to implement it as an extension.
Put the smaller foreground picture into the background.
Do not include any pixels that are sufficiently blue.
"""

from simpleimage import SimpleImage

INTENSITY = 1.9

def main():
    foreground = SimpleImage('images/tiefighter.jpg')
    background = SimpleImage('images/quad.jpg')
    foreground.show()
    background.show()

    for x in range(foreground.width):
        for y in range(foreground.height):
            pixel = foreground.get_pixel(x, y)
            if pixel.blue < (pixel.blue + pixel.green + pixel.red) // 3 * INTENSITY:
                background.set_pixel(x, y, pixel)


    background.show()



if __name__ == '__main__':
    main()