"""Implementation of Tic Tac Toe."""


class InvalidPosition(Exception):
    """Not a valid board position."""


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
        if x < 0 or y < 0:
            raise InvalidPosition
        try:
            current = self.positions[x][y]
        except IndexError:
            raise InvalidPosition("Position (%d, %d) out of bounds." % (x, y))
        except TypeError:
            raise InvalidPosition("Illegal position (%r, %r)." % (x, y))
        if current is not None:
            raise InvalidPosition(
                "Already occupied by player %s" % (current,))
        self.positions[x][y] = player
