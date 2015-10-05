import unittest
import random
from gameboard import Gameboard, Direction
from coordinate import Coordinate

class TestBoard(unittest.TestCase):

    def setUp(self):
        self.board = Gameboard()

    def test_64_squares(self):
        self.assertEqual(len(self.board._squares),64)

    def test_index_raises_TypeError(self):
        self.assertRaises(TypeError,self.board._indexOf,"notCoordinate")

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

    def test_index_of_coordinate_center(self):
        index = self.board._indexOf(Coordinate.d3)
        self.assertEqual(index,(5,3))

    def test_neighbors_raises_TypeError(self):
        self.assertRaises(TypeError,self.board.neighbors,"notCoordinate")

    def test_neighbors_top(self):
        corner = self.board.neighbors(Coordinate.a1)[Direction.top]
        self.assertEqual(corner, Coordinate.a2)
        top = self.board.neighbors(Coordinate.c8)[Direction.top]
        self.assertEqual(top, None)
        right = self.board.neighbors(Coordinate.h7)[Direction.top]
        self.assertEqual(right, Coordinate.h8)
        bottom = self.board.neighbors(Coordinate.d1)[Direction.top]
        self.assertEqual(bottom, Coordinate.d2)
        left = self.board.neighbors(Coordinate.a5)[Direction.top]
        self.assertEqual(left, Coordinate.a6)
        center = self.board.neighbors(Coordinate.d3)[Direction.top]
        self.assertEqual(center, Coordinate.d4)

    def test_neighbors_top_right(self):
        corner = self.board.neighbors(Coordinate.a1)[Direction.topRight]
        self.assertEqual(corner, Coordinate.b2)
        top = self.board.neighbors(Coordinate.c8)[Direction.topRight]
        self.assertEqual(top, None)
        right = self.board.neighbors(Coordinate.h7)[Direction.topRight]
        self.assertEqual(right, None)
        bottom = self.board.neighbors(Coordinate.d1)[Direction.topRight]
        self.assertEqual(bottom, Coordinate.e2)
        left = self.board.neighbors(Coordinate.a5)[Direction.topRight]
        self.assertEqual(left, Coordinate.b6)
        center = self.board.neighbors(Coordinate.d3)[Direction.topRight]
        self.assertEqual(center, Coordinate.e4)

    def test_neighbors_right(self):
        corner = self.board.neighbors(Coordinate.a1)[Direction.right]
        self.assertEqual(corner, Coordinate.b1)
        top = self.board.neighbors(Coordinate.c8)[Direction.right]
        self.assertEqual(top, Coordinate.d8)
        right = self.board.neighbors(Coordinate.h7)[Direction.right]
        self.assertEqual(right, None)
        bottom = self.board.neighbors(Coordinate.d1)[Direction.right]
        self.assertEqual(bottom, Coordinate.e1)
        left = self.board.neighbors(Coordinate.a5)[Direction.right]
        self.assertEqual(left, Coordinate.b5)
        center = self.board.neighbors(Coordinate.d3)[Direction.right]
        self.assertEqual(center, Coordinate.e3)

    def test_neighbors_btm_right(self):
        corner = self.board.neighbors(Coordinate.a1)[Direction.btmRight]
        self.assertEqual(corner, None)
        top = self.board.neighbors(Coordinate.c8)[Direction.btmRight]
        self.assertEqual(top, Coordinate.d7)
        right = self.board.neighbors(Coordinate.h7)[Direction.btmRight]
        self.assertEqual(right, None)
        bottom = self.board.neighbors(Coordinate.d1)[Direction.btmRight]
        self.assertEqual(bottom, None)
        left = self.board.neighbors(Coordinate.a5)[Direction.btmRight]
        self.assertEqual(left, Coordinate.b4)
        center = self.board.neighbors(Coordinate.d3)[Direction.btmRight]
        self.assertEqual(center, Coordinate.e2)

    def test_neighbors_btm(self):
        corner = self.board.neighbors(Coordinate.a1)[Direction.btm]
        self.assertEqual(corner, None)
        top = self.board.neighbors(Coordinate.c8)[Direction.btm]
        self.assertEqual(top, Coordinate.c7)
        right = self.board.neighbors(Coordinate.h7)[Direction.btm]
        self.assertEqual(right, Coordinate.h6)
        bottom = self.board.neighbors(Coordinate.d1)[Direction.btm]
        self.assertEqual(bottom, None)
        left = self.board.neighbors(Coordinate.a5)[Direction.btm]
        self.assertEqual(left, Coordinate.a4)
        center = self.board.neighbors(Coordinate.d3)[Direction.btm]
        self.assertEqual(center, Coordinate.d2)

    def test_neighbors_btm_left(self):
        corner = self.board.neighbors(Coordinate.a1)[Direction.btmLeft]
        self.assertEqual(corner, None)
        top = self.board.neighbors(Coordinate.c8)[Direction.btmLeft]
        self.assertEqual(top, Coordinate.b7)
        right = self.board.neighbors(Coordinate.h7)[Direction.btmLeft]
        self.assertEqual(right, Coordinate.g6)
        bottom = self.board.neighbors(Coordinate.d1)[Direction.btmLeft]
        self.assertEqual(bottom, None)
        left = self.board.neighbors(Coordinate.a5)[Direction.btmLeft]
        self.assertEqual(left, None)
        center = self.board.neighbors(Coordinate.d3)[Direction.btmLeft]
        self.assertEqual(center, Coordinate.c2)

    def test_neighbors_left(self):
        corner = self.board.neighbors(Coordinate.a1)[Direction.left]
        self.assertEqual(corner, None)
        top = self.board.neighbors(Coordinate.c8)[Direction.left]
        self.assertEqual(top, Coordinate.b8)
        right = self.board.neighbors(Coordinate.h7)[Direction.left]
        self.assertEqual(right, Coordinate.g7)
        bottom = self.board.neighbors(Coordinate.d1)[Direction.left]
        self.assertEqual(bottom, Coordinate.c1)
        left = self.board.neighbors(Coordinate.a5)[Direction.left]
        self.assertEqual(left, None)
        center = self.board.neighbors(Coordinate.d3)[Direction.left]
        self.assertEqual(center, Coordinate.c3)

    def test_neighbors_top_left(self):
        corner = self.board.neighbors(Coordinate.a1)[Direction.topLeft]
        self.assertEqual(corner, None)
        top = self.board.neighbors(Coordinate.c8)[Direction.topLeft]
        self.assertEqual(top, None)
        right = self.board.neighbors(Coordinate.h7)[Direction.topLeft]
        self.assertEqual(right, Coordinate.g8)
        bottom = self.board.neighbors(Coordinate.d1)[Direction.topLeft]
        self.assertEqual(bottom, Coordinate.c2)
        left = self.board.neighbors(Coordinate.a5)[Direction.topLeft]
        self.assertEqual(left, None)
        center = self.board.neighbors(Coordinate.d3)[Direction.topLeft]
        self.assertEqual(center, Coordinate.c4)

    def test_row_for_square_raises_TypeError(self):
        self.assertRaises(TypeError,self.board.rowForSquare,"notCoordinate")

    def test_row_for_square(self):
        boardAnswer = self.board.rowForSquare(Coordinate.d5)
        correctAnswer = [Coordinate.a5,
                        Coordinate.b5,
                        Coordinate.c5,
                        Coordinate.d5,
                        Coordinate.e5,
                        Coordinate.f5,
                        Coordinate.g5,
                        Coordinate.h5]
        self.assertEqual(sorted(boardAnswer),sorted(correctAnswer))

    def test_column_for_square_raises_TypeError(self):
        self.assertRaises(TypeError,self.board.columnForSquare,"notCoordinate")

    def test_column_for_square(self):
        boardAnswer = self.board.columnForSquare(Coordinate.a1)
        correctAnswer = [Coordinate.a1,
                        Coordinate.a2,
                        Coordinate.a3,
                        Coordinate.a4,
                        Coordinate.a5,
                        Coordinate.a6,
                        Coordinate.a7,
                        Coordinate.a8]
        self.assertEqual(sorted(boardAnswer),sorted(correctAnswer))

    def test_row_and_column_for_square_raises_TypeError(self):
        self.assertRaises(TypeError,self.board.columnForSquare,"notCoordinate")

    def test_row_and_column_for_square(self):
        boardAnswer = self.board.rowAndColumnForSquare(Coordinate.b4)
        correctAnswer = [Coordinate.b1,
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
                        Coordinate.h4]
        self.assertEqual(sorted(boardAnswer),sorted(correctAnswer))

    def test_diagonals_for_square_raises_TypeError(self):
        self.assertRaises(TypeError,self.board.columnForSquare,"notCoordinate")

    def test_diagonals_for_square(self):
        boardAnswer = self.board.diagonalsForSquare(Coordinate.d4)
        correctAnswer = [Coordinate.a1,
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
                        Coordinate.g1]
        self.assertEqual(sorted(boardAnswer),sorted(correctAnswer))

    def test_square_content_raises_TypeError(self):
        self.assertRaises(TypeError,self.board.getContent,"notCoordinate")

    def test_square_content(self):
        self.board.setContent(Coordinate.a3, "white piece")
        self.assertEqual(self.board.getContent(Coordinate.a3), "white piece")

    def test_is_square_emtpy_raises_TypeError(self):
        self.assertRaises(TypeError,self.board.isEmpty,"notCoordinate")

    def test_is_square_empty_true(self):
        self.assertTrue(self.board.isEmpty(Coordinate.d2))

    def test_is_square_empty_false(self):
        self.board.setContent(Coordinate.e3, 2)
        self.assertFalse(self.board.isEmpty(Coordinate.e3))

    def test_clear_square_raises_TypeError(self):
        self.assertRaises(TypeError,self.board.clearSquare,"notCoordinate")

    def test_clear_square(self):
        self.board.setContent(Coordinate.h4, [1,2])
        self.board.clearSquare(Coordinate.h4)
        self.assertTrue(self.board.isEmpty(Coordinate.h4))

    def test_clear_board(self):
        for i in range(10):
            square = Coordinate(random.randrange(1,64))
            self.board.setContent(square,"pawn")
        self.board.clearBoard()
        for square in Coordinate:
            self.assertTrue(self.board.isEmpty(square))

    def test_move_content_raises_TypeError(self):
        self.assertRaises(TypeError,self.board.move,
            origin = Coordinate.a3,
            destination = "notCoordinate")
        self.assertRaises(TypeError,self.board.move,
            origin = "notCoordinate",
            destination = Coordinate.a3)

    def test_move_content(self):
        self.board.setContent(Coordinate.g8, "knight")
        self.board.move(Coordinate.g8, Coordinate.f6)
        self.assertEqual(self.board.getContent(Coordinate.f6),"knight")

if __name__ == '__main__':
    unittest.main()