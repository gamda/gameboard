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
        self._squares = {}
        for k in Coordinate:
            self._squares[k] = None

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
        number = 1
        letter = 8
        top = None
        tr = None
        right = None
        br = None
        btm = None
        bl = None
        left = None
        tl = None
        try:
            newCoord = square + number
            if (newCoord // letter) == (square // letter):
                top = Coordinate(newCoord)
            else:
                pass # adding a square puts us in the next letter column
        except ValueError:
            pass # index is out of bounds, so neighbor stays None
        try:
            newCoord = square + letter + number
            if (newCoord // letter) == (square // letter + 1):
                tr  = Coordinate(newCoord)
        except ValueError:
            pass
        try:
            right  = Coordinate(square + letter)
        except ValueError:
            pass
        try:
            newCoord = square + letter - number
            if (newCoord // letter) == (square // letter + 1):
                br  = Coordinate(newCoord)
            else:
                pass # We are in the same column
        except ValueError:
            pass
        try:
            newCoord = square - number
            if (newCoord // letter) == (square // letter):
                btm  = Coordinate(newCoord)
        except ValueError:
            pass
        try:
            newCoord = square - letter - number
            if (newCoord // letter) == (square // letter - 1):
                bl  = Coordinate(newCoord)
        except ValueError:
            pass
        try:
            left  = Coordinate(square - letter)
        except ValueError:
            pass
        try:
            newCoord = square - letter + number
            if (newCoord // letter) == (square // letter - 1):
                tl  = Coordinate(newCoord)
        except ValueError:
            pass
        neighbors = {Direction.top: top,
                    Direction.topRight: tr,
                    Direction.right: right,
                    Direction.btmRight: br,
                    Direction.btm: btm,
                    Direction.btmLeft: bl,
                    Direction.left: left,
                    Direction.topLeft: tl}
        return neighbors

    def rowForSquare(self, square):
        """Returns a list representing the horizontal line where the square given belongs.

        Args:
            square (Coordinate): the square in the row to find
        Returns:
            list: elements are Coordinate elements in the row, including 'square'
        Raises:
            TypeError: if square is not of type Coordinate
        """
        if not isinstance(square, Coordinate):
            raise TypeError("square variable must be from Coordinate enum")
        # Horizontal lines all have the same number (x-value)
        x, y = self._indexOf(square)
        return self.rows[x]

    def columnForSquare(self, square):
        """Returns a list representing the vertical line where the square given belongs.

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
        column = []
        for row in self.rows:
            column.append(row[y])
        return column

    def rowAndColumnForSquare(self, square):
        """Returns a list representing the horizontal and vertical lines where the square given belongs.

        Args:
            square (Coordinate): the square in the row to find
        Returns:
            list: elements are Coordinate elements in the row and column, including 'square'
        Raises:
            TypeError: if square is not of type Coordinate
        """
        if not isinstance(square, Coordinate):
            raise TypeError("square variable must be from Coordinate enum")
        row = self.rowForSquare(square)
        col = self.columnForSquare(square)
        row.extend(col)
        return list(set(row)) 
        # ^ turn into set because 'square' is in both lists and a duplicate element after extend()

    def diagonalsForSquare(self, square):
        """Returns a list representing both diagonals where the square given belongs.

        Args:
            square (Coordinate): the square in the diagonals to find
        Returns:
            list: elements are Coordinate elements in the diagonals, including 'square'
        Raises:
            TypeError: if square is not of type Coordinate
        """
        if not isinstance(square, Coordinate):
            raise TypeError("square variable must be from Coordinate enum")
        MAX_INDEX = len(self.rows) - 1
        MIN_INDEX = 0
        
        x, y = self._indexOf(square)
        diagonals = [square]

        # 4 directions: 
        #   top-right:  x decreases, y increases
        rowIndex, colIndex = x, y
        while rowIndex > MIN_INDEX and colIndex < MAX_INDEX:
            rowIndex -= 1
            colIndex += 1
            diagonals.append(self.rows[rowIndex][colIndex])
        #   btm-right:  x increases, y increases
        rowIndex, colIndex = x, y
        while rowIndex < MAX_INDEX and colIndex < MAX_INDEX:
            rowIndex += 1
            colIndex += 1
            diagonals.append(self.rows[rowIndex][colIndex])
        #   btm-left:   x increases, y decreases
        rowIndex, colIndex = x, y
        while rowIndex < MAX_INDEX and colIndex > MIN_INDEX:
            rowIndex += 1
            colIndex -= 1
            diagonals.append(self.rows[rowIndex][colIndex])
        #   top-right:  x decreases, y decreases
        rowIndex, colIndex = x, y
        while rowIndex > MIN_INDEX and colIndex > MIN_INDEX:
            rowIndex -= 1
            colIndex -= 1
            diagonals.append(self.rows[rowIndex][colIndex])
        return diagonals

    def setContent(self, square, content):
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

    def getContent(self, square):
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

    def isEmpty(self, square):
        """Returns a boolean indicating whether the square at the given Coordinate is empty.

        Args:
            square (Coordinate): the square to check
        Returns:
            boolean: true if square is empty
        Raises:
            TypeError: if square is not of type Coordinate

        """
        if not isinstance(square, Coordinate):
            raise TypeError("square variable must be from Coordinate enum")
        return (self._squares[square] == None)

    def clearSquare(self, square):
        """No return value. Sets the content of given square to None

        Args:
            square (Coordinate): the square to clear
        Raises:
            TypeError: if square is not of type Coordinate

        """
        if not isinstance(square, Coordinate):
            raise TypeError("square variable must be from Coordinate enum")
        self._squares[square] = None

    def clearBoard(self):
        """No return value. Sets the content of all squares to None

        """
        for s in Coordinate:
            self.clearSquare(s)

    def move(self, origin, destination):
        """No return value. Moves the content from origin to destination

        Args:
            origin (Coordinate): the square to move from
            destination (Coordinate): the square to move to
        Raises:
            TypeError: if square is not of type Coordinate

        """
        if (not isinstance(origin, Coordinate)) or (not isinstance(destination, Coordinate)):
            raise TypeError("origin and destination must be from Coordinate enum")
        self._squares[destination] = self._squares[origin]
        self._squares[origin] = None
