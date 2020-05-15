"""
This program generates the Warhol effect based on the original image.
"""

from simpleimage import SimpleImage
from random import uniform

N_ROWS = 2
N_COLS = 3
PATCH_SIZE = 222
WIDTH = N_COLS * PATCH_SIZE
HEIGHT = N_ROWS * PATCH_SIZE
PATCH_NAME = 'images/simba-sq.jpg'

def main():
    final_image = SimpleImage.blank(WIDTH, HEIGHT)
    n = 0  # width move
    m = 0  # height move
    for picture in range(2):
        for i in range(3):
            patch = make_recolored_patch(random_nums(), random_nums(), random_nums())
            for x in range(PATCH_SIZE):
                for y in range(PATCH_SIZE):
                    pixel = patch.get_pixel(x, y)
                    final_image.set_pixel(x + n, y + m, pixel)
            n += PATCH_SIZE
        m += PATCH_SIZE
        n = 0


    # This is an example which should generate a pinkish patch

    final_image.show()

def random_nums():
    color = round(uniform(0, 4), 1)
    return color

def make_recolored_patch(red_scale, green_scale, blue_scale):
    '''
    Implement this function to make a patch for the Warhol Filter. It
    loads the patch image and recolors it.
    :param red_scale: A number to multiply each pixels' red component by
    :param green_scale: A number to multiply each pixels' green component by
    :param blue_scale: A number to multiply each pixels' blue component by
    :return: the newly generated patch
    '''
    patch = SimpleImage(PATCH_NAME)
    for pixel in patch:
        pixel.red *= red_scale
        pixel.green *= green_scale
        pixel.blue *= blue_scale
    return patch

if __name__ == '__main__':
    main()