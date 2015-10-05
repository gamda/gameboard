import unittest
from gameboard import Gameboard
from gameboard import Coordinates

class TestSquares(unittest.TestCase):
    
    pass

class TestBoard(unittest.TestCase):

    def test_64_squares(self):
        board = Gameboard()
        self.assertEqual(len(board.squares),64)

if __name__ == '__main__':
    unittest.main()