import unittest
from gameboard import Gameboard
from gameboard import Coordinates

class TestSquares(unittest.TestCase):
    
    pass

class Testboard(unittest.TestCase):

    def setUp(self):
        self.board = Gameboard()

    def test_64_squares(self):
        self.assertEqual(len(self.board.squares),64)

    def test_index_raises_TypeError(self):
        self.assertRaises(TypeError,self.board._indexOf,"bleh")

    def test_index_of_coordinate_corner(self):
        index = self.board._indexOf(Coordinates.a1)
        self.assertEqual(index,(7,0))

    def test_index_of_coordinate_top(self):
        index = self.board._indexOf(Coordinates.c8)
        self.assertEqual(index,(0,2))

    def test_index_of_coordinate_right(self):
        index = self.board._indexOf(Coordinates.h7)
        self.assertEqual(index,(1,7))

    def test_index_of_coordinate_bottom(self):
        index = self.board._indexOf(Coordinates.d1)
        self.assertEqual(index,(7,3))

    def test_index_of_coordinate_left(self):
        index = self.board._indexOf(Coordinates.a5)
        self.assertEqual(index,(3,0))

    def test_column_raises_TypeError(self):
        self.assertRaises(TypeError,self.board.columnForSquare,"bleh")

    def test_column_given_square(self):
        boardAnswer = self.board.columnForSquare(Coordinates.a1)
        correctAnswer = [Coordinates.a1,
                        Coordinates.a2,
                        Coordinates.a3,
                        Coordinates.a4,
                        Coordinates.a5,
                        Coordinates.a6,
                        Coordinates.a7,
                        Coordinates.a8]
        self.assertEqual(boardAnswer,correctAnswer)

if __name__ == '__main__':
    unittest.main()