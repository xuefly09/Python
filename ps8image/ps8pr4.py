#
# ps8pr4.py  (Problem Set 8, Problem 4)
#
# Images as 2-D lists  
#
# Computer Science 111
# 

from hmcpng import *

def create_uniform_image(height, width, pixel):
    """ creates and returns a 2-D list of pixels with height rows and
        width columns in which all of the pixels have the RGB values
        given by pixel
        inputs: height and width are non-negative integers
                pixel is a 1-D list of RBG values of the form [R,G,B],
                     where each element is an integer between 0 and 255.
    """
    pixels = []
    
    for r in range(height):
        row = [pixel] * width
        pixels += [row]

    return pixels

# 1
def blank_image(height, width):
    pixels = create_uniform_image(height, width, [0, 255, 0])
    return pixels

# 2
def flip_horiz(pixels):
    width = len(pixels[0])
    height = len(pixels)
    new_pixels = create_uniform_image(height, width, [0, 0 ,0])
    for r in range(height):
        for c in range(width):
            new_pixels[r][width - c - 1] = pixels[r][c]
    return new_pixels

# 3
def extract(pixels, rmin, rmax, cmin, cmax):
    width = len(pixels[0])
    height = len(pixels)
    new_pixels = create_uniform_image(rmax - rmin,cmax - cmin, [0, 0 ,0])
    current_r = 0
    current_c = 0
    for r in range(height):
        if rmax + 1 > r > rmin:
            for c in range(width):
                if cmax + 1 > c > cmin:
                    new_pixels[current_r][current_c] = pixels[r][c]
                    current_c += 1
            current_r += 1
            current_c = 0
    return new_pixels

# 4
def transpose(pixels):
    width = len(pixels[0])
    row = []
    new_pixels = []
    for index in range(width):
        for val in pixels:
            row += [val[index]]
        new_pixels += [row]
        row = []
    return new_pixels

# 5
def rotate_clockwise(pixels):
    new_pixels = flip_horiz(pixels)
    new_pixels = rotate_counterclockwise(new_pixels)
    return flip_horiz(new_pixels)

def rotate_counterclockwise(pixels):
    new_pixels = flip_horiz(pixels)
    return transpose(new_pixels)
