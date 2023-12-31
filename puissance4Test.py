import unittest
import numpy as np
from io import StringIO
from unittest.mock import patch

from puissance4 import create_board, print_board, drop_piece, is_valid_location, winning_move, reverse_board, reverse_single_col


class TestPuissance4(unittest.TestCase):

    def setUp(self):
        self.board = create_board()

    def test_create_board(self):
        self.assertTrue(np.array_equal(self.board, np.zeros((6, 7), dtype=int)))

    def test_drop_piece(self):
        drop_piece(self.board, 2, 1)
        self.assertEqual(self.board[5][2], 1)

    def test_reverse_board(self):
        drop_piece(self.board, 2, 1)
        drop_piece(self.board, 2, 1)
        drop_piece(self.board, 2, 2)
        drop_piece(self.board, 2, 2)
        self.assertEqual(self.board[len(self.board) - 1][2], 1)
        tmp_board = reverse_board(self.board)
        self.assertTrue(tmp_board[len(tmp_board) - 1][2], 2)
    
    def test_reverse_single_col(self):
        drop_piece(self.board, 2, 1)
        drop_piece(self.board, 2, 1)
        drop_piece(self.board, 2, 2)
        drop_piece(self.board, 2, 2)
        self.assertEqual(self.board[len(self.board) - 1][2], 1)
        tmp_board = reverse_single_col(self.board, 2)
        print(tmp_board)
        self.assertTrue(tmp_board[len(tmp_board) - 1][2], 2)

    def test_is_valid_location(self):
        self.assertTrue(is_valid_location(self.board, 3))
        drop_piece(self.board, 3, 1)
        self.assertFalse(is_valid_location(self.board, 8))

    def test_winning_move_horizontal(self):
        for col in range(1, 5):
            drop_piece(self.board, col, 1)
        self.assertTrue(winning_move(self.board, 1))

    def test_winning_move_vertical(self):
        drop_piece(self.board, 2, 1)
        drop_piece(self.board, 2, 1)
        drop_piece(self.board, 2, 1)
        drop_piece(self.board, 2, 1)
        self.assertTrue(winning_move(self.board, 1))

    def test_winning_move_diagonal_positive_slope(self):
        for i in range(3):
            drop_piece(self.board, i, 1)
            drop_piece(self.board, i, 2)
        drop_piece(self.board, 3, 1)
        drop_piece(self.board, 4, 1)
        drop_piece(self.board, 4, 1)
        drop_piece(self.board, 5, 1)
        self.assertTrue(winning_move(self.board, 1))

    def test_winning_move_diagonal_negative_slope(self):
        for i in range(3):
            drop_piece(self.board, i, 1)
            drop_piece(self.board, i, 2)
        drop_piece(self.board, 3, 1)
        drop_piece(self.board, 2, 1)
        drop_piece(self.board, 2, 1)
        drop_piece(self.board, 1, 1)
        self.assertTrue(winning_move(self.board, 1))

if __name__ == "__main__":
    unittest.main()
