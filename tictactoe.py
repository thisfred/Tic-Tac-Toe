"""Implementation of Tic Tac Toe."""


class Board(object):

    def __init__(self):
        self.positions = []
        for i in range(3):
            self.positions.append([None, None, None])

    def get_piece(self, x, y):
        return self.positions[x][y]

