"""
File: stanCodoshop.py
----------------------------------------------
SC101_Assignment3
Adapted from Nick Parlante's
Ghost assignment by Jerry Liao.

-----------------------------------------------

TODO:
"""
import math
import os
import sys
from simpleimage import SimpleImage


def get_pixel_dist(pixel, red, green, blue):
    """
    Returns the color distance between pixel and mean RGB value

    Input:
        pixel (Pixel): pixel with RGB values to be compared
        red (int): average red value across all images
        green (int): average green value across all images
        blue (int): average blue value across all images

    Returns:
        dist (int): color distance between red, green, and blue pixel values

    """
    red_avg = red
    green_avg = green
    blue_avg = blue
    color_distance = math.sqrt((red_avg-pixel.red)**2 + (green_avg-pixel.green)**2 + (blue_avg-pixel.blue)**2)
    return color_distance


def get_average(pixels):
    """
    Given a list of pixels, finds the average red, blue, and green values

    Input:
        pixels (List[Pixel]): list of pixels to be averaged
    Returns:
        rgb (List[int]): list of average red, green, blue values across pixels respectively

    Assumes you are returning in the order: [red, green, blue]

    """
    red_pixel = 0                                 # To count the total red pixel of picture.
    green_pixel = 0                               # To count the total green pixel of picture.
    blue_pixel = 0                                # To count the total blue pixel of picture.
    for i in range(len(pixels)):
        red_pixel += pixels[i].red
        green_pixel += pixels[i].green
        blue_pixel += pixels[i].blue
    rgb = [red_pixel // len(pixels), green_pixel // len(pixels), blue_pixel // len(pixels)]
    return rgb


def get_best_pixel(pixels):
    """
    Given a list of pixels, returns the pixel with the smallest
    distance from the average red, green, and blue values across all pixels.

    Input:
        pixels (List[Pixel]): list of pixels to be averaged and compared
    Returns:
        best (Pixel): pixel closest to RGB averages

    """
    avg = get_average(pixels)
    best_value = 442                                                    # Square root of 255^2*3 = 441.6.
    best_pixel_list = []                                                # To store the newest lower pixel dist.
    for i in range(len(pixels)):
        compare = get_pixel_dist(pixels[i], avg[0], avg[1], avg[2])     # Compares each pixel to avg RGB.
        if compare < best_value:                                        # Add lower value is the list.
            best_value = compare
            best_pixel_list.append(pixels[i])
    best_pixel = best_pixel_list[len(best_pixel_list)-1]                # The last value of the list means the lowest
                                                                        # value of the pixel distance.

    return best_pixel


def solve(images):
    """
    Given a list of image objects, compute and display a Ghost solution image
    based on these images. There will be at least 3 images and they will all
    be the same size.

    Input:
        images (List[SimpleImage]): list of images to be processed
    """
    width = images[0].width
    height = images[0].height
    result = SimpleImage.blank(width, height)
    ######## YOUR CODE STARTS HERE #########
    for x in range(width):
        for y in range(height):
            lst = []                                        # To store pixels at (x, y) in each picture.
            for i in range(len(images)):
                lst.append(images[i].get_pixel(x, y))
            best = get_best_pixel(lst)                      # Get the best pixel.
            pixel = result.get_pixel(x, y)
            pixel.red = best.red                            # Substitute the pixels of blank picture to the best
            pixel.green = best.green                        # pixels in other pictures.
            pixel.blue = best.blue
    ######## YOUR CODE ENDS HERE ###########
    print("Displaying image!")
    result.show()


def jpgs_in_dir(dir):
    """
    (provided, DO NOT MODIFY)
    Given the name of a directory, returns a list of the .jpg filenames
    within it.

    Input:
        dir (string): name of directory
    Returns:
        filenames(List[string]): names of jpg files in directory
    """
    filenames = []
    for filename in os.listdir(dir):
        if filename.endswith('.jpg'):
            filenames.append(os.path.join(dir, filename))
    return filenames


def load_images(dir):
    """
    (provided, DO NOT MODIFY)
    Given a directory name, reads all the .jpg files within it into memory and
    returns them in a list. Prints the filenames out as it goes.

    Input:
        dir (string): name of directory
    Returns:
        images (List[SimpleImages]): list of images in directory
    """
    images = []
    jpgs = jpgs_in_dir(dir)
    for filename in jpgs:
        print("Loading", filename)
        image = SimpleImage(filename)
        images.append(image)
    return images


def main():
    # (provided, DO NOT MODIFY)
    args = sys.argv[1:]
    # We just take 1 argument, the folder containing all the images.
    # The load_images() capability is provided above.
    images = load_images(args[0])
    solve(images)


if __name__ == '__main__':
    main()
