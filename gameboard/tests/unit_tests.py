import unittest
import random
from gameboard.gameboard import Gameboard, Direction
from gameboard.coordinate import Coordinate

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

    def test_neighbor_top_with_top_square(self):
        n = self.board._neighborTop(Coordinate.a8)
        self.assertEqual(n, None)

    def test_neighbor_top(self):
        n = self.board._neighborTop(Coordinate.d3)
        self.assertEqual(n, Coordinate.d4)

    def test_neighbor_top_right_with_top_square(self):
        n = self.board._neighborTopRight(Coordinate.b8)
        self.assertEqual(n, None)

    def test_neighbor_top_right_with_right_square(self):
        n = self.board._neighborTopRight(Coordinate.h5)
        self.assertEqual(n, None)

    def test_neighbor_top_right(self):
        n = self.board._neighborTopRight(Coordinate.f3)
        self.assertEqual(n, Coordinate.g4)

    def test_neighbor_right_with_right_square(self):
        n = self.board._neighborRight(Coordinate.h5)
        self.assertEqual(n, None)

    def test_neighbor_right(self):
        n = self.board._neighborRight(Coordinate.d3)
        self.assertEqual(n, Coordinate.e3)

    def test_neighbor_btm_right_with_btm_square(self):
        n = self.board._neighborBtmRight(Coordinate.b1)
        self.assertEqual(n, None)

    def test_neighbor_btm_right_with_right_square(self):
        n = self.board._neighborBtmRight(Coordinate.h5)
        self.assertEqual(n, None)

    def test_neighbor_btm_right(self):
        n = self.board._neighborBtmRight(Coordinate.f3)
        self.assertEqual(n, Coordinate.g2)

    def test_neighbor_btm_with_btm_square(self):
        n = self.board._neighborBtm(Coordinate.a1)
        self.assertEqual(n, None)

    def test_neighbor_btm(self):
        n = self.board._neighborBtm(Coordinate.d3)
        self.assertEqual(n, Coordinate.d2)

    def test_neighbor_btm_left_with_btm_square(self):
        n = self.board._neighborBtmLeft(Coordinate.b1)
        self.assertEqual(n, None)

    def test_neighbor_btm_left_with_left_square(self):
        n = self.board._neighborBtmLeft(Coordinate.a6)
        self.assertEqual(n, None)

    def test_neighbor_btm_left(self):
        n = self.board._neighborBtmLeft(Coordinate.f3)
        self.assertEqual(n, Coordinate.e2)

    def test_neighbor_left_with_left_square(self):
        n = self.board._neighborLeft(Coordinate.a5)
        self.assertEqual(n, None)

    def test_neighbor_left(self):
        n = self.board._neighborLeft(Coordinate.d3)
        self.assertEqual(n, Coordinate.c3)

    def test_neighbor_top_left_with_top_square(self):
        n = self.board._neighborTopLeft(Coordinate.b8)
        self.assertEqual(n, None)

    def test_neighbor_top_left_with_left_square(self):
        n = self.board._neighborTopLeft(Coordinate.a5)
        self.assertEqual(n, None)

    def test_neighbor_top_left(self):
        n = self.board._neighborTopLeft(Coordinate.f3)
        self.assertEqual(n, Coordinate.e4)

    def test_neighbor_in_direction_raises_TypeError(self):
        self.assertRaises(TypeError, self.board.neighborInDirection,
            square = "notCoordinate",
            direction = Direction.top)
        self.assertRaises(TypeError, self.board.neighborInDirection,
            square = Coordinate.a1,
            direction = "notDirection")

    def test_neighbor_in_direction_top(self):
        n = self.board.neighborInDirection(Coordinate.d3, Direction.top)
        self.assertEqual(n, Coordinate.d4)

    def test_neighbor_in_direction_top_right(self):
        n = self.board.neighborInDirection(Coordinate.d3, Direction.topRight)
        self.assertEqual(n, Coordinate.e4)

    def test_neighbor_in_direction_right(self):
        n = self.board.neighborInDirection(Coordinate.d3, Direction.right)
        self.assertEqual(n, Coordinate.e3)

    def test_neighbor_in_direction_btm_right(self):
        n = self.board.neighborInDirection(Coordinate.d3, Direction.btmRight)
        self.assertEqual(n, Coordinate.e2)

    def test_neighbor_in_direction_btm(self):
        n = self.board.neighborInDirection(Coordinate.d3, Direction.btm)
        self.assertEqual(n, Coordinate.d2)

    def test_neighbor_in_directino_btm_left(self):
        n = self.board.neighborInDirection(Coordinate.d3, Direction.btmLeft)
        self.assertEqual(n, Coordinate.c2)

    def test_neighbor_in_direction_left(self):
        n = self.board.neighborInDirection(Coordinate.d3, Direction.left)
        self.assertEqual(n, Coordinate.c3)

    def test_neighbor_in_direction_top_left(self):
        n = self.board.neighborInDirection(Coordinate.d3, Direction.topLeft)
        self.assertEqual(n, Coordinate.c4)

    def test_neighbors_raises_TypeError(self):
        self.assertRaises(TypeError,self.board.neighbors,"notCoordinate")

    def test_neighbors_corner(self):
        n = self.board.neighbors(Coordinate.a1)
        correct = {Direction.top: Coordinate.a2,
                    Direction.topRight: Coordinate.b2,
                    Direction.right: Coordinate.b1,
                    Direction.btmRight: None,
                    Direction.btm: None,
                    Direction.btmLeft: None,
                    Direction.left: None,
                    Direction.topLeft: None}
        self.assertEqual(n, correct)

    def test_neighbors_top(self):
        n = self.board.neighbors(Coordinate.c8)
        correct = {Direction.top: None,
                    Direction.topRight: None,
                    Direction.right: Coordinate.d8,
                    Direction.btmRight: Coordinate.d7,
                    Direction.btm: Coordinate.c7,
                    Direction.btmLeft: Coordinate.b7,
                    Direction.left: Coordinate.b8,
                    Direction.topLeft: None}
        self.assertEqual(n, correct)

    def test_neighbors_right(self):
        n = self.board.neighbors(Coordinate.h7)
        correct = {Direction.top: Coordinate.h8,
                    Direction.topRight: None,
                    Direction.right: None,
                    Direction.btmRight: None,
                    Direction.btm: Coordinate.h6,
                    Direction.btmLeft: Coordinate.g6,
                    Direction.left: Coordinate.g7,
                    Direction.topLeft: Coordinate.g8}
        self.assertEqual(n, correct)

    def test_neighbors_bottom(self):
        n = self.board.neighbors(Coordinate.d1)
        correct = {Direction.top: Coordinate.d2,
                    Direction.topRight: Coordinate.e2,
                    Direction.right: Coordinate.e1,
                    Direction.btmRight: None,
                    Direction.btm: None,
                    Direction.btmLeft: None,
                    Direction.left: Coordinate.c1,
                    Direction.topLeft: Coordinate.c2}
        self.assertEqual(n, correct)

    def test_neighbors_left(self):
        n = self.board.neighbors(Coordinate.a5)
        correct = {Direction.top: Coordinate.a6,
                    Direction.topRight: Coordinate.b6,
                    Direction.right: Coordinate.b5,
                    Direction.btmRight: Coordinate.b4,
                    Direction.btm: Coordinate.a4,
                    Direction.btmLeft: None,
                    Direction.left: None,
                    Direction.topLeft: None}
        self.assertEqual(n, correct)

    def test_neighbors_center(self):
        n = self.board.neighbors(Coordinate.d3)
        correct = {Direction.top: Coordinate.d4,
                    Direction.topRight: Coordinate.e4,
                    Direction.right: Coordinate.e3,
                    Direction.btmRight: Coordinate.e2,
                    Direction.btm: Coordinate.d2,
                    Direction.btmLeft: Coordinate.c2,
                    Direction.left: Coordinate.c3,
                    Direction.topLeft: Coordinate.c4}
        self.assertEqual(n, correct)

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