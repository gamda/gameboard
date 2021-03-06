# Copyright (c) 2015 Daniel Garcia
#
# See the file LICENSE.txt for copying permission.

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
        n = self.board._neighbor_top(Coordinate.a8)
        self.assertEqual(n, None)

    def test_neighbor_top(self):
        n = self.board._neighbor_top(Coordinate.d3)
        self.assertEqual(n, Coordinate.d4)

    def test_neighbor_top_right_with_top_square(self):
        n = self.board._neighbor_top_right(Coordinate.b8)
        self.assertEqual(n, None)

    def test_neighbor_top_right_with_right_square(self):
        n = self.board._neighbor_top_right(Coordinate.h5)
        self.assertEqual(n, None)

    def test_neighbor_top_right(self):
        n = self.board._neighbor_top_right(Coordinate.f3)
        self.assertEqual(n, Coordinate.g4)

    def test_neighbor_right_with_right_square(self):
        n = self.board._neighbor_right(Coordinate.h5)
        self.assertEqual(n, None)

    def test_neighbor_right(self):
        n = self.board._neighbor_right(Coordinate.d3)
        self.assertEqual(n, Coordinate.e3)

    def test_neighbor_btm_right_with_btm_square(self):
        n = self.board._neighbor_btm_right(Coordinate.b1)
        self.assertEqual(n, None)

    def test_neighbor_btm_right_with_right_square(self):
        n = self.board._neighbor_btm_right(Coordinate.h5)
        self.assertEqual(n, None)

    def test_neighbor_btm_right(self):
        n = self.board._neighbor_btm_right(Coordinate.f3)
        self.assertEqual(n, Coordinate.g2)

    def test_neighbor_btm_with_btm_square(self):
        n = self.board._neighbor_btm(Coordinate.a1)
        self.assertEqual(n, None)

    def test_neighbor_btm(self):
        n = self.board._neighbor_btm(Coordinate.d3)
        self.assertEqual(n, Coordinate.d2)

    def test_neighbor_btm_left_with_btm_square(self):
        n = self.board._neighbor_btm_left(Coordinate.b1)
        self.assertEqual(n, None)

    def test_neighbor_btm_left_with_left_square(self):
        n = self.board._neighbor_btm_left(Coordinate.a6)
        self.assertEqual(n, None)

    def test_neighbor_btm_left(self):
        n = self.board._neighbor_btm_left(Coordinate.f3)
        self.assertEqual(n, Coordinate.e2)

    def test_neighbor_left_with_left_square(self):
        n = self.board._neighbor_left(Coordinate.a5)
        self.assertEqual(n, None)

    def test_neighbor_left(self):
        n = self.board._neighbor_left(Coordinate.d3)
        self.assertEqual(n, Coordinate.c3)

    def test_neighbor_top_left_with_top_square(self):
        n = self.board._neighbor_top_left(Coordinate.b8)
        self.assertEqual(n, None)

    def test_neighbor_top_left_with_left_square(self):
        n = self.board._neighbor_top_left(Coordinate.a5)
        self.assertEqual(n, None)

    def test_neighbor_top_left(self):
        n = self.board._neighbor_top_left(Coordinate.f3)
        self.assertEqual(n, Coordinate.e4)

    def test_neighbor_in_direction_raises_TypeError(self):
        self.assertRaises(TypeError, self.board.neighbor_in_direction,
            square = "notCoordinate",
            direction = Direction.top)
        self.assertRaises(TypeError, self.board.neighbor_in_direction,
            square = Coordinate.a1,
            direction = "notDirection")

    def test_neighbor_in_direction_top(self):
        n = self.board.neighbor_in_direction(Coordinate.d3, Direction.top)
        self.assertEqual(n, Coordinate.d4)

    def test_neighbor_in_direction_top_right(self):
        n = self.board.neighbor_in_direction(Coordinate.d3, Direction.top_right)
        self.assertEqual(n, Coordinate.e4)

    def test_neighbor_in_direction_right(self):
        n = self.board.neighbor_in_direction(Coordinate.d3, Direction.right)
        self.assertEqual(n, Coordinate.e3)

    def test_neighbor_in_direction_btm_right(self):
        n = self.board.neighbor_in_direction(Coordinate.d3, Direction.btm_right)
        self.assertEqual(n, Coordinate.e2)

    def test_neighbor_in_direction_btm(self):
        n = self.board.neighbor_in_direction(Coordinate.d3, Direction.btm)
        self.assertEqual(n, Coordinate.d2)

    def test_neighbor_in_directino_btm_left(self):
        n = self.board.neighbor_in_direction(Coordinate.d3, Direction.btm_left)
        self.assertEqual(n, Coordinate.c2)

    def test_neighbor_in_direction_left(self):
        n = self.board.neighbor_in_direction(Coordinate.d3, Direction.left)
        self.assertEqual(n, Coordinate.c3)

    def test_neighbor_in_direction_top_left(self):
        n = self.board.neighbor_in_direction(Coordinate.d3, Direction.top_left)
        self.assertEqual(n, Coordinate.c4)

    def test_neighbors_raises_TypeError(self):
        self.assertRaises(TypeError,self.board.neighbors,"notCoordinate")

    def test_neighbors_corner(self):
        n = self.board.neighbors(Coordinate.a1)
        correct = {Direction.top: Coordinate.a2,
                    Direction.top_right: Coordinate.b2,
                    Direction.right: Coordinate.b1,
                    Direction.btm_right: None,
                    Direction.btm: None,
                    Direction.btm_left: None,
                    Direction.left: None,
                    Direction.top_left: None}
        self.assertEqual(n, correct)

    def test_neighbors_top(self):
        n = self.board.neighbors(Coordinate.c8)
        correct = {Direction.top: None,
                    Direction.top_right: None,
                    Direction.right: Coordinate.d8,
                    Direction.btm_right: Coordinate.d7,
                    Direction.btm: Coordinate.c7,
                    Direction.btm_left: Coordinate.b7,
                    Direction.left: Coordinate.b8,
                    Direction.top_left: None}
        self.assertEqual(n, correct)

    def test_neighbors_right(self):
        n = self.board.neighbors(Coordinate.h7)
        correct = {Direction.top: Coordinate.h8,
                    Direction.top_right: None,
                    Direction.right: None,
                    Direction.btm_right: None,
                    Direction.btm: Coordinate.h6,
                    Direction.btm_left: Coordinate.g6,
                    Direction.left: Coordinate.g7,
                    Direction.top_left: Coordinate.g8}
        self.assertEqual(n, correct)

    def test_neighbors_bottom(self):
        n = self.board.neighbors(Coordinate.d1)
        correct = {Direction.top: Coordinate.d2,
                    Direction.top_right: Coordinate.e2,
                    Direction.right: Coordinate.e1,
                    Direction.btm_right: None,
                    Direction.btm: None,
                    Direction.btm_left: None,
                    Direction.left: Coordinate.c1,
                    Direction.top_left: Coordinate.c2}
        self.assertEqual(n, correct)

    def test_neighbors_left(self):
        n = self.board.neighbors(Coordinate.a5)
        correct = {Direction.top: Coordinate.a6,
                    Direction.top_right: Coordinate.b6,
                    Direction.right: Coordinate.b5,
                    Direction.btm_right: Coordinate.b4,
                    Direction.btm: Coordinate.a4,
                    Direction.btm_left: None,
                    Direction.left: None,
                    Direction.top_left: None}
        self.assertEqual(n, correct)

    def test_neighbors_center(self):
        n = self.board.neighbors(Coordinate.d3)
        correct = {Direction.top: Coordinate.d4,
                    Direction.top_right: Coordinate.e4,
                    Direction.right: Coordinate.e3,
                    Direction.btm_right: Coordinate.e2,
                    Direction.btm: Coordinate.d2,
                    Direction.btm_left: Coordinate.c2,
                    Direction.left: Coordinate.c3,
                    Direction.top_left: Coordinate.c4}
        self.assertEqual(n, correct)

    def test_squares_in_direction_raises_TypeError(self):
        self.assertRaises(TypeError,self.board.squares_in_direction,
            origin = "notCoordinate",
            direction = Direction.top)
        self.assertRaises(TypeError, self.board.squares_in_direction,
            origin = Coordinate.a1,
            direction = "notDirection")

    def test_squares_in_direction_center_to_edge(self):
        s = self.board.squares_in_direction(Coordinate.d4, Direction.top)
        correct = [Coordinate.d5,
                   Coordinate.d6,
                   Coordinate.d7,
                   Coordinate.d8]
        self.assertEqual(s, correct)

    def test_squares_in_direction_along_edge(self):
        s = self.board.squares_in_direction(Coordinate.a5, Direction.btm)
        correct = [Coordinate.a4,
                   Coordinate.a3,
                   Coordinate.a2,
                   Coordinate.a1]
        self.assertEqual(s, correct)

    def test_squares_in_direction_edge_to_outside(self):
        s = self.board.squares_in_direction(Coordinate.a1, Direction.left)
        self.assertEqual(s, [])

    def test_squares_in_direction_with_non_empty_square_ignored(self):
        self.board.set_content(Coordinate.g5, "boo")
        s = self.board.squares_in_direction(Coordinate.a5, Direction.right)
        correct = [Coordinate.b5,
                   Coordinate.c5,
                   Coordinate.d5,
                   Coordinate.e5,
                   Coordinate.f5]
        self.assertEqual(s, correct)

    def test_squares_in_direction_with_non_empty_square_included(self):
        self.board.set_content(Coordinate.g5, "boo")
        s = self.board.squares_in_direction(Coordinate.d2, Direction.top_right,
            include_last_non_empty_square = True)
        correct = [Coordinate.e3,
                   Coordinate.f4,
                   Coordinate.g5]
        self.assertEqual(s, correct)

    def test_path_in_direction_raises_TypeError(self):
        self.assertRaises(TypeError, self.board.path_in_direction,
            origin = "notCoordinate",
            destination = Coordinate.a3,
            direction = Direction.top)
        self.assertRaises(TypeError, self.board.path_in_direction,
            origin = Coordinate.a1,
            destination = "notCoordinate",
            direction = Direction.btm)
        self.assertRaises(TypeError, self.board.path_in_direction,
            origin = Coordinate.a1,
            destination = Coordinate.b4,
            direction = "notDirection")

    def test_path_in_direction_top(self):
        path = self.board.path_in_direction(Coordinate.d3, Coordinate.d7, \
                                            Direction.top) 
        correctPath = [Coordinate.d4,
                        Coordinate.d5,
                        Coordinate.d6]
        self.assertEqual(path, correctPath)                  

    def test_path_in_direction_top_right(self):
        path = self.board.path_in_direction(Coordinate.a1, Coordinate.h8, \
                                            Direction.top_right)
        correctPath = [Coordinate.b2,
                        Coordinate.c3,
                        Coordinate.d4,
                        Coordinate.e5,
                        Coordinate.f6,
                        Coordinate.g7]
        self.assertEqual(path, correctPath)

    def test_path_in_direction_unreachable(self):
        path = self.board.path_in_direction(Coordinate.a8, Coordinate.h8, \
                                            Direction.btm)
        correctPath = []
        self.assertEqual(path, correctPath)

    def test_path_in_direction_out_of_bounds(self):
        path = self.board.path_in_direction(Coordinate.a8, Coordinate.a1, \
                                            Direction.left)
        correctPath = []
        self.assertEqual(path, correctPath)

    def test_square_content_raises_TypeError(self):
        self.assertRaises(TypeError,self.board.get_content,"notCoordinate")

    def test_square_content(self):
        self.board.set_content(Coordinate.a3, "white piece")
        self.assertEqual(self.board.get_content(Coordinate.a3), "white piece")

    def test_is_square_emtpy_raises_TypeError(self):
        self.assertRaises(TypeError,self.board.is_empty,"notCoordinate")

    def test_is_square_empty_true(self):
        self.assertTrue(self.board.is_empty(Coordinate.d2))

    def test_is_square_empty_false(self):
        self.board.set_content(Coordinate.e3, 2)
        self.assertFalse(self.board.is_empty(Coordinate.e3))

    def test_clear_square_raises_TypeError(self):
        self.assertRaises(TypeError,self.board.clear_square,"notCoordinate")

    def test_clear_square(self):
        self.board.set_content(Coordinate.h4, [1,2])
        self.board.clear_square(Coordinate.h4)
        self.assertTrue(self.board.is_empty(Coordinate.h4))

    def test_clear_board(self):
        for i in range(10):
            square = Coordinate(random.randrange(1,64))
            self.board.set_content(square,"pawn")
        self.board.clear_board()
        for square in Coordinate:
            self.assertTrue(self.board.is_empty(square))

    def test_move_content_raises_TypeError(self):
        self.assertRaises(TypeError,self.board.move,
            origin = Coordinate.a3,
            destination = "notCoordinate")
        self.assertRaises(TypeError,self.board.move,
            origin = "notCoordinate",
            destination = Coordinate.a3)

    def test_move_content(self):
        self.board.set_content(Coordinate.g8, "knight")
        self.board.move(Coordinate.g8, Coordinate.f6)
        self.assertEqual(self.board.get_content(Coordinate.f6),"knight")

if __name__ == '__main__':
    unittest.main()