class Cell():

    def __init__(self,val,pos,row,column,box,grid):

        self.pos = pos
        self.rowNum = pos[0]
        self.colNum = pos[1]

        if val:
            self.known = True
            self.val = val
        else:
            self.val = 0
            self.known = False
            self.row = row
            self.column = column
            self.box = box
            self.grid = grid
        

        if not self.known:
            self.checkFromPotential()

    def checkFromPotential(self):
        self.potentialNumbers = []
        for number in self.row.missingNumbers:
            if number in self.column.missingNumbers and number in self.box.missingNumbers:
                    self.potentialNumbers.append(number)
        
        if len(self.potentialNumbers) == 1:

            self.found(self.potentialNumbers[0])


    def found(self,num):
        self.val = num
        self.known == True
        print(self.val)

        # update row and column objects
        self.row.addNumber(self.val)
        self.column.addNumber(self.val)
        self.box.addNumber(self.val)

        self.grid.updateGrid(self.pos,self.val)

