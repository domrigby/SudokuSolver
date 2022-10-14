from collections import Counter
from typing import Dict , List
from lineOrBox import LineOrBox
from cell import Cell

import numpy as np

class Grid:

    def __init__(self,gridArray):

        self.done = False

        self.gridArray = gridArray

        self.numSqLeft = np.count_nonzero(self.gridArray==0)

    def divide(self,grid):        
        self.occupyRows(grid)
        self.occupyColumns(grid)
        self.occupyBoxes(grid)

    def createCellGrid(self):
        self.cellList: List[Cell] = []
        for i in range(len(self.gridArray)):
            self.cellList.append([])
            for j in range(len(self.gridArray[i])):
                if self.gridArray[i][j] :
                    self.cellList[i].append(Cell(self.gridArray[i][j],[i,j],self.rowDict[i],self.colDict[j],self.boxDict[3*(i//3)+j//3],self))
                else:
                    self.cellList[i].append(Cell(0,[i,j],self.rowDict[i],self.colDict[j],self.boxDict[3*(i//3)+j//3],self))

        self.cellList = np.array(self.cellList)


    def updateGrid(self,pos,val):
        self.gridArray[pos[0],pos[1]] = val
        
        if not 0 in self.gridArray:
            self.done = True
        
        self.numSqLeft = np.count_nonzero(self.gridArray==0)

        print("grid updated")

    def printGrid(self):
        i = 1
        for row in self.gridArray:
            print(f"{row[0:3]}    {row[3:6]}    {row[6:9]}")

            if i%3 == 0:
                print("\n")
            i+=1

    def occupyRows(self,grid):
        self.rowDict: Dict[LineOrBox] =  {}
        j =0
        for row in grid:
            rowObj = LineOrBox(row,j) # the asterix unpacks the list
            self.rowDict[j] = rowObj
            j += 1           
    
    def occupyColumns(self,grid):
        self.colDict: Dict[LineOrBox] = {}
        for i in range(len(grid[0])):
            colObj = LineOrBox(grid[:,i],i) # for ease of input, this is the jth column of the ith column
            self.colDict[i]= colObj

    def occupyBoxes(self,grid):
        self.boxDict: Dict[LineOrBox] = {}
        self.boxArray = np.array([])
        for z in range(len(grid)//3):
            for q in range(len(grid)//3):
                box = grid[3*q:3*(q+1)][:,3*z:3*(z+1)] # it needs to go [0:3], [3:6] then [6:9] when i = 0,1,2
                boxNum = q*3+z
                self.boxDict[boxNum] = LineOrBox(box,boxNum)

    def checkBoxAndRowColInteraction(self):
        self.rowNums = [[0,1,2],[3,4,5],[6,7,8]]
        self.colNums = [[0,3,6],[1,4,7],[2,5,8]]

        for row in self.rowNums:
            if len(np.intersect1d(self.boxDict[row[0]].missingNumbers,self.boxDict[row[1]].missingNumbers,self.boxDict[row[2]].missingNumbers)) > 0:
                print("Possible here")
        
        for col in self.colNums:
            if len(np.intersect1d(self.boxDict[col[0]].missingNumbers,self.boxDict[col[1]].missingNumbers,self.boxDict[col[2]].missingNumbers)) > 0:
                print("possible")
