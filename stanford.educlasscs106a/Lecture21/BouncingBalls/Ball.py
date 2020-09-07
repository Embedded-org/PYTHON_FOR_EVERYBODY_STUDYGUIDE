import random
from constants import *

class Ball:
    '''
    This is the blueprint for a new variable type called "Ball"
    Every ball has three things: an oval, a change_x and a change_y.
    Every ball supports the "update" method which will move the ball one step.
    '''

    # note the use of 'canvas' as a parameter!
    def __init__(self, canvas):
        x_1 = random.randint(0, CANVAS_WIDTH - BALL_SIZE)
        y_1 = random.randint(0, CANVAS_HEIGHT - BALL_SIZE)
        x_2 = x_1 + BALL_SIZE
        y_2 = y_1 + BALL_SIZE
        self.oval = canvas.create_oval(x_1, y_1, x_2, y_2, fill='blue', outline='blue')
        self.change_x = random.randint(5, 15)
        self.change_y = random.randint(5, 15)

    # again, I pass in canvas. Good times.
    def update(self, canvas):
        # update a single ball instance (the one given by self)
        canvas.move(self.oval, self.change_x, self.change_y)
        if self._hit_left_or_right_wall(canvas):
            self.change_x *= -1

        if self._hit_top_or_bottom_wall(canvas):
            self.change_y *= -1

    def _hit_left_or_right_wall(self, canvas):
        # this is a tkinter function which gets the coordinates of a shape
        # the first element in the returned list is the x value of the left
        # of the shape
        ball_x = canvas.coords(self.oval)[0]
        return ball_x < 0 or ball_x > CANVAS_WIDTH - BALL_SIZE

    def _hit_top_or_bottom_wall(self, canvas):
        # the second element in the returned list is the y value of the top
        ball_y = canvas.coords(self.oval)[1]
        return ball_y < 0 or ball_y > CANVAS_HEIGHT - BALL_SIZE