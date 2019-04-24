#
# ps7pr4.py (Problem Set 7, Problem 4)
#
# Image processing with loops and image objects    
#
# Computer Science 111
# 

from cs111png import *

def invert(filename):
    """ loads a PNG image from the file with the specified filename
        and creates a new image in which the colors of the pixels are
        inverted.
        input: filename is a string specifying the name of the PNG file
               that the function should process.
        No value is returned, but the new image is stored in a file
        whose name is invert_filename, where filename is the name of
        the original file.
    """
    # create an image object for the image stored in the
    # file with the specified filename
    img = load_image(filename)

    # determine the dimensions of the image
    height = img.get_height()
    width = img.get_width()

    # process the image, one pixel at a time
    for r in range(height):
        for c in range(width):
            # get the RGB values of the pixel at row r, column c
            rgb = img.get_pixel(r, c)            
            red = rgb[0]
            green = rgb[1]
            blue = rgb[2]

            # invert the colors of the pixel at row r, column c
            new_rgb = [255 - red, 255 - green, 255 - blue]
            img.set_pixel(r, c, new_rgb)

    # save the modified image, using a filename that is based on the
    # name of the original file.
    new_filename = 'invert_' + filename
    img.save(new_filename)

def brightness(rgb):
    """ takes the RGB values of a pixel (an [R, G, B] list) and returns a value
        between 0 and 255 that represents the brightness of that pixel.
    """
    red = rgb[0]
    green = rgb[1]
    blue = rgb[2]
    return (21*red + 72*green + 7*blue) // 100

### PUT YOUR WORK FOR PROBLEM 4 BELOW. ###
# 1
def grayscale(filename):
    # load img
    img = load_image(filename)
    height = img.get_height()
    width = img.get_width()
    # process the image
    for r in range(height):
        for c in range(width):
            new_rgb = [brightness(img._get_pixel(r, c))]*3
            img.set_pixel( r, c, new_rgb)
    # save the new image
    new_filename = 'gray_' + filename
    img.save(new_filename)

# 2
def mirror_horiz(filename):
    # load img
    img = load_image(filename)
    height = img.get_height()
    width = img.get_width()
    # index of column
    i = 1
    # process the image
    for r in range(height):
        for c in range(width):
            if c > width//2:
                new_rgb = img._get_pixel(r, c - (2*i + 1))
                img.set_pixel( r, c, new_rgb)
                i += 1
        i = 1
    # save the new image
    new_filename = 'mirrorh_' + filename
    img.save(new_filename)

# 3
def reduce(filename):
    # load img
    img = load_image(filename)
    height = img.get_height()
    width = img.get_width()
    # create new img
    new_img = Image(height//2, width//2)
    # process the new_img
    for r in range(height):
        if r%2 == 0:
            for c in range(width):
                if c%2 == 0:
                    new_img.set_pixel( r//2, c//2, img._get_pixel(r, c))
    # save the new image
    new_filename = 'reduce_' + filename
    new_img.save(new_filename)

