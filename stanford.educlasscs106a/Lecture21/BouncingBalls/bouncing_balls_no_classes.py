import tkinter
import time
import random
from constants import *

N_BALLS = 10

def main():
    canvas = make_canvas(CANVAS_WIDTH, CANVAS_HEIGHT, 'Bouncing Ball')
    balls = create_balls(canvas)
    while True:
        # update world
        for ball in balls:
            # move the current ball
            canvas.move(ball['oval'], ball['change_x'], ball['change_y'])

            # check for collisions for the current ball
            if hit_left_or_right_wall(canvas, ball['oval']):
                ball['change_x'] *= -1
            if hit_top_or_bottom_wall(canvas, ball['oval']):
                ball['change_y'] *= -1
        # redraw canvas
        canvas.update()
        # pause
        time.sleep(1/50.)

def create_balls(canvas):
    balls = []
    for i in range(N_BALLS):
        ball = {}
        ball['change_x'] = random.randint(5, 15)
        ball['change_y'] = random.randint(5, 15)
        ball['oval'] = create_ball_oval(canvas)
        balls.append(ball)
    return balls

def create_ball_oval(canvas):
    # make a single ball. Give it random position
    x_1 = random.randint(0, CANVAS_WIDTH - BALL_SIZE)
    y_1 = random.randint(0, CANVAS_HEIGHT - BALL_SIZE)
    x_2 = x_1 + BALL_SIZE
    y_2 = y_1 + BALL_SIZE
    oval = canvas.create_oval(x_1, y_1, x_2, y_2, fill='blue', outline='blue')
    return oval

def hit_left_or_right_wall(canvas, object):
    ball_x = canvas.coords(object)[0]
    return ball_x <= 0 or ball_x > CANVAS_WIDTH - BALL_SIZE

def hit_top_or_bottom_wall(canvas, object):
    ball_y = canvas.coords(object)[1]
    return ball_y <= 0 or ball_y > CANVAS_HEIGHT - BALL_SIZE



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