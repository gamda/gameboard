import unittest
from gameboard import Gameboard
from coordinate import Coordinate

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
        index = self.board._indexOf(Coordinate.a1)
        self.assertEqual(index,(7,0))

    def test_index_of_coordinate_top(self):
        index = self.board._indexOf(Coordinate.c8)
        self.assertEqual(index,(0,2))

    def test_index_of_coordinate_right(self):
        index = self.board._indexOf(Coordinate.h7)
        self.assertEqual(index,(1,7))

    def test_index_of_coordinate_bottom(self):
        index = self.board._indexOf(Coordinate.d1)
        self.assertEqual(index,(7,3))

    def test_index_of_coordinate_left(self):
        index = self.board._indexOf(Coordinate.a5)
        self.assertEqual(index,(3,0))

    def test_column_raises_TypeError(self):
        self.assertRaises(TypeError,self.board.columnForSquare,"bleh")

    def test_column_given_square(self):
        boardAnswer = self.board.columnForSquare(Coordinate.a1)
        correctAnswer = {Coordinate.a1,
                        Coordinate.a2,
                        Coordinate.a3,
                        Coordinate.a4,
                        Coordinate.a5,
                        Coordinate.a6,
                        Coordinate.a7,
                        Coordinate.a8}
        self.assertEqual(boardAnswer,correctAnswer)

if __name__ == '__main__':
    unittest.main()