"""Implementation of Tic Tac Toe."""


class Board(object):
    """The game board."""

    def __init__(self):
        self.positions = []
        for i in range(3):
            self.positions.append([None, None, None])

    def get_piece(self, x, y):
        """Return the piece at position (x, y) if any or None."""
        return self.positions[x][y]

    def play(self, x, y, player):
        """Put player's piece in position (x, y)."""
        self.positions[x][y] = player
