import unittest
from gameboard import Gameboard

# Jason downloaded this gameboard package to create a game of
#   checkers.
class TestCheckers(unittest.TestCase):

    def setUp(self): 
        board = Gameboard()

    def tearDown(self):
        pass
    
    # First, he starts assigning chips as content for certain squares
    def test_content_is_saved_to_square(self):
        pass

# Then, he test moving pieces around

# Finally, he removes pieces when they are "eaten"


# Mark also downloaded this gameboard, but he is going to use it
#   for chess

# He gets all the neighbors of a specific square because
#   those are the legal moves for a king

# He retrieves a diagonal line starting from a square to see
#   the moves available to a bishop

# He then retrieves a straight line for the rook

if __name__ == '__main__':
    unittest.main()