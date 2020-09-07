import tkinter
import time
import random
from constants import *
from Ball import Ball

N_BALLS = 10

def main():
    canvas = make_canvas(CANVAS_WIDTH, CANVAS_HEIGHT, 'Bouncing Ball')
    balls = create_balls(canvas)
    while True:
        # update world
        for ball in balls:
            ball.update(canvas)
        # redraw canvas
        canvas.update()
        # pause
        time.sleep(1/50.)

def create_balls(canvas):
    balls = []
    for i in range(N_BALLS):
        ball = Ball(canvas)
        balls.append(ball)
    return balls

######## DO NOT MODIFY ANY CODE BELOW THIS LINE ###########

# This function is provided to you and should not be modified.
# It creates a window that contains a drawing canvas that you
# will use to make your drawings.
def make_canvas(width, height, title):
    """
    DO NOT MODIFY
    Creates and returns a drawing canvas
    of the given int size with a blue border,
    reachange_y for drawing.
    """
    top = tkinter.Tk()
    top.minsize(width=width, height=height)
    top.title(title)
    canvas = tkinter.Canvas(top, width=width + 1, height=height + 1)
    canvas.pack()
    return canvas

if __name__ == '__main__':
    main()