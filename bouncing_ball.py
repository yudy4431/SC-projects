"""
File:bouncing ball
Name:Yudy
-------------------------
To let the ball bouncing inside the window for 3 times.
"""

from campy.graphics.gobjects import GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause
from campy.gui.events.mouse import onmouseclicked

VX = 5
DELAY = 10
GRAVITY = 1
SIZE = 20
REDUCE = 0.9
START_X = 30
START_Y = 40
# initial y-coordinate speed 
v0 = 0
# to store the objects from function "make_a_ball()"
ball = None
# the max times of the animation.
count = 3
# to open/close the move while loop.
switch = 0

window = GWindow(800, 500, title='bouncing_ball.py')


def main():
    """
    This program simulates a bouncing ball at (START_X, START_Y)
    that has VX as x velocity and 0 as y velocity. Each bounce reduces
    y velocity to REDUCE of itself.
    """
    make_a_ball()
    onmouseclicked(move)


def make_a_ball():
    global ball
    new_ball = GOval(SIZE, SIZE, x=START_X, y=START_Y)
    new_ball.filled = True
    new_ball.fill_color = 'black'
    window.add(new_ball)
    ball = new_ball


def move(mouse):
    global v0, ball, count, switch
    # run only when switch is open.
    if switch == 0:
        # lives of ball
        if count > 0:
            # close switch
            switch = 1
            while True:
                v0 += GRAVITY
                ball.move(VX, v0)
                # check for bounce.
                if ball.y + ball.height >= window.height:
                    v0 = -v0*REDUCE
                    ball.move(VX, v0)
                # check for collision.
                if ball.x > window.width:
                    ball.x = START_X
                    ball.y = START_Y
                    break
                pause(DELAY)
            # time +1 when animation is over.
            count -= 1
            # open the switch when animation is over.
            switch = 0










if __name__ == "__main__":
    main()
