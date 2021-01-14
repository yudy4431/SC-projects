"""
File: draw_line
Name: Yudy
-------------------------
To draw a line with clicking twice mouse.
"""

from campy.graphics.gobjects import GOval, GLine
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked

# Decide the circle size we click on the window.
SIZE = 5
window = GWindow()
# To store the number of the points on the window.
count = 0
# To store the start point of x
x0 = 0
# To store the start point of y
y0 = 0
# To store the object of start point.
temp = None


def main():
    """
    This program creates lines on an instance of GWindow class.
    There is a circle indicating the user’s first click. A line appears
    at the condition where the circle disappears as the user clicks
    on the canvas for the second time.
    """
    onmouseclicked(draw_a_line)


def draw_a_line(mouse):
    global count, x0, y0, temp
    point = GOval(SIZE, SIZE, x=mouse.x, y=mouse.y)
    count += 1
    # odd points means there is a start point
    # even points means there is a start point and a end point to make a line.
    if count % 2 == 1:
        window.add(point)
        x0 = mouse.x
        y0 = mouse.y
        temp = point
    elif count % 2 == 0:
        line = GLine(x0, y0, mouse.x, mouse.y)
        window.add(line)
        window.remove(temp)





if __name__ == "__main__":
    main()
