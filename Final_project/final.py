import tkinter
import time
from simpleimage import SimpleImage
from PIL import ImageTk
from PIL import Image
from random import randint



CANVAS_WIDTH = 1000
CANVAS_HEIGHT = 1000
BALL_SIZE = 100
DOG_Y = CANVAS_HEIGHT-200


def main():

    canvas = make_canvas(CANVAS_WIDTH, CANVAS_HEIGHT, "Simba is Playng with a Bouncing Ball")
    image = ImageTk.PhotoImage(Image.open("dog.png"))
    dog = canvas.create_image(300, DOG_Y, image = image, anchor = "sw")

    ball = canvas.create_oval(300, 300, 300+BALL_SIZE, 300+BALL_SIZE, fill = "#c1cefa", outline="white",tag="barbie")
    rect_list = create_board(canvas)
    dx = 4
    dy = 12
    while True:
        mouse_x = canvas.winfo_pointerx()
        canvas.moveto(dog, mouse_x, DOG_Y)
        canvas.move(ball, dx, dy)
        if not rect_list:
            canvas.delete(ball)
            canvas.create_text(200, 510, anchor = 'w', font = 'Broadway 50',
                               text = 'Simba is Happy!', fill = "#eaa0a4")
            canvas.create_text(200, 560, anchor = 'w', font = 'Broadway 50',
                               text = 'Programming is Awesome!', fill = "#eaa0a4")
            random_line(canvas)
            canvas.update()
            time.sleep(15)
            break
        if hit_left_wall(canvas, ball) or hit_right_wall(canvas, ball):
            dx *= -1
        if hit_top_wall(canvas, ball):
            dy *= -1
        if hit_dog(canvas, dog):
            dy *= -1
        if hit_bottom_wall(canvas, ball):
            canvas.create_text(CANVAS_WIDTH // 2 - 50, 300, anchor = 'w', font = 'Broadway 22 ', text = 'Programming is Awesome!', fill = "#faedc1")
            canvas.move(ball, 300, 580)
        hit_tri(canvas, rect_list)
        canvas.update()
        time.sleep(1/50)


def create_board(canvas):
    part = 15
    tri_len = CANVAS_WIDTH / part
    n_y = 0
    rect_list = []
    for i in range(7):
        n_x = 0
        rect_height = 30
        for j in range(part):
            rect = canvas.create_rectangle(n_x, n_y, n_x + tri_len, n_y + rect_height, fill = "#f69f9e", outline="white")
            rect_list.append(rect)
            n_x += tri_len + (CANVAS_WIDTH % part)/part
        n_y += rect_height + 2
    return rect_list

def hit_dog(canvas, dog):
    dog_coord = canvas.coords(dog)
    x1 = dog_coord[0]
    y1 = dog_coord[1]
    x2 = x1 + 210
    y2 = y1 - 210
    result = canvas.find_overlapping(x1, y1, x2, y2)
    return len(result) > 1


def hit_tri(canvas, rect_list):
    for rect in rect_list:
        rect_coord = canvas.coords(rect)
        x1 = rect_coord[0]
        y1 = rect_coord[1]
        x2 = rect_coord[2]
        y2 = rect_coord[3]
        if len(canvas.find_overlapping(x1, y1, x2, y2)) > 1:
            canvas.delete(rect)
            rect_list.remove(rect)



def hit_bottom_wall(canvas, ball):
    return get_top_y(canvas, ball) > CANVAS_HEIGHT - BALL_SIZE


def hit_top_wall(canvas, ball):
    return get_top_y(canvas, ball) <= 0


def hit_left_wall(canvas, ball):
    return get_left_x(canvas, ball) <= 0


def hit_right_wall(canvas, ball):
    return get_left_x(canvas, ball) > CANVAS_WIDTH - BALL_SIZE


def get_left_x(canvas, object):
    return canvas.coords(object)[0]


def get_top_y(canvas, object):
    return canvas.coords(object)[1]


def get_right_x(canvas, object):
    return canvas.coords(object)[2]


def get_bottom_y(canvas, object):
    return canvas.coords(object)[3]


def random_color():
    return f'#{randint(100,0xffffff):06x}'


def random_line(canvas):
    for i in range(150):
        x1 = randint(0, CANVAS_WIDTH)
        y1 = randint(0, CANVAS_HEIGHT-500)
        x2 = randint(0, CANVAS_WIDTH)
        y2 = randint(0, CANVAS_HEIGHT-500)
        random_width = randint(0, 10)
        canvas.create_line(x1, y1, x2, y2, width=3, fill=random_color())
        canvas.update()
        time.sleep(1 / 50)

def make_canvas(width, height, title):
    """
    DO NOT MODIFY
    Creates and returns a drawing canvas
    of the given int size with a blue border,
    ready for drawing.
    """
    top = tkinter.Tk()
    top.minsize(width=width, height=height)
    top.resizable(width = False, height = False)
    top.title(title)
    canvas = tkinter.Canvas(top, width=width + 1, height=height + 1, bg="#616d7e")

    canvas.pack()
    return canvas


if __name__ == '__main__':
    main()