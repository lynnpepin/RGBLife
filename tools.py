"""tools.py

A number of tools useful for making the board readable by a human.
"""

from cells import *
import Board

def pic_to_board(filename):
    """Convert the file located at filename to a Board() object."""
    raise NotImplementedError

def save_as_image(board, filename):
    """Save the board as an image located at filename."""
    raise NotImplementedError

def board_to_string(board):
    """Return a string representing the board."""
    raise NotImplementedError

