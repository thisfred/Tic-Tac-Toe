"""Tests for tictactoe.py."""

from unittest import TestCase
from tictactoe import Board


class BoardTests(TestCase):
    """Tests for the Board class."""

    def test_init(self):
        board = Board()
        for x in range(3):
            for y in range(3):
                self.assertEqual(None, board.get_piece(x, y))
