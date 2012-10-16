"""Tests for tictactoe.py."""

from unittest import TestCase
from tictactoe import Board, InvalidPosition, OutOfTurn


class BoardTests(TestCase):
    """Tests for the Board class."""

    def setUp(self):
        self.board = Board()

    def test_init(self):
        """Init results in empty board."""
        for x in range(3):
            for y in range(3):
                self.assertEqual(None, self.board.get_piece(x, y))

    def test_play(self):
        """Playing a piece changes the board."""
        player = 1
        x = 1
        y = 2
        self.board.play(x, y, player)
        self.assertEqual(player, self.board.get_piece(x, y))

    def test_out_of_bounds(self):
        """Playing out of bounds raises an exception."""
        player = 1
        self.assertRaises(InvalidPosition, self.board.play, 3, 1, player)
        self.assertRaises(InvalidPosition, self.board.play, 1, 3, player)
        self.assertRaises(InvalidPosition, self.board.play, -1, 1, player)
        self.assertRaises(InvalidPosition, self.board.play, 1, -1, player)

    def test_invalid_coordinate_values(self):
        """Non-integer coordinates raise an exception."""
        player = 1
        self.assertRaises(InvalidPosition, self.board.play, '3', 1, player)
        self.assertRaises(
            InvalidPosition, self.board.play, 1, 'wednesday', player)

    def test_occupied(self):
        """Playing to an occupied position raises an exception."""
        player = 1
        self.board.positions[2][2] = 2
        self.assertRaises(InvalidPosition, self.board.play, 2, 2, player)

    def test_out_of_turn(self):
        """Playing out of turn raises an exception."""
        player = 1
        self.board.play(2, 2, player)
        self.assertRaises(OutOfTurn, self.board.play, 1, 2, player)
