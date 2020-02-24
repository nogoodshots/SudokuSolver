from .version import __version__
from .solver import Sudoku 

# if somebody does "from sudoku import *", this is what they will be able to access:
__all__ = [
    'Sudoku',
]
