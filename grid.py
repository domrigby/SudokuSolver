
class Grid:

    def __init__(self,gridArray):

        self.done = False

        self.gridArray = gridArray

    def updateGrid(self,pos,val):
        self.gridArray[pos[0],pos[1]] = val
        
        if not 0 in self.gridArray:
            self.done = True

    def printGrid(self):
        i = 1
        for row in self.gridArray:
            print(f"{row[0:3]}    {row[3:6]}    {row[6:9]}")

            if i%3 == 0:
                print("\n")
            i+=1