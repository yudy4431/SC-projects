"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao

YOUR DESCRIPTION HERE
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing.
BRICK_WIDTH = 40       # Height of a brick (in pixels).
BRICK_HEIGHT = 15      # Height of a brick (in pixels).
BRICK_ROWS = 10        # Number of rows of bricks.
BRICK_COLS = 10        # Number of columns of bricks.
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels).
BALL_RADIUS = 10       # Radius of the ball (in pixels).
PADDLE_WIDTH = 75      # Width of the paddle (in pixels).
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels).
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels).

INITIAL_Y_SPEED = 7.0  # Initial vertical speed for the ball.
MAX_X_SPEED = 5      # Maximum initial horizontal speed for the ball.


class BreakoutGraphics:

    def __init__(self, ball_radius = BALL_RADIUS, paddle_width = PADDLE_WIDTH,
                 paddle_height = PADDLE_HEIGHT, paddle_offset = PADDLE_OFFSET,
                 brick_rows = BRICK_ROWS, brick_cols = BRICK_COLS,
                 brick_width = BRICK_WIDTH, brick_height = BRICK_HEIGHT,
                 brick_offset = BRICK_OFFSET, brick_spacing = BRICK_SPACING,
                 title='Breakout'):

        # Create a graphical window, with some extra space.
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)

        # Create a paddle.
        self.paddle = GRect(paddle_width, paddle_height, x=(self.window.width - paddle_width) / 2,
                            y=self.window.height - paddle_offset)
        self.paddle.filled = True
        self.paddle.fill_color = 'medium blue'
        self.window.add(self.paddle)

        # Center a filled ball in the graphical window.
        self.ball = GOval(2*ball_radius, 2*ball_radius, x=window_width/2-2*ball_radius, y=window_height/2-2*ball_radius)
        self.ball.filled = True
        self.ball.fill_color = 'medium blue'
        self.window.add(self.ball)

        # Default initial velocity for the ball.
        # for x
        self.__dx = random.randint(0, MAX_X_SPEED)
        if random.random() > 0.5:
            self.__dx = -self.__dx
        # for y
        self.__dy = INITIAL_Y_SPEED

        # Initialize our mouse listeners.
        self.is_started = False
        onmouseclicked(self.switch)
        onmousemoved(self.mouse_move_paddle)

        # Draw bricks.
        count_rows = 0
        count_rows_color = 1
        for i in range(brick_cols):
            for j in range(brick_rows):
                self.brick = GRect(brick_width, brick_height, x=count_rows+j*brick_spacing,
                                   y=BRICK_OFFSET+i*(brick_height+brick_spacing))
                self.brick.filled = True
                if count_rows_color == 1 or count_rows_color == 2:
                    self.brick.fill_color = 'royal blue'
                elif count_rows_color == 3 or count_rows_color == 4:
                    self.brick.fill_color = 'dodger blue'
                elif count_rows_color == 5 or count_rows_color == 6:
                    self.brick.fill_color = 'deep sky blue'
                elif count_rows_color == 7 or count_rows_color == 8:
                    self.brick.fill_color = 'aqua'
                elif count_rows_color == 9 or count_rows_color == 10:
                    self.brick.fill_color = 'pale turquoise'
                self.window.add(self.brick)
                count_rows += brick_width
            count_rows = 0
            count_rows_color += 1
        # to check if there are any bricks left on window.
        # when bricks count > bricks amount , it means all the bricks are deleted.
        self.bricks_amount = brick_rows * brick_cols
        self.bricks_count = 1

    # paddle movement
    def mouse_move_paddle(self, event):
        self.paddle.x = event.x - self.paddle.width/2
        if self.paddle.x <= 0:
            self.paddle.x = 0
        if self.paddle.x >= self.window.width-self.paddle.width:
            self.paddle.x = self.window.width-self.paddle.width

    # ball movement

    def get_ball_dx(self):
        return self.__dx

    def get_ball_dy(self):
        return self.__dy

    def set_ball_dx(self, new_dx):
        self.__dx = new_dx

    def set_ball_dy(self, new_dy):
        self.__dy = new_dy

    def reset_ball(self):
        self.ball.x = self.window.width / 2 - self.ball.width
        self.ball.y = self.window.height / 2 - self.ball.height
        self.__dx = random.randint(0, MAX_X_SPEED)
        if random.random() > 0.5:
            self.__dx = -self.__dx
        # for y
        self.__dy = INITIAL_Y_SPEED

    # switch
    def switch(self, mouse):
        self.is_started = True

    # check for touching bricks
    def obstacles(self):
        maybe_brick_1 = self.window.get_object_at(self.ball.x, self.ball.y)
        maybe_brick_2 = self.window.get_object_at(self.ball.x+self.ball.width, self.ball.y)
        maybe_brick_3 = self.window.get_object_at(self.ball.x, self.ball.y+self.ball.height)
        maybe_brick_4 = self.window.get_object_at(self.ball.x+self.ball.width, self.ball.y+self.ball.height)
        if maybe_brick_1 is not None:
            if maybe_brick_1 is not self.paddle:
                self.window.remove(maybe_brick_1)
                self.__dy = -1 * self.__dy
                self.bricks_count += 1
            else:
                # make sure the ball will not het into paddle.
                self.ball.y = self.paddle.y-self.ball.height
                self.__dy = -1 * self.__dy
        elif maybe_brick_2 is not None:
            if maybe_brick_2 is not self.paddle:
                self.window.remove(maybe_brick_2)
                self.__dy = -1 * self.__dy
                self.bricks_count += 1
            else:
                # make sure the ball will not het into paddle.
                self.ball.y = self.paddle.y - self.ball.height
                self.__dy = -1 * self.__dy
        elif maybe_brick_3 is not None:
            if maybe_brick_3 is not self.paddle:
                self.window.remove(maybe_brick_3)
                self.__dy = -1 * self.__dy
                self.bricks_count += 1
            else:
                # make sure the ball will not het into paddle.
                self.ball.y = self.paddle.y - self.ball.height
                self.__dy = -1 * self.__dy
        elif maybe_brick_4 is not None:
            if maybe_brick_4 is not self.paddle:
                self.window.remove(maybe_brick_4)
                self.__dy = -1 * self.__dy
                self.bricks_count += 1
            else:
                # make sure the ball will not het into paddle.
                self.ball.y = self.paddle.y - self.ball.height
                self.__dy = -1 * self.__dy














