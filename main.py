import numpy as np
import itertools

from cell import Cell
from lineOrBox import LineOrBox
from grid import Grid

from typing import Dict, List

boxSize = 3

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

    rowDict: Dict[LineOrBox] =  {}
    j =0
    for row in suduku:
        rowObj = LineOrBox(row,j) # the asterix unpacks the list
        rowDict[j] = rowObj
        j += 1

    colDict: Dict[LineOrBox] = {}
    for i in range(len(grid.gridArray[0])):
        colObj = LineOrBox(grid.gridArray[:,i],i) # for ease of input, this is the jth column of the ith column
        colDict[i]= colObj

    boxDict: Dict[LineOrBox] = {}
    for z in range(len(grid.gridArray)//boxSize):
        for q in range(len(grid.gridArray)//boxSize):
            box = grid.gridArray[3*q:3*(q+1)][:,3*z:3*(z+1)] # it needs to go [0:3], [3:6] then [6:9] when i = 0,1,2
            boxNum = q*3+z
            boxDict[boxNum] = LineOrBox(box,boxNum)

    cellList: List[Cell] = []
    for i in range(len(grid.gridArray)):
        cellList.append([])
        for j in range(len(grid.gridArray[i])):
            if grid.gridArray[i][j] :
                cellList[i].append(Cell(grid.gridArray[i][j],[i,j],rowDict[i],colDict[j],boxDict[3*(i//3)+j//3],grid))
            else:
                cellList[i].append(Cell(0,[i,j],rowDict[i],colDict[j],boxDict[3*(i//3)+j//3],grid))

    while not grid.done:
        for row in cellList:
            for cell in row:
                if not cell.known:
                    cell.checkFromPotential()
                else:
                    pass
    grid.printGrid()



if __name__ == "__main__":
    main(suduku)