#
# ps10pr3.py  (Problem Set 10, Problem 3)
#
# Playing the game    
#

from ps10pr1 import Board
from ps10pr2 import Player
import random
    
def connect_four(player1, player2):
    """ Plays a game of Connect Four between the two specified players,
        and returns the Board object as it looks at the end of the game.
        inputs: player1 and player2 are objects representing Connect Four
                  players (objects of the Player class or a subclass of Player).
                  One player should use 'X' checkers and the other should
                  use 'O' checkers.
    """
    # Make sure one player is 'X' and one player is 'O'.
    if player1.checker not in 'XO' or player2.checker not in 'XO' \
       or player1.checker == player2.checker:
        print('need one X player and one O player.')
        return None

    print('Welcome to Connect Four!')
    print()
    board = Board(6, 7)
    print(board)
    
    while True:
        if process_move(player1, board) == True:
            return board

        if process_move(player2, board) == True:
            return board

# 1
def process_move(player, board):
    print('%s\'s turn'% player)
    col_move = player.next_move(board)
    board.add_checker(player.checker, col_move)
    print('\n')
    print(board)
    if board.is_win_for(player.checker):
        print('%s wins in %d moves.\nCongratulations!' % (player,player.num_moves))
        return True
    elif board.is_full():
        print('It\'s a tie!')
        return True
    else:
        return False

class RandomPlayer(Player):
    def next_move(self, board):
        res_list = []
        for index in range(board.width):
            if board.can_add_to(index):
                res_list += [index]
        return random.choice(res_list)

