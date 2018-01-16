"""cells.py

Contains the names for different classes of cells, as well as functions
defining the relationships between these different classes of cells.

Defines:
    E  = -1
    R  = 0
    G  = 1
    B  = 2
    _N = 3

Functions:
    to_rgb(int cell)                        returns (int, int, int) rgb
    from_rgb((int, int, int) RGB)           returns int cell
    to_string(int cell)                     returns string cell
    
    prey(int cell)                          returns int cell
    predator(int cell)                      returns int cell
    is_friendly(int c1, int c2)             returns bool friendly
    is_like(int c1, int c2)                 returns bool like
    
    classcount(int[] neighbours)            returns [int, int, int] classcount
    
    iterate_cell(int cell, int[] counts)    returns int cell
    
"""

# The types of cells
E = -1  # Dead cell
R = 0   # R, G, B are live cells
G = 1
B = 2 

_N = 3  # Number of unique classes of cells.


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
    """Return the type of cell that is prey of the input cell"""
    return (cell + 1) % _N

def predator(cell):
    """Return the type of cell that is predator of the input cell"""
    return (cell - 1) % _N

def is_friendly(cell,neighbour):
    """Return true if neighbour is friendly to cell"""
    return (neighbour in (cell, prey(cell)))

def is_like(cell,neighbour):
    """Return true if neighbour is like to cell"""
    return (cell == neighbour)

def classcount(neighbours):
    """Count each cell in the list neighbours and return a list.
    
    >>>classcount([R,R,R,G,B,R,G,E])
    [4,2,1]
    
    No longer utilized as part of a performance enhancment
    """
    counts = [0]*_N
    for cell in neighbours:
        if(cell >= 0):
            counts[cell] += 1
    return counts

def iterate_cell(cell, counts):
    # Returns the class a cell becomes based on its neighbour counts
    
    # Dead cell:
    #  Warning: This implementation requires _N == 3
    if (cell == E):
        unique_classes = _N - counts.count(0)
        # the unique classes of neighbours present

        if ((unique_classes == 1) and (3 in counts)): # reproduction
            return counts.index(3)
        elif (unique_classes == 2):
            # Expansion is possible
            # First, find the predatory and prey classes
            missing_class = counts.index(0)
            pred_class = prey(missing_class)
            prey_class = prey(pred_class)
            # No over/underpopulation
            if(1 <= counts[pred_class] <= 3):
                # Need at least three friendly neighbours
                if (counts[pred_class] + counts[prey_class] >= 3):
                    return pred_class
        return E 

    # Living cell:
    prey_count = counts[prey(cell)]
    pred_count = counts[predator(cell)]
    like_count = counts[cell]

    if (like_count >= 4): # overpopulation
        return E

    elif (pred_count >= prey_count + like_count + 1): # encroachment
        if (pred_count >= prey_count + like_count + 2): # conversion
            return predator(cell)
        else: # stifling
            return E
    
    elif (like_count + prey_count < 2):   # starvation
        return E
    
    return cell # survival
