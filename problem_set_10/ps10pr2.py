#
# ps10pr2.py  (Problem Set 10, Problem 2)
#
# A Connect-Four Player class   
#

from ps10pr1 import Board

# write your class below
class Player:
    def __init__(self, checker):
        self.checker = checker
        self.num_moves = 0

    # 2
    def __repr__(self):
        return 'Player ' + self.checker

    # 3
    def opponent_checker(self):
        if self.checker == 'X':
            return 'O'
        else:
            return 'X'

    # 4
    def next_move(self, board):
        col = int(input('Which columns do you want to place the checker in: '))
        if board.can_add_to(col):
            self.num_moves += 1
            return col
        else:
            print('Try again!')
            self.next_move(board)