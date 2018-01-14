"""tools.py

A number of tools useful for making the board readable by a human.
"""

from copy import deepcopy
from PIL import Image
from cells import *
from Board import Board

def pic_to_board(filename):
    """Convert the file located at filename to a Board() object."""
    image = Image.open(filename).convert("RGB")
    rgb_data = list(image.getdata())
    width, height = image.size
    image.close()
    
    # convert rgb_data from rgb tuples to cells
    for ii, cell in enumerate(rgb_data):
        rgb_data[ii] = from_rgb(cell)
    
    data = []
    
    for k in range(0,len(rgb_data),width):
        data.append(rgb_data[k:width+k])

    return Board(width, height, data)


def save_as_pic(board, filename):
    """Save the board as an image located at filename."""
    image = Image.new("RGB",board.size())
    rgb_data = []
    for x, row in enumerate(board.data()):
        for y, cell in enumerate(row):
            rgb_data.append(to_rgb(cell))
    image.putdata(rgb_data)
    image.save(filename,"PNG")

def board_to_string(board):
    """Return a string representing the board."""
    data = board.data()
    data_strings = []   # 1D list of strings; e.g. ["RBB","B B"]
    for row in data:
        row_as_strings = []
        for cell in row:
            row_as_strings.append(to_string(cell))
        data_strings.append("".join(row_as_strings))
    return "\n".join(data_strings)
