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

def to_rgb(cell):
    """Return a tuple representing the color of the cell."""
    return [(255,255,255), (255,0,0), (0,255,0), (0,0,255)][cell + 1]

def from_rgb(RGB):
    """Return the cell corresponding to the given RGB representation"""
    return [(255,255,255), (255,0,0), (0,255,0), (0,0,255)].index(RGB) - 1

def to_string(cell):
    """Return a string representation of the cell."""
    return [" ","R","G","B"][cell + 1]

def prey(cell):
    """Return the type of cell that is prey of the input cell
    
    >>> prey(R) == G
    True
    """
    
    return (cell + 1) % _N


def predator(cell):
    """Return the type of cell that is predator of the input cell
    
    >>> predator(R) == B
    True
    """
    
    return (cell - 1) % _N


def is_friendly(cell,neighbour):
    """Return true if neighbour is friendly to cell
    
    >>> is_friendly(R,G)
    True
    
    >>> is_friendly(R,B)
    False
    
    >>> is_friendly(R,R)
    True 
    """
    
    return (neighbour in (cell, prey(cell)))


def is_like(cell,neighbour):
    """Return true if neighbour is like to cell
    
    >>> is_like(R,R)
    True
    
    >>> is_like(R,G)
    False
    
    >>> is_like(R,B)
    False
    """
    return (cell == neighbour)


def iterate_cell(cell, neighbours):
    # Returns the class a cell becomes based on its neighbours
    
    # Dead cell:
    # TODO: This is not expandable, relies on (R,G,B)=(0,1,2).
    # Too seoteric.

    if (cell == E):
        life = [0,0,0] # red, green, blue
        for neighbour in neighbours:
            # Determine the dominant class surrounding the cell
            if neighbour == R:
                life[0] += 3
                life[1] -= 8
                life[2] += 2
            if neighbour == G:
                life[0] += 2
                life[1] += 3
                life[2] -= 8
            if neighbour == B:
                life[0] -= 8
                life[1] += 2
                life[2] += 3

        if max(life) in range(7,12):
            return life.index(max(life))
        else:
            return E
    
    # Living cell:
    prey_count = 0
    pred_count = 0
    like_count = 0

    for neighbour in neighbours:
        if neighbour == prey(cell):
            prey_count += 1
        if neighbour == predator(cell):
            pred_count += 1
        if is_like(cell,neighbour):
            like_count += 1
        

    if (like_count >= 4): # overpopulation
        return E

    if (like_count + prey_count - pred_count < 2): # encroachment
        if (pred_count + like_count >= 3): # conversion
            return predator(cell)
        else: # stifling
            return E
    
    if (like_count + prey_count < 2):
        # unreachable in 2D
        return E

    return cell # survival
