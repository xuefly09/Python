class Board:
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.slots = [self.width*[' '] for w in range(height)]
        self.inverse_slots = []

    # 2
    def __repr__(self):
        """ Returns a string representation for a Board object.
        """
        s = ''         # begin with an empty string

        # add one row of slots at a time
        for row in range(self.height):
            s += '|'   # one vertical bar at the start of the row

            for col in range(self.width):
                s += self.slots[row][col] + '|'

            s += '\n'  # newline at the end of the row

        # Add code here for the hyphens at the bottom of the board
        # and the numbers underneath it.
        list_numbers = [str(t) + ' ' for t in range(self.width)]
        for val in list_numbers:
            s += '--'
        s += '-\n '
        for val in list_numbers:
            s += val
        return s

    # a helper function to get the transposed slots
    def getInverse(self):
        row = []
        res = []
        for index in range(len(self.slots[0])):
            for val in self.slots:
                row += [val[index]]
            res += [row]
            row = []
        self.inverse_slots = res

    # a help function to find the empty slot of a specific column
    def number_emptiness(self, col):
        # empty slot
        position_empty = -1
        # get the inverse slots
        self.getInverse()
        # get the empty slot
        for index in range(len(self.inverse_slots[col])):
            if self.inverse_slots[col][index] == ' ':
                position_empty = index
        return position_empty

    # 3
    def add_checker(self, checker, col):
        assert(checker == 'X' or checker == 'O')
        assert(0 <= col < self.width)
        # empty slot
        position_empty = self.number_emptiness(col)
        if position_empty != -1:
            self.slots[position_empty][col] = checker

    # 5
    def add_checkers(self, colnums):
        """ takes in a string of column numbers and places alternating
            checkers in those columns of the called Board object,
            starting with 'X'.
        """
        checker = 'X'   # start by playing 'X'

        for col_str in colnums:
            col = int(col_str)
            if 0 <= col < self.width:
                self.add_checker(checker, col)

            # switch to the other checker
            if checker == 'X':
                checker = 'O'
            else:
                checker = 'X'
    # 4
    def reset(self):
        self.__init__(self.height, self.width)

    # 6
    def can_add_to(self, col):
        if 0 > col or col >= len(self.slots[0]):
            return False
        # get the inverse slots
        self.getInverse()
        # check the column
        for index in range(len(self.inverse_slots[col])):
            if self.inverse_slots[col][index] == ' ':
                return True
        return False

    # 7
    def is_full(self):
        for val in self.slots:
            for val_s in val:
                if val_s == ' ':
                    return False
        return True

    # a helper function to check emptiness
    def is_empty(self, col):
        # get the inverse slots
        self.getInverse()
        if self.inverse_slots[col][-1] == ' ':
            return True
        else:
            return False

    # 8
    def remove_checker(self, col):
        if self.is_empty(col):
            return
        else:
            # the position of empty slot
            position_empty = self.number_emptiness(col)
            if position_empty == -1:
                self.slots[0][col] = ' '
            else:
                self.slots[position_empty + 1][col] = ' '

    # 9
    def is_win_for(self, checker):
        return self.is_down_diagonal_win(checker) or self.is_up_diagonal_win(checker) or self.is_horizontal_win(checker) or self.is_vertical_win(checker)

    # helper function of vertical checking
    def is_vertical_win(self, checker):
        for val in self.slots:
            sum = 0
            for val_s in val:
                if val_s == checker:
                    sum += 1
                    if sum == 4:
                        return True
                else:
                    sum = 0
        return False

    # helper function of horizontal checking
    def is_horizontal_win(self, checker):
        # get the inverse slots
        self.getInverse()
        for val in self.inverse_slots:
            sum = 0
            for val_s in val:
                if val_s == checker:
                    sum += 1
                    if sum == 4:
                        return True
                else:
                    sum = 0
        return False

    # helper function of diagonal checking
    def is_down_diagonal_win(self, checker):
        # get the inverse slots
        self.getInverse()
        # set the boundary
        width_boundary = self.width - 4
        height_boundary = self.height - 4
        for i_r in range(width_boundary):
            for i_c in range(height_boundary):
                if self.inverse_slots[i_r][i_c] == self.inverse_slots[i_r + 1][i_c + 1] == self.inverse_slots[i_r + 2][i_c + 2] == self.inverse_slots[i_r + 3][i_c + 3] and self.inverse_slots[i_r][i_c] == checker:
                    return True
        return False

    def is_up_diagonal_win (self, checker):
        # get the inverse slots
        self.getInverse()
        # set the boundary
        width_boundary = self.width - 4
        height_boundary = self.height - 4
        for i_r in range(width_boundary):
            for i_c in range(height_boundary, self.height):
                if self.inverse_slots[i_r][i_c] == self.inverse_slots[i_r + 1][i_c - 1] == self.inverse_slots[i_r + 2][i_c - 2] == self.inverse_slots[i_r + 3][i_c - 3] and self.inverse_slots[i_r][i_c] == checker:
                    return True
        return False





