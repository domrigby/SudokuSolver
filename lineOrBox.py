import itertools
import numpy as np

class LineOrBox():

    def __init__(self,numbers,ID):
        
        self.numbers = []

        self.ID = ID

        if len(numbers) != 9:
            numbers = list(itertools.chain(*numbers)) # flattens list if it is not flat

        for number in numbers:
            if number != 0 : # 0s are placeholds in this array
                self.numbers.append(number)
        self.numbers.sort()

        self.findMissing()

    def findMissing(self):
        self.missingNumbers = [x for x in range(1,10) if x not in self.numbers] # returns values between 1 and 9 which are not in the box
        self.missingNumbers.sort()

    def addNumber(self,number):
        self.numbers.append(number)
        self.missingNumbers.remove(number)