import itertools
import numpy as np

class LineOrBox():

    def __init__(self,cellList,ID):
        
        self.numbers = []
        self.cellList = cellList

        self.ID = ID

        cellList = np.array(cellList)

        cellList = cellList.flatten()

        for cell in cellList:
            if isinstance(cell,np.int64):
                self.numbers.append(cell)
            elif cell.val: # filters out 0 values
                self.numbers.append(cell.val)

        self.numbers.sort()

        self.findMissing()

    def findMissing(self):
        self.missingNumbers = [x for x in range(1,10) if x not in self.numbers] # returns values between 1 and 9 which are not in the box
        self.missingNumbers.sort()

    def addNumber(self,number):
        self.numbers.append(number)
        self.missingNumbers.remove(number)

    def checkCells(self):
        for cell in self.cellList:
            if cell.val and cell.val not in cell.numbers:
                self.numbers.append(cell.val)
                self.missingNumbers.remove(cell.val)