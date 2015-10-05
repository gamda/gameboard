from enum import Enum
from square import Square
from coordinate import Coordinate

class Direction(Enum):
    top = 1
    topRight = 2
    right = 3
    btmRight = 4
    btm = 5
    btmLeft = 6
    left = 7
    topLeft = 8

class Gameboard:
    rows = [[Coordinate.a8, Coordinate.b8, Coordinate.c8, Coordinate.d8, Coordinate.e8, Coordinate.f8, Coordinate.g8, Coordinate.h8],
            [Coordinate.a7, Coordinate.b7, Coordinate.c7, Coordinate.d7, Coordinate.e7, Coordinate.f7, Coordinate.g7, Coordinate.h7],
            [Coordinate.a6, Coordinate.b6, Coordinate.c6, Coordinate.d6, Coordinate.e6, Coordinate.f6, Coordinate.g6, Coordinate.h6],
            [Coordinate.a5, Coordinate.b5, Coordinate.c5, Coordinate.d5, Coordinate.e5, Coordinate.f5, Coordinate.g5, Coordinate.h5],
            [Coordinate.a4, Coordinate.b4, Coordinate.c4, Coordinate.d4, Coordinate.e4, Coordinate.f4, Coordinate.g4, Coordinate.h4],
            [Coordinate.a3, Coordinate.b3, Coordinate.c3, Coordinate.d3, Coordinate.e3, Coordinate.f3, Coordinate.g3, Coordinate.h3],
            [Coordinate.a2, Coordinate.b2, Coordinate.c2, Coordinate.d2, Coordinate.e2, Coordinate.f2, Coordinate.g2, Coordinate.h2],
            [Coordinate.a1, Coordinate.b1, Coordinate.c1, Coordinate.d1, Coordinate.e1, Coordinate.f1, Coordinate.g1, Coordinate.h1]]
    
    def __init__(self):
        self.squares = {}
        for k in Coordinate:
            self.squares[k] = Square()
        self.graph = self._populateGraph()

    def columnForSquare(self, square):
        """Returns  a list representing the vertical line that corresponds to the square given.

        Args:
            square (Coordinate): the square in the column to find
        Returns:
            list: elements are Coordinate elements in the column, including 'square'
        Raises:
            TypeError: if square is not of type Coordinate
        """
        if not isinstance(square, Coordinate):
            raise TypeError("square variable must be from Coordinate enum")
        # Vertical lines all have the same letter (y-value)
        x, y = self._indexOf(square)
        column = set()
        for row in self.rows:
            column.add(row[y])
        print(column)
        return column

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

    def _populateGraph(self):
        """Creates a dictionary where each key represents a square
        and the value is a list of the squares it is connected to."""
        # graph = {}
        # letter = 8
        # number = 1
        # for k in self.squares.keys():
        #     edges = []
        #     # There's 8 directions, going TRouBLe order
        #     edges.append(k + number)            # top
        #     edges.append(k + number + letter)   # top right
        #     edges.append(k + letter)            # right
        #     edges.append(k + letter - number)   # btm right
        #     edges.append(k - number)            # btm
        #     edges.append(k - letter - number)   # btm left
        #     edges.append(k - letter)            # left
        #     edges.append(k - letter + number)   # top left
        #     # remove out of bounds
        #     edges = [e for e in edges if e > 0 and e <= 64]
        #     graph[k] = edges
        # print(graph)
        # return graph