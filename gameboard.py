from square import Square
from coordinates import Coordinates

class Gameboard:
    rows = [[Coordinates.a8, Coordinates.b8, Coordinates.c8, Coordinates.d8, Coordinates.e8, Coordinates.f8, Coordinates.g8, Coordinates.h8],
            [Coordinates.a7, Coordinates.b7, Coordinates.c7, Coordinates.d7, Coordinates.e7, Coordinates.f7, Coordinates.g7, Coordinates.h7],
            [Coordinates.a6, Coordinates.b6, Coordinates.c6, Coordinates.d6, Coordinates.e6, Coordinates.f6, Coordinates.g6, Coordinates.h6],
            [Coordinates.a5, Coordinates.b5, Coordinates.c5, Coordinates.d5, Coordinates.e5, Coordinates.f5, Coordinates.g5, Coordinates.h5],
            [Coordinates.a4, Coordinates.b4, Coordinates.c4, Coordinates.d4, Coordinates.e4, Coordinates.f4, Coordinates.g4, Coordinates.h4],
            [Coordinates.a3, Coordinates.b3, Coordinates.c3, Coordinates.d3, Coordinates.e3, Coordinates.f3, Coordinates.g3, Coordinates.h3],
            [Coordinates.a2, Coordinates.b2, Coordinates.c2, Coordinates.d2, Coordinates.e2, Coordinates.f2, Coordinates.g2, Coordinates.h2],
            [Coordinates.a1, Coordinates.b1, Coordinates.c1, Coordinates.d1, Coordinates.e1, Coordinates.f1, Coordinates.g1, Coordinates.h1]]
    
    def __init__(self):
        self.squares = {}
        for k in Coordinates:
            self.squares[k] = Square()
        self.graph = self._populateGraph()

    def columnForSquare(self, square):
        """Returns the vertical line that corresponds to the square
        given. Returns a list of 'coordinates' values."""
        if not isinstance(square, Coordinates):
            raise TypeError("square variable must be from Coordinates enum")
        # Vertical lines all have the same letter

    def _indexOf(self, square):
        if not isinstance(square, Coordinates):
            raise TypeError("square variable must be from Coordinates enum")

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