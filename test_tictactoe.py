"""Tests for tictactoe.py."""

from unittest import TestCase
from tictactoe import Board, InvalidPosition


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
        self.assertRaises(InvalidPosition, self.board.play, player, 3, 1)
        self.assertRaises(InvalidPosition, self.board.play, player, 1, 3)
        self.assertRaises(InvalidPosition, self.board.play, player, -1, 1)
        self.assertRaises(InvalidPosition, self.board.play, player, 1, -1)
