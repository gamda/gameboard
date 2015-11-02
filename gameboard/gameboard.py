# Copyright (c) 2015 Daniel Garcia
#
# See the file LICENSE.txt for copying permission.

from enum import Enum
from gameboard.coordinate import Coordinate

class Direction(Enum):
    top = 1
    top_right = 2
    right = 3
    btm_right = 4
    btm = 5
    btm_left = 6
    left = 7
    top_left = 8


SHIFT_SQUARE = 1
SHIFT_LETTER = 8 # because adding and substracting 8 will shift a column

class Gameboard:

    rows = [[Coordinate.a8, Coordinate.b8, Coordinate.c8, Coordinate.d8, 
                Coordinate.e8, Coordinate.f8, Coordinate.g8, Coordinate.h8],
            [Coordinate.a7, Coordinate.b7, Coordinate.c7, Coordinate.d7, 
                Coordinate.e7, Coordinate.f7, Coordinate.g7, Coordinate.h7],
            [Coordinate.a6, Coordinate.b6, Coordinate.c6, Coordinate.d6, 
                Coordinate.e6, Coordinate.f6, Coordinate.g6, Coordinate.h6],
            [Coordinate.a5, Coordinate.b5, Coordinate.c5, Coordinate.d5, 
                Coordinate.e5, Coordinate.f5, Coordinate.g5, Coordinate.h5],
            [Coordinate.a4, Coordinate.b4, Coordinate.c4, Coordinate.d4, 
                Coordinate.e4, Coordinate.f4, Coordinate.g4, Coordinate.h4],
            [Coordinate.a3, Coordinate.b3, Coordinate.c3, Coordinate.d3, 
                Coordinate.e3, Coordinate.f3, Coordinate.g3, Coordinate.h3],
            [Coordinate.a2, Coordinate.b2, Coordinate.c2, Coordinate.d2, 
                Coordinate.e2, Coordinate.f2, Coordinate.g2, Coordinate.h2],
            [Coordinate.a1, Coordinate.b1, Coordinate.c1, Coordinate.d1, 
                Coordinate.e1, Coordinate.f1, Coordinate.g1, Coordinate.h1]]

    @property
    def moves(self):
        """List of tuples of the form (origin, destination), both Coordinate"""
        return self._moves
    
    def __init__(self):
        self._squares = {}
        for k in Coordinate:
            self._squares[k] = None
        self._moves = []

    def _indexOf(self, square):
        """Returns a tuple with the index of given square in self.rows

        Args:
            square (Coordinate): the square to find index for
        Returns:
            tuple: it has the form (x,y). The square can be found by accessing
            self.rows[x][y]
        Raises:
            TypeError: if square is not of type Coordinate

        """
        if not isinstance(square, Coordinate):
            raise TypeError("square variable must be from Coordinate enum")
        for i in range(len(self.rows)):
            if square in self.rows[i]:
                return (i,self.rows[i].index(square))

    def _neighbor_top(self, square):
        top = square + SHIFT_SQUARE
        if top // SHIFT_LETTER == square // SHIFT_LETTER:
            return Coordinate(top)
        return None

    def _neighbor_top_right(self, square):
        tr = square + SHIFT_LETTER + SHIFT_SQUARE
        if tr // SHIFT_LETTER == square // SHIFT_LETTER + 1 and \
           tr < 64: # make sure it's a column to the right and not OB
            return Coordinate(tr)
        return None

    def _neighbor_right(self, square):
        right = square + SHIFT_LETTER
        if right // SHIFT_LETTER == square // SHIFT_LETTER + 1 and \
           right < 64:
            return Coordinate(right)
        return None

    def _neighbor_btm_right(self, square):
        br = square + SHIFT_LETTER - SHIFT_SQUARE
        if br // SHIFT_LETTER == square // SHIFT_LETTER + 1 and \
           br < 64:
            return Coordinate(br)
        return None

    def _neighbor_btm(self, square):
        btm = square - SHIFT_SQUARE
        if (btm // SHIFT_LETTER) == (square // SHIFT_LETTER):
            return Coordinate(btm)
        return None

    def _neighbor_btm_left(self, square):
        bl = square - SHIFT_LETTER - SHIFT_SQUARE
        if bl // SHIFT_LETTER == square // SHIFT_LETTER - 1 and \
           bl >= 0:
            return Coordinate(bl)
        return None

    def _neighbor_left(self, square):
        left = square - SHIFT_LETTER
        if left // SHIFT_LETTER == square // SHIFT_LETTER - 1 and \
           left >= 0:
            return Coordinate(left)
        return None

    def _neighbor_top_left(self, square):
        tl = square - SHIFT_LETTER + SHIFT_SQUARE
        if tl // SHIFT_LETTER == square // SHIFT_LETTER - 1 and \
           tl >= 0:
            return Coordinate(tl)
        return None

    def neighbor_in_direction(self, square, direction):
        """Returns a Coordinate object or None if the neighbor doesn't exist

        Args:
            square (Coordinate): the square whose neighbor we'll find
            direction (Direction): the direction in which to look for the 
            neighbor
        Returns:
            Coordinate: the coordinate of the neighbor in the given direction, 
            None if no neighbor exists in that direction
        Raises:
            TypeError: if square is not Coordinate or if direction is not 
            Direction

        """
        if not isinstance(square, Coordinate):
            raise TypeError("square variable must be from Coordinate enum")
        if not isinstance(direction, Direction):
            raise TypeError("direction must be from Direction enum")
        if direction == Direction.top:
            return self._neighbor_top(square)
        if direction == Direction.top_right:
            return self._neighbor_top_right(square)
        if direction == Direction.right:
            return self._neighbor_right(square)
        if direction == Direction.btm_right:
            return self._neighbor_btm_right(square)
        if direction == Direction.btm:
            return self._neighbor_btm(square)
        if direction == Direction.btm_left:
            return self._neighbor_btm_left(square)
        if direction == Direction.left:
            return self._neighbor_left(square)
        if direction == Direction.top_left:
            return self._neighbor_top_left(square)

    def neighbors(self, square):
        """Returns a dictionary dict[Direction]=Coordinate.

        Args:
            square (Coordinate): the square to get neighbors from
        Returns:
            dict: keys are Direction values; values are Coordinate elements 
            of the corresponding neighbor, None if neighbor doesn't exist
        Raises:
            TypeError: if square is not of type Coordinate

        """
        if not isinstance(square, Coordinate):
            raise TypeError("square variable must be from Coordinate enum")
        return {Direction.top: self._neighbor_top(square),
                Direction.top_right: self._neighbor_top_right(square),
                Direction.right: self._neighbor_right(square),
                Direction.btm_right: self._neighbor_btm_right(square),
                Direction.btm: self._neighbor_btm(square),
                Direction.btm_left: self._neighbor_btm_left(square),
                Direction.left: self._neighbor_left(square),
                Direction.top_left: self._neighbor_top_left(square)}

    def squares_in_direction(self, origin, direction, 
            include_last_non_empty_square = False):
        """Returns a list with the points from origin to destination.

        Args:
            origin (Coordinate): the square to start from
            direction (Direction): direction to move in
                include_last_non_empty_square (bool): if False, the list will
                include squares up to, but not including the first square where
                content was found. Default value is False
        Returns:
            list: elements are Coordinate elements from origin until the edge
                of the board is reached or a non-empty square is found.
        Raises:
            TypeError: if origin is not of type Coordinate, or if direction 
                is not of type Direction

        """
        if not isinstance(origin, Coordinate):
            raise TypeError("origin variable must be from Coordinate enum")
        if not isinstance(direction, Direction):
            raise TypeError("direction variable must be from Direction enum")
        path = []
        square = self.neighbor_in_direction(origin, direction)
        while square is not None:
            if self.is_empty(square):
                path.append(square)
            else:
                if include_last_non_empty_square:
                    path.append(square)
                break
            square = self.neighbor_in_direction(square, direction)
        return path

    def path_in_direction(self, origin, destination, direction):
        """Returns a list with the points from origin to destination.

        Args:
            origin (Coordinate): the square to start from
            destination (Coordinate): the square to reach
            direction (Direction): direction to move in
        Returns:
            list: elements are Coordinate elements in the path from origin 
                to destination. The list is returned empty if destination is 
                not reached in specified direction from origin
        Raises:
            TypeError: if origin or destination is not of type Coordinate, 
                or if direction is not of type Direction

        """
        if not isinstance(origin, Coordinate):
            raise TypeError("origin variable must be from Coordinate enum")
        if not isinstance(destination, Coordinate):
            raise TypeError("destination variable must be from Coordinate enum")
        if not isinstance(direction, Direction):
            raise TypeError("direction variable must be from Direction enum")
        path = []
        square = self.neighbor_in_direction(origin, direction)
        foundDestination = False
        while square is not None:
            path.append(square)
            square = self.neighbor_in_direction(square, direction)
            if square is destination:
                foundDestination = True
                break
        return path if foundDestination else []

    def set_content(self, square, content):
        """No return value, updates the chosen square with the given content.

        Args:
            square (Coordinate): the square to update
            content: the content to store inside the square
        Raises:
            TypeError: if square is not of type Coordinate

        """
        if not isinstance(square, Coordinate):
            raise TypeError("square variable must be from Coordinate enum")
        self._squares[square] = content

    def get_content(self, square):
        """Returns the content of the square (can be None).

        Args:
            square (Coordinate): the square to check content from
        Returns:
            content: the content previously stored in the square by user
        Raises:
            TypeError: if square is not of type Coordinate

        """
        if not isinstance(square, Coordinate):
            raise TypeError("square variable must be from Coordinate enum")
        return self._squares[square]

    def is_empty(self, square):
        """Returns false if there is content in the square.

        Args:
            square (Coordinate): the square to check
        Returns:
            boolean: true if square is empty
        Raises:
            TypeError: if square is not of type Coordinate

        """
        if not isinstance(square, Coordinate):
            raise TypeError("square variable must be from Coordinate enum")
        return (self._squares[square] is None)

    def clear_square(self, square):
        """No return value. Sets the content of given square to None

        Args:
            square (Coordinate): the square to clear
        Raises:
            TypeError: if square is not of type Coordinate

        """
        if not isinstance(square, Coordinate):
            raise TypeError("square variable must be from Coordinate enum")
        self._squares[square] = None

    def clear_board(self):
        """No return value. Sets the content of all squares to None

        """
        for s in Coordinate:
            self.clear_square(s)

    def move(self, origin, destination):
        """No return value. Moves the content from origin to destination

        Args:
            origin (Coordinate): the square to move from
            destination (Coordinate): the square to move to
        Raises:
            TypeError: if square is not of type Coordinate

        """
        if (not isinstance(origin, Coordinate)) or \
                (not isinstance(destination, Coordinate)):
            raise TypeError("origin and destination must be from Coordinate enum")
        self._squares[destination] = self._squares[origin]
        self._squares[origin] = None
        self._moves.append((origin, destination))
