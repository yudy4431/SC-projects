"""
SC101 Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by
Jerry Liao.

YOUR DESCRIPTION HERE
"""

import tkinter
import babynames
import babygraphicsgui as gui

FILENAMES = [
    'data/full/baby-1900.txt', 'data/full/baby-1910.txt',
    'data/full/baby-1920.txt', 'data/full/baby-1930.txt',
    'data/full/baby-1940.txt', 'data/full/baby-1950.txt',
    'data/full/baby-1960.txt', 'data/full/baby-1970.txt',
    'data/full/baby-1980.txt', 'data/full/baby-1990.txt',
    'data/full/baby-2000.txt', 'data/full/baby-2010.txt'
]
CANVAS_WIDTH = 1000
CANVAS_HEIGHT = 600
YEARS = [1900, 1910, 1920, 1930, 1940, 1950, 1960, 1970, 1980, 1990, 2000, 2010]
GRAPH_MARGIN_SIZE = 20
COLORS = ['red', 'purple', 'green', 'blue']
TEXT_DX = 2
LINE_WIDTH = 2
MAX_RANK = 1000
R = 3       # Radius of the oval.


def get_x_coordinate(width, year_index):
    """
    Given the width of the canvas and the index of the current year
    in the YEARS list, returns the x coordinate of the vertical
    line associated with that year.

    Input:
        width (int): The width of the canvas
        year_index (int): The index of the current year in the YEARS list
    Returns:
        x_coordinate (int): The x coordinate of the vertical line associated
                              with the specified year.
    """
    x_coordinate = GRAPH_MARGIN_SIZE + year_index*((width-2*GRAPH_MARGIN_SIZE) / len(YEARS))

    return x_coordinate


def draw_fixed_lines(canvas):
    """
    Erases all existing information on the given canvas and then
    draws the fixed background lines on it.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.

    Returns:
        This function does not return any value.
    """
    canvas.delete('all')            # delete all existing lines from the canvas

    # Write your code below this line
    canvas.create_line(GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE, CANVAS_WIDTH-GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE)
    canvas.create_line(GRAPH_MARGIN_SIZE, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE, CANVAS_WIDTH-GRAPH_MARGIN_SIZE, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE)
    canvas.create_line(GRAPH_MARGIN_SIZE, 0, GRAPH_MARGIN_SIZE, CANVAS_HEIGHT)

    for i in range(len(YEARS)):
        x = get_x_coordinate(CANVAS_WIDTH, i)
        canvas.create_line(x, 0, x, CANVAS_HEIGHT)
        canvas.create_text(x, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE, text=YEARS[i], anchor=tkinter.NW, font='modern 15')


def what_color(color_now, n):
    """
    Decide the color of the lines, points and texts.
    :param color_now: (str) A empty string to store color.
    :param n: (int) The index of the lookup_names.
    :return: (str) The color gonna used in the lookup_names line.
    If n > 4 , the color will change by COLORS according to remainder.
    """
    if n % 4 == 0:
        color_now = COLORS[3]
    elif n % 4 == 1:
        color_now = COLORS[0]
    elif n % 4 == 2:
        color_now = COLORS[1]
    elif n % 4 == 3:
        color_now = COLORS[2]
    return color_now


def create_all(canvas, x1, y1, x2, y2, color, name):
    """
    Create a line and all points and texts of years.
    :param canvas: (obj)(Tkinter Canvas): The canvas on which we are drawing.
    :param x1: (int) First x-coordinate.
    :param y1: (int) First y-coordinate.
    :param x2: (int) Second x-coordinate.
    :param y2: (int) Second y-coordinate.
    :param color: (str) Color of the line, point and text.
    :param name: Name which is processed.
    :return: Line, points, texts on graphic.
    """
    canvas.create_line(x1, y1, x2, y2, fill=color, width=LINE_WIDTH)
    canvas.create_text(x1+TEXT_DX, y1, text=name, anchor=tkinter.SW, font='modern 12', fill=color)
    canvas.create_oval(x1-R, y1-R, x1+R, y1+R, fill=color)


def draw_names(canvas, name_data, lookup_names):
    """
    Given a dict of baby name data and a list of name, plots
    the historical trend of those names onto the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
        name_data (dict): Dictionary holding baby name data
        lookup_names (List[str]): A list of names whose data you want to plot

    Returns:
        This function does not return any value.
    """
    draw_fixed_lines(canvas)        # draw the fixed background grid

    # Write your code below this line

    # To control y-coordinate place.
    ratio = (CANVAS_HEIGHT-2*GRAPH_MARGIN_SIZE) / MAX_RANK

    # The times of names input, the times names be processed.
    for i in range(len(lookup_names)):
        # Get the data of name.
        value = name_data[lookup_names[i]]
        # To control the input data of x-coordinate.
        year_index = 0
        for j in range(len(YEARS)-1):
            # Get the x-coordinate of the start and the end point.
            x1 = get_x_coordinate(CANVAS_WIDTH, year_index)
            x2 = get_x_coordinate(CANVAS_WIDTH, year_index + 1)

            ###################################################################################
            # To check whether the key-value is in dictionary and get the value of rank.
            if str(YEARS[j]) not in value and str(YEARS[j+1]) not in value:
                rank = str(MAX_RANK)
                rank2 = str(MAX_RANK)
            elif str(YEARS[j]) in value and str(YEARS[j+1]) not in value:
                rank = name_data[lookup_names[i]][str(YEARS[j])]
                rank2 = str(MAX_RANK)
            elif str(YEARS[j]) not in value and str(YEARS[j+1]) in value:
                rank = str(MAX_RANK)
                rank2 = name_data[lookup_names[i]][str(YEARS[j + 1])]
            else:
                rank = name_data[lookup_names[i]][str(YEARS[j])]
                rank2 = name_data[lookup_names[i]][str(YEARS[j+1])]

            ###################################################################################
            # Choose the color of line and text.
            color = ''
            color += what_color(color, i)

            ###################################################################################
            # To check if rank and rank is out of ranking and then create line, text and oval.
            if int(rank) == MAX_RANK and int(rank2 != MAX_RANK):
                create_all(canvas, x1, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE, x2,GRAPH_MARGIN_SIZE + int(rank2) * ratio, color
                           , lookup_names[i]+' *')

            elif int(rank2) == MAX_RANK and int(rank) != MAX_RANK:
                create_all(canvas, x1, GRAPH_MARGIN_SIZE + int(rank) * ratio, x2, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE, color
                           , lookup_names[i]+' '+rank)

            elif int(rank) == MAX_RANK and int(rank2) == MAX_RANK:
                create_all(canvas, x1, CANVAS_HEIGHT - GRAPH_MARGIN_SIZE, x2, CANVAS_HEIGHT - GRAPH_MARGIN_SIZE,
                           color, lookup_names[i]+' *')
            else:
                create_all(canvas, x1, GRAPH_MARGIN_SIZE+int(rank)*ratio, x2, GRAPH_MARGIN_SIZE+int(rank2)*ratio,
                           color, lookup_names[i]+' '+rank)

            ###################################################################################
            # Because we create line with 2 points and text with first point, there must a last point of the data
            # that hasn't create text. This if-else gonna create the last text and oval of the data.
            if j == len(YEARS)-2:
                if rank2 == str(MAX_RANK):
                    canvas.create_text(x2, GRAPH_MARGIN_SIZE+int(rank2)*ratio,
                                       text=lookup_names[i] + ' ' + '*', anchor=tkinter.SW, font='modern 12', fill=color)

                    canvas.create_oval(x2-R, GRAPH_MARGIN_SIZE+int(rank2)*ratio-R, x2+R,
                                       GRAPH_MARGIN_SIZE+int(rank2)*ratio+R, fill=color)
                else:
                    canvas.create_text(x2, GRAPH_MARGIN_SIZE + int(rank2) * ratio, text=lookup_names[i] + ' ' + rank2,
                                       anchor=tkinter.SW, font='modern 12',
                                       fill=color)
                    canvas.create_oval(x2-R, GRAPH_MARGIN_SIZE + int(rank2) * ratio-R, x2+R,
                                       GRAPH_MARGIN_SIZE + int(rank2) * ratio+R, fill=color)
            year_index += 1



# main() code is provided, feel free to read through it but DO NOT MODIFY
def main():
    # Load data
    name_data = babynames.read_files(FILENAMES)

    # Create the window and the canvas
    top = tkinter.Tk()
    top.wm_title('Baby Names')
    canvas = gui.make_gui(top, CANVAS_WIDTH, CANVAS_HEIGHT, name_data, draw_names, babynames.search_names)

    # Call draw_fixed_lines() once at startup so we have the lines
    # even before the user types anything.
    draw_fixed_lines(canvas)

    # This line starts the graphical loop that is responsible for
    # processing user interactions and plotting data
    top.mainloop()


if __name__ == '__main__':
    main()
