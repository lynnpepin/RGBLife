"""cells.py

Contains the names for different classes of cells, as well as functions
defining the relationships between these different classes of cells.

The implementation of the functions in this module rely on the ordering
of the cells. That is, (R,G,B) -> (0, 1, 2)
"""

# The types of cells
E = -1  # Dead cell
R = 0   # R, G, B are live cells
G = 1
B = 2 

_N = 3  # 



def prey(cell):
    """Return the type of cell that is prey of the input cell
    
    >>> prey(R) == G
    True
    """
    
    raise NotImplementedError


def predator(cell):
    """Return the type of cell that is predator of the input cell
    
    >>> predator(R) == B
    True
    """
    
    raise NotImplementedError


def is_friendly(cell,neighbour):
    """Return true if neighbour is friendly to cell
    
    >>> is_friendly(R,G)
    True
    
    >>> is_friendly(R,B)
    False
    
    >>> is_friendly(R,R)
    True 
    """
    
    raise NotImplementedError


def is_like(cell,neighbour):
    """Return true if neighbour is like to cell
    
    >>> is_like(R,R)
    True
    
    >>> is_like(R,G)
    False
    
    >>> is_like(R,B)
    False
    """
    
    raise NotImplementedError
