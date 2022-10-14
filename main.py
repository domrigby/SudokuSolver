import time
from numba import jit

import numpy as np
import itertools

from cell import Cell
from lineOrBox import LineOrBox
from grid import Grid

from typing import Dict, List

# would be nice to add an import image

suduku = np.array([[7,0,0,  0,3,6,  0,4,0],
                   [0,4,0,  1,0,0,  0,7,0],
                   [3,0,0,  0,0,0,  1,0,0],

                   [5,3,0,  0,0,0,  0,0,0],
                   [2,0,9,  6,4,0,  0,0,0],
                   [0,6,0,  9,7,0,  0,8,0],

                   [0,2,0,  7,0,4,  0,0,5],
                   [0,0,0,  0,0,8,  0,0,4],
                   [0,5,4,  0,6,9,  0,0,1]])

def main(suduku):

    grid = Grid(suduku)

    grid.printGrid()

    grid.divide(grid.gridArray)

    grid.createCellGrid()

    grid.divide(grid.cellList)
   
    lastCount = 0
    while not grid.done:
        for row in grid.cellList:
            for cell in row:
                if not cell.known:
                    cell.checkFromPotential()
                else:
                    pass
        if lastCount == grid.numSqLeft:
            print("Switching to row, column, box interactions")
            grid.checkBoxAndRowColInteraction()
        lastCount = grid.numSqLeft

    grid.printGrid()

if __name__ == "__main__":
    main(suduku)