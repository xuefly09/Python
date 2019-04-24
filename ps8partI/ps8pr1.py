#
# ps8pr1.py (Problem Set 8, Problem 1)
#
# 2D Lists
#
# Computer Science 111
#
# If you worked with a partner, put his or her contact info below:
# partner's name:
# partner's email:
# 

# IMPORTANT: This file is for your solutions to Problem 1.
# Your solutions to problem 2 should go in ps8pr2.py instead.

import random

def create_grid(height, width):
    """ creates and returns a 2-D list of 0s with the specified dimensions.
        inputs: height and width are non-negative integers
    """
    grid = []
    
    for r in range(height):
        row = [0] * width     # a row containing width 0s
        grid += [row]

    return grid

def print_grid(grid):
    """ prints the 2-D list specified by grid in 2-D form,
        with each row on its own line, and nothing between values.
        input: grid is a 2-D list. We assume that all of the cell
               values are integers between 0 and 9.
    """
    height = len(grid)
    width = len(grid[0])
    
    for r in range(height):
        for c in range(width):
            print(grid[r][c], end='')   # print nothing between values
        print()                         # at end of row, go to next line

def diagonal_grid(height, width):
    """ creates and returns a height x width grid in which the cells
        on the diagonal are set to 1, and all other cells are 0.
        inputs: height and width are non-negative integers
    """
    grid = create_grid(height, width)   # initially all 0s

    for r in range(height):
        for c in range(width):
            if r == c:
                grid[r][c] = 1

    return grid

# 1
def inner_grid(height, width, digit):
    grid = create_grid(height, width)
    for r in range(height):
        for c in range(width):
            if r == 0 or r == height - 1:
                grid[r][c] = 0
            elif c == 0 or c == width - 1:
                grid[r][c] = 0
            else:
                grid[r][c] = digit
    return grid

# 2
def random_grid(height, width):
    grid = create_grid(height, width)
    for r in range(height):
        for c in range(width):
            if r == 0 or r == height - 1:
                grid[r][c] = 0
            elif c == 0 or c == width - 1:
                grid[r][c] = 0
            else:
                grid[r][c] = random.choice([0, 1])
    return grid

# 3
def copy(grid):
    new_list = []
    for val in grid:
        new_list += [val[:]]
    return new_list

# 4
def increment(grid):
    height = len(grid)
    width = len(grid[0])
    for r in range(height):
        for c in range(width):
            if grid[r][c] == 9:
                grid[r][c] = 0
            else:
                grid[r][c] += 1
    return grid

