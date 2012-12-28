import unittest
import tictactoe as ttt


class AIPlayerTests(unittest.TestCase):
    """Test the AIPlayer class"""

    def setUp(self):
        self.player = ttt.AIPlayer('X')

    def test_look_for_win_no_wins(self):
        """Test AIPlayer.look_for_win() when there are no possible wins"""

        board = ttt.Board()

        # Check several non-winning board layouts which
        # cover several distinct categories of situations
        self.assertEqual(None, self.player.look_for_win(board))

        board.tttboard = ['Y', None, 'Y',
                          None, None, None,
                          None, None, None]
        self.assertEqual(None, self.player.look_for_win(board))

        board.tttboard = ['X', None, None,
                          None, None, None,
                          None, None, None]
        self.assertEqual(None, self.player.look_for_win(board))

        board.tttboard = ['X', None, None,
                          None, None, 'X',
                          None, None, None]
        self.assertEqual(None, self.player.look_for_win(board))

    def test_look_for_win_winner(self):
        """Test AIPlayer.look_for_win() when there are possible wins"""

        board = ttt.Board()
        board.tttboard = ['X', None, 'X',
                          None, None, None,
                          None, None, None]
        self.assertEqual(1, self.player.look_for_win(board))

        board.tttboard = ['X', None, None,
                          None, None, None,
                          None, None, 'X']
        self.assertEqual(4, self.player.look_for_win(board))


if __name__ == '__main__':
    unittest.main()

