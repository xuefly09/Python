#
# ps8pr3.py  (Problem Set 8, Problem 3)
#
# Matrix Operations  
#
# Computer Science 111   
# 

def display_menu():
    """ prints a menu of options
    """  
    print()
    print('(0) Enter a new matrix')
    print('(1) Negate the matrix')
    print('(2) Multiply a row by a constant')
    print('(3) Add one row to another')
    print('(4) Add a multiple of one row to another')
    print('(5) Transpose the matrix')
    print('(6) Quit')
    print()

def print_matrix(matrix):
    """ prints the specified matrix in rectangular form.
        input: matrix is a rectangular 2-D list numbers
    """
    for r in range(len(matrix)):
        for c in range(len(matrix[0])):
            print('%6.2f' % matrix[r][c], end=' ')
        print()
       
def get_matrix():
    """ gets a new matrix from the user and returns it
    """
    matrix = eval(input('Enter a new 2-D list of numbers: '))
    return matrix

def negate_matrix(matrix):
    """ negates all of the elements in the specified matrix
        inputs: matrix is a rectangular 2-D list of numbers
    """
    for r in range(len(matrix)):
        for c in range(len(matrix[0])):
            matrix[r][c] *= -1
    # We don't need to return the matrix!
    # All changes to the matrix will still be there when the
    # function returns, because we received a copy of the
    # *reference* to the matrix used by main().

### Add your functions for options 2-5 here. ###
# 2
def mult_row(matrix, r, m):
    for row in range(len(matrix)):
        if row == r:
            for c in range(len(matrix[0])):
                matrix[row][c] *= m

# 3
def add_row_into(matrix, source, dest):
    for c in range(len(matrix[0])):
        matrix[dest][c] += matrix[source][c]

# 4
def add_mult_row_into(matrix, m, source, dest):
    for c in range(len(matrix[0])):
        matrix[dest][c] += m*matrix[source][c]

# 5
def transpose(matrix):
    row = []
    res = []
    for index in range(len(matrix[0])):
        for val in matrix:
            row += [val[index]]
        res += [row]
        row = []
    return res

def main():
    """ the main user-interaction loop
    """
    ## The default starting matrix.
    ## DO NOT CHANGE THESE LINES.
    matrix = [[1, 2, 3], [4, 5, 6]]

    while True:
        print()
        print_matrix(matrix)
        display_menu()
        choice = int(input('Enter your choice: '))

        if choice == 0:
            matrix = get_matrix()
        elif choice == 1:
            negate_matrix(matrix)

        ## add code to handle the other options here
        elif choice == 2:
            row = int(input('Enter your row: '))
            factor = float(input('Enter your multiplier: '))
            mult_row(matrix, row, factor)
        elif choice == 3:
            source = int(input('Enter your source row: '))
            dest = int(input('Enter your dest row: '))
            add_row_into(matrix, source, dest)
        elif choice == 4:
            factor = float(input('Enter your multiplier: '))
            source = int(input('Enter your source row: '))
            dest = int(input('Enter your dest row: '))
            add_mult_row_into(matrix, factor, source, dest)
        elif choice == 5:
            matrix = transpose(matrix)
        elif choice == 6:
            break
        else:
            print('Invalid choice. Try again.')

class Point:
    def __init__(self, xcoord, ycoord):
        self.x = xcoord
        self.y = ycoord
    def print_point(self):
        print(self.x, self.y)

p1 = Point(10, 20)
p2 = Point(10, 20)
print(p1 == p2)

main()