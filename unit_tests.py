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

    def test_row_for_square_raises_TypeError(self):
        self.assertRaises(TypeError,self.board.rowForSquare,"bleh")

    def test_row_for_square(self):
        boardAnswer = self.board.rowForSquare(Coordinate.d5)
        correctAnswer = {Coordinate.a5,
                        Coordinate.b5,
                        Coordinate.c5,
                        Coordinate.d5,
                        Coordinate.e5,
                        Coordinate.f5,
                        Coordinate.g5,
                        Coordinate.h5}
        self.assertEqual(boardAnswer,correctAnswer)

    def test_column_for_square_raises_TypeError(self):
        self.assertRaises(TypeError,self.board.columnForSquare,"bleh")

    def test_column_for_square(self):
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

    def test_row_and_column_for_square_raises_TypeError(self):
        self.assertRaises(TypeError,self.board.columnForSquare,"bleh")

    def test_row_and_column_for_square(self):
        boardAnswer = self.board.rowAndColumnForSquare(Coordinate.b4)
        correctAnswer = {Coordinate.b1,
                        Coordinate.b2,
                        Coordinate.b3,
                        Coordinate.b4,
                        Coordinate.b5,
                        Coordinate.b6,
                        Coordinate.b7,
                        Coordinate.b8,
                        Coordinate.a4,
                        Coordinate.c4,
                        Coordinate.d4,
                        Coordinate.e4,
                        Coordinate.f4,
                        Coordinate.g4,
                        Coordinate.h4}
        self.assertEqual(boardAnswer,correctAnswer)

    def test_diagonals_for_square_raises_TypeError(self):
        self.assertRaises(TypeError,self.board.columnForSquare,"bleh")

    def test_diagonals_for_square(self):
        boardAnswer = self.board.diagonalsForSquare(Coordinate.d4)
        correctAnswer = {Coordinate.a1,
                        Coordinate.b2,
                        Coordinate.c3,
                        Coordinate.d4,
                        Coordinate.e5,
                        Coordinate.f6,
                        Coordinate.g7,
                        Coordinate.h8,
                        Coordinate.a7,
                        Coordinate.b6,
                        Coordinate.c5,
                        Coordinate.e3,
                        Coordinate.f2,
                        Coordinate.g1}
        self.assertEqual(boardAnswer,correctAnswer)

if __name__ == '__main__':
    unittest.main()