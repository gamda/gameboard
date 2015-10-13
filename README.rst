Gameboard
=========

Gameboard intended to be used for implementation of chess and checkers.

Copyright (c) 2015 Daniel Garcia

See the file LICENSE.txt for copying permission.

Public methods:

neighborInDirection(square, direction):
    Args:

    *square* (**Coordinate**): the square whose neighbor we'll find
    *direction* (**Direction**): the direction in which to look for the neighbor
    
    Returns:

    *Coordinate*: the coordinate of the neighbor in the given direction, *None*
    if no neighbor exists in that direction
    
    Raises:

    *TypeError*: if *square* is not **Coordinate** or if *direction* is not **Direction**

neighbors(square):
    Args:

    *square* (**Coordinate**): the square to get neighbors from
    
    Returns:

    *Dictionary*: keys are **Direction** values; values are **Coordinate** elements 
    of the corresponding neighbor, *None* if neighbor doesn't exist
    
    Raises:

    *TypeError*: if *square* is not of type **Coordinate**

rowForSquare(square):
    Args:

    *square* (**Coordinate**): the square in the row to find
    
    Returns:

    *list*: elements are **Coordinate** elements in the row, including *square*
    
    Raises:

    *TypeError*: if *square* is not of type **Coordinate**


columnForSquare(square):
    Args:

    *square* (**Coordinate**): the square in the column to find
    
    Returns:

    *list*: elements are **Coordinate** elements in the column, including *square*
    
    Raises:

    *TypeError*: if *square* is not of type **Coordinate**


rowAndColumnForSquare(square):
    Args:

    *square* (**Coordinate**): the square in the row to find
    
    Returns:

    *list*: elements are **Coordinate** elements in the row and column, including *square*
    
    Raises:

    *TypeError*: if *square* is not of type **Coordinate**


diagonalsForSquare(square):
    Args:

    *square* (**Coordinate**): the square in the diagonals to find
    
    Returns:

    *list*: elements are **Coordinate** elements in the diagonals, including *square*
    
    Raises:

    *TypeError*: if *square* is not of type **Coordinate**


pathInDirection(origin, destination, direction):
    Args:

    *origin* (**Coordinate**): the square to start from
    *destination* (**Coordinate**): the square to reach
    *direction* (**Direction**): direction to move in
    
    Returns:

    *list*: elements are **Coordinate** elements in the path from *origin* to *destination*
    the list is returned empty if *destination* is not reached in specified *direction*
    from *origin*
    
    Raises:

    *TypeError*: if *origin* or *destination* is not of type **Coordinate**, or 
    if *direction* is not of type **Direction**


setContent(square, content):
    Args:

    *square* (**Coordinate**): the square to update
    *content*: the content to store inside the square
    
    Raises:

    *TypeError*: if *square* is not of type **Coordinate**


getContent(square):
    Args:

    *square* (**Coordinate**): the square to check content from
    
    Returns:

    *content*: the content previously stored in the square by user
    
    Raises:

    *TypeError*: if *square* is not of type **Coordinate**


isEmpty(square):
    Args:

    *square* (**Coordinate**): the square to check
    
    Returns:

    boolean: **True** if *square* is empty
    
    Raises:

    *TypeError*: if *square* is not of type **Coordinate**


clearSquare(square):
    Args:

    *square* (**Coordinate**): the square to clear
    
    Raises:

    *TypeError*: if *square* is not of type **Coordinate**


clearBoard(self):
    No return value. Sets the content of all squares to *None*


move(origin, destination):
    Args:

    *origin* (**Coordinate**): the square to move from
    *destination* (**Coordinate**): the square to move to
    
    Raises:

    *TypeError*: if *square* is not of type **Coordinate**