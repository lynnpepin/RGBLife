"""Board.py

Board(int width, int height, int[][] data) is an object representing
the session of an RGB game of life.
"""

from copy import deepcopy
from cells import *

class Board():
    def __init__(self, width, height, data=None):
        self._generation = 0
        self._width = width
        self._height = height

        if not data:
            self._data = [[E]*self._height]*self._width
        else:
            self._data = data

    def _get_neighbour_count(self, x, y, board_data):
        # A list of the eight neighbours of cell x,y
        neighbours = [
            board_data[(x-1)%self._height][(y-1)%self._width],
            board_data[(x-1)%self._height][y],
            board_data[(x-1)%self._height][(y+1)%self._width],
            board_data[x][(y-1)%self._width],
            #board_data[x][y],
            board_data[x][(y+1)%self._width],
            board_data[(x+1)%self._height][(y-1)%self._width],
            board_data[(x+1)%self._height][y],
            board_data[(x+1)%self._height][(y+1)%self._width]
            ]
            
        return classcount(neighbours)


    def iterate_board(self):
        """Performs a single iteration upon the board's data."""
        board_copy = deepcopy(self._data)
        for x, row in enumerate(board_copy):
            for y, cell in enumerate(row):
                counts = self._get_neighbour_count(x,y,board_copy)
                self._data[x][y] = iterate_cell(cell,counts)
        self._generation += 1


    def set_board(self, data):
        """Updates the board's data, resetting width and height based on
        data, and resetting generation to 0.
        """
        self._data = data
        self._width = len(self._data)
        self._height = len(self._data[0])
        self._generation = 0
       

    def clear(self, width=0, height=0):
        """Resets all the cells in the board to empty, and resets
        generation to 0.
        
        If width and height are defined, reset the board to that size.
        """
        if (width == height == 0):
            self._data = [[E]*self._width]*self._height
            self._generation = 0
        else:
            self._data = [[E for ii in range(self.width)] for jj in range(self.height)]


    def generation(self):
        """The amount of time iterate() has been performed."""
        return self._generation


    def data(self):
        """Returns a deepcopy of the data of the board."""
        return deepcopy(self._data)


    def size(self):
        return (self._width, self._height)
