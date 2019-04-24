# 
# ps1pr3.py - Problem Set 1, Problem 3
#
# Functions with numeric inputs
#
# name: 
# email:
#
# If you worked with a partner, put his or her contact info below:
# partner's name:
# partner's email:
#

# function 0
def opposite(x):
    """ returns the opposite of its input
        input x: any number (int or float)
    """
    return -1*x

# put your definitions for the remaining functions below
def cube(x):
    return x**3
print(cube(3))

def compare(num1, num2):
    if num1 > num2:
        return 1
    elif num1 < num2:
        return -1
    else:
        return 0
print(compare(10,100))

def slope(x1, y1, x2, y2):
    if x1 == x2:
        return float('nan')
    else:
        return (y2 - y1)/(x2 - x1)
print(slope(2, 3, 5, 3))

def make_change(cents):
    quarters = cents//25       # number of quarters
    dimes = cents%25//10       # number of dimes
    nickels = cents%25%10//5   # number of nickels
    pennies = cents%5          # number of pennies
    return [quarters, dimes, nickels, pennies]
print(make_change(100))

# test function with a sample test call for function 0
def test():
    """ performs test calls on the functions above """
    print('opposite(-8) returns', opposite(-8))

    # optional but encouraged: add test calls for your functions below
