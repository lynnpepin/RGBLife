"""Board.py

Board(int width, int height, int[][] data) is an object representing
the session of an RGB game of life.
"""

from cells import *

class Board():
    def __init__(self, width, height, data=None):
        self._generation = 0
        self.width = width
        self.height = height

        if not data:
            self.data = [[E for ii in range(self.width)] for jj in range(self.height)]
        else:
            self.data = data
    
    def iterate():
        """Performs a single iteration upon the board's data."""
        raise NotImplementedError

    def set_board(data):
        """Updates the board's data, resetting width and height based on
        data, and resetting generation to 0.
        """
        raise NotImplementedError
        
    def clear():
        """Resets all the cells in the board to empty, and resets
        generation to 0.
        """
        raise NotImplementedError
    
    def generation():
        """The amount of time iterate() has been performed."""
        return generation()
