#
# ps10pr4.py  (Problem Set 10, Problem 4)
#
# AI Player for use in Connect Four   
#

import random  
from ps10pr3 import *

class AIPlayer(Player):
    # 2
    def __init__(self, checker, tiebreak, lookahead):
        """ put your docstring here
        """
        assert(checker == 'X' or checker == 'O')
        assert(tiebreak == 'LEFT' or tiebreak == 'RIGHT' or tiebreak == 'RANDOM')
        assert(lookahead >= 0)
        super().__init__(checker)
        self.tiebreak = tiebreak
        self.lookahead  = lookahead

    # 3
    def __repr__(self):
        return super().__repr__() + ' (' + self.tiebreak + ', ' + str(self.lookahead) + ')'

    # 4
    def max_score_column(self, scores):
        print(scores)
        res_list = []
        max_score = max(scores)
        for index in range(len(scores)):
            if scores[index] == max_score:
                res_list += [index]
        if len(res_list) > 1:
            if self.tiebreak == 'LEFT':
                return res_list[0]
            elif self.tiebreak == 'RIGHT':
                return res_list[-1]
            else:
                return random.choice(res_list)
        else:
            return res_list[0]

    # 5
    def scores_for(self, board):
        scores = [50] * board.width
        for col in range(board.width):
            if board.can_add_to(col) == False:
                scores[col] = -1
            elif board.is_win_for(self.checker):
                scores[col] = 100
            elif board.is_win_for(self.opponent_checker()):
                scores[col] = 0
            elif self.lookahead == 0:
                scores[col] = 50
            else:
                board.add_checker(self.checker, col)
                opp = AIPlayer(self.opponent_checker(), self.tiebreak, self.lookahead - 1)
                scores_list = opp.scores_for(board)
                if 100 in scores_list:
                    scores[col] = 0
                elif 100 not in scores_list and 50 not in scores_list:
                    scores[col] = 100
                else:
                    if scores_list[col] == 0 or scores_list[col] == -1:
                        scores[col] = 50
                    else:
                        scores[col] = scores_list[col]
                board.remove_checker(col)
        return scores

    # 6
    def next_move(self, board):
        self.num_moves += 1
        return self.max_score_column(self.scores_for(board))



                

