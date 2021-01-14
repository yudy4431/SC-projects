"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao

YOUR DESCRIPTION HERE
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 1000 / 120 # 120 frames per second.
NUM_LIVES = 3


def main():
    graphics = BreakoutGraphics()
    lives = NUM_LIVES
    # Add animation loop here
    while True:
        if lives > 0 and graphics.bricks_count <= graphics.bricks_amount:
            if graphics.is_started:
                graphics.ball.move(graphics.get_ball_dx(), graphics.get_ball_dy())
                graphics.obstacles()
                # check for wall x collision
                if graphics.ball.x <= 0:
                    new_dx = -1 * graphics.get_ball_dx()
                    graphics.set_ball_dx(new_dx)
                elif graphics.ball.x >= graphics.window.width-graphics.ball.width:
                    new_dx = -1 * graphics.get_ball_dx()
                    graphics.set_ball_dx(new_dx)
                # check for wall y collision
                if graphics.ball.y <= 0:
                    new_dy = -1 * graphics.get_ball_dy()
                    graphics.set_ball_dy(new_dy)
                elif graphics.ball.y >= graphics.window.height:
                    graphics.is_started = False
                    lives -= 1
                    graphics.reset_ball()
        else:
            graphics.reset_ball()
            break
        pause(FRAME_RATE)






if __name__ == '__main__':
    main()
