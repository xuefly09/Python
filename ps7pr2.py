#
# ps7pr2.py (Problem Set 7, Problem 2)
#
# Estimating the value of pi
#
# Computer Science 111
#

import random
import math

def throw_dart():
    """ Simulates the throwing of a random dart at a 2 x 2 square that.
        is centered on the origin. Returns True if the dart hits a circle
        inscribed in the square, and False if the dart misses the circle.
    """
    x = random.uniform(-1.0, 1.0)
    y = random.uniform(-1.0, 1.0)

    if x**2 + y**2 <= 1.0:
        return True
    else:
        return False

### PUT YOUR WORK FOR PROBLEM 2 BELOW. ###

def est_pi1(error):
    pi = 0
    dart_time = 0
    hit_time = 0
    while abs(math.pi - pi) > error:
        dart_time += 1
        hit_or_not = throw_dart()
        if throw_dart():
            hit_time += 1
        pi = hit_time*4/dart_time
        print(hit_time, "hits out of", dart_time, "throws so that pi is", pi)
    return pi

def est_pi2(n):
    hit_time = 0
    for t in range(0, n):
        hit_or_not = throw_dart()
        if throw_dart():
            hit_time += 1
        pi = hit_time*4/(t + 1)
        print(hit_time, "hits out of", t + 1, "throws so that pi is", pi)
