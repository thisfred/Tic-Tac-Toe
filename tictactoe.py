"""Implementation of Tic Tac Toe."""


class InvalidPosition(Exception):
    """Not a valid board position."""


class OutOfTurn(Exception):
    """Attempting to play out of turn."""


class Board(object):
    """The game board."""

    def __init__(self):
        self.positions = []
        self.players = [1, 2]
        for i in range(3):
            self.positions.append([None, None, None])

    def get_piece(self, x, y):
        """Return the piece at position (x, y) if any or None."""
        return self.positions[y][x]

    def get_pieces(self, player):
        """Return a list of played pieces for player."""
        for y, col in enumerate(self.positions):
            for x, row in enumerate(col):
                if row == player:
                    yield x, y

    def other_player(self, player):
        for pl in self.players:
            if pl != player:
                return pl

    def play(self, x, y, player):
        """Put player's piece in position (x, y)."""
        if x < 0 or y < 0:
            raise InvalidPosition
        try:
            current = self.positions[y][x]
        except IndexError:
            raise InvalidPosition("Position (%d, %d) out of bounds." % (x, y))
        except TypeError:
            raise InvalidPosition("Illegal position (%r, %r)." % (x, y))
        if current is not None:
            raise InvalidPosition(
                "Already occupied by player %s" % (current,))
        if (len(set(self.get_pieces(player))) >
                len(set(self.get_pieces(self.other_player(player))))):
            raise OutOfTurn("It's not player %s's turn." % (player,))
        self.positions[y][x] = player
