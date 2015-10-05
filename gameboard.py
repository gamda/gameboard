from enum import Enum
from square import Square

class Gameboard:
    
    def __init__(self):
        self.squares = {}
        for k in Coordinates:
            self.squares[k] = Square()

class Coordinates(Enum):
    A1 = 1
    A2 = 2
    A3 = 3
    A4 = 4
    A5 = 5
    A6 = 6
    A7 = 7
    A8 = 8
    B1 = 9
    B2 = 10
    B3 = 11
    B4 = 12
    B5 = 13
    B6 = 14
    B7 = 15
    B8 = 16
    C1 = 17
    C2 = 18
    C3 = 19
    C4 = 20
    C5 = 21
    C6 = 22
    C7 = 23
    C8 = 24
    D1 = 25
    D2 = 26
    D3 = 27
    D4 = 28
    D5 = 29
    D6 = 30
    D7 = 31
    D8 = 32
    E1 = 33
    E2 = 34
    E3 = 35
    E4 = 36
    E5 = 37
    E6 = 38
    E7 = 39
    E8 = 40
    F1 = 41
    F2 = 42
    F3 = 43
    F4 = 44
    F5 = 45
    F6 = 46
    F7 = 47
    F8 = 48
    G1 = 49
    G2 = 50
    G3 = 51
    G4 = 52
    G5 = 53
    G6 = 54
    G7 = 55
    G8 = 56
    H1 = 57
    H2 = 58
    H3 = 59
    H4 = 60
    H5 = 61
    H6 = 62
    H7 = 63
    H8 = 64