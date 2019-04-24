#
# ps8pr2.py  (Problem Set 8, Problem 2)
#
# Conway's Game of Life
#
# Computer Science 111  
#

# IMPORTANT: this file is for your solutions to Problem 2.
# Your solutions to Problem 1 should go in ps8pr1.py instead.

from ps8pr1 import *
from gol_graphics import *

# 1
def inner_reverse(grid):
    new_grid = copy(grid)
    height = len(new_grid)
    width = len(new_grid[0])
    for r in range(height):
        if r != 0 and r != height - 1:
            for c in range(width):
                if c != 0 and c != width - 1:
                    if new_grid[r][c] == 0:
                        new_grid[r][c] = 1
                    else:
                        new_grid[r][c] = 0
    return new_grid

# 2
def count_neighbors(cellr, cellc, grid):
    height = len(grid)
    width = len(grid[0])
    sum_alive = 0
    for r in range(height):
        if r == cellr - 1 or r ==  cellr or r == cellr + 1:
            sum_alive += grid[r][cellc] + grid[r][cellc - 1] + grid[r][cellc + 1]
    return sum_alive - grid[cellr][cellc]

# 3
def next_gen(grid):
    new_grid = copy(grid)
    height = len(new_grid)
    width = len(new_grid[0])
    for r in range(height):
        if r != 0 and r != height - 1:
            for c in range(width):
                if c != 0 and c != width - 1:
                    num_alive = count_neighbors(r, c, grid)
                    current_status = grid[r][c]
                    if num_alive < 2 and current_status == 1:
                        new_grid[r][c] = 0
                    elif num_alive > 3 and current_status == 1:
                        new_grid[r][c] = 0
                    elif num_alive == 3 and current_status == 0:
                        new_grid[r][c] = 1
    return new_grid