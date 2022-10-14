import time
from numba import jit

import numpy as np
import itertools

from cell import Cell
from lineOrBox import LineOrBox
from grid import Grid

from typing import Dict, List

# would be nice to add an import image

suduku = np.array([[0,0,4,  0,5,0,  0,0,0],
                   [9,0,0,  7,3,4,  6,0,0],
                   [0,0,3,  0,2,1,  0,4,9],

                   [0,3,5,  0,9,0,  4,8,0],
                   [0,9,0,  0,0,0,  0,3,0],
                   [0,7,6,  0,1,0,  9,2,0],

                   [3,1,0,  9,7,0,  2,0,0],
                   [0,0,9,  1,8,2,  0,0,3],
                   [0,0,0,  0,6,0,  1,0,0]])

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
            grid.checkBoxAndRowColInteraction()
        lastCount = grid.numSqLeft

    grid.printGrid()

if __name__ == "__main__":
    main(suduku)