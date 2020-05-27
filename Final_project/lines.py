from tkinter import *
from random import *

def random_color():
    return f'#{randint(0,0xffffff):06x}'

def random_line(event):
    for i in range(50):
        x1 = randint(0, 200)
        y1 = randint(0, 200)
        x2 = randint(0, 200)
        y2 = randint(0, 200)
        random_width = randint(0, 10)
        canvas.create_line(x1, y1, x2, y2, width=random_width, fill=random_color())

def clear_canvas(event):
    canvas.delete('all')

window = Tk()
window.title("Lines drawer")
canvas = Canvas(window, width=300, height=300, bg="#ff9950")
canvas.grid(row=0, column=0)
button1 = Button(window, text="Draw a random color line", command=random_line)
button2 = Button(window, text="Clear canvas", command=clear_canvas)
button1.grid(row=1, column=0)
button2.grid(row=2, column=0)

# canvas.bind('<Button-1>', random_line)
# canvas.bind('<Button-3>', clear_canvas)
canvas.grid(row=0, column=0)
window.mainloop()

