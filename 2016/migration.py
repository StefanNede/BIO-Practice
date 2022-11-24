# BIO round 1 q2 2016

# structure of self.board:
# 2d array
# when go out of bounds of the array up or down add another sub array of length of the others above or below
# when go out of bounds left or right add another value to the left or right of all of the sub arrays
# starting sub array will be "" x ""

class Migration:
    def __init__(self, startPos, sequVals):
        self.position:int = startPos
        self.sequVals:list = sequVals
        self.board = []
    
    def generateInitialBoard(self):
        # looks at sequVals and startPos to generate a board large enough for the initial input
        pass

    def getCoor(self, pos):
        # outputs the indexes need to access a 2d array from self.position
        boardLength = len(self.board)
        subBoardLength = len(self.board[0])
        xCoor = pos
        yCoor = pos
        return [xCoor, yCoor]

    def addArrUp(self):
        subArrayLength = len(self.board[0])
        subArray = [0] * subArrayLength
        self.board = [subArray] + self.board
    
    def addArrDown(self):
        subArrayLength = len(self.board[0])
        subArray = [0] * subArrayLength
        self.board.append(subArray)
    
    def addArrLeft(self):
        for subArray in self.board:
            subArray.insert(0,0)

    def addArrRight(self):
        for subArray in self.board:
            subArray.append(0)
    
    def simulate(self):
        pass

    def outputBoard(self):
        for row in self.board:
            print(" ".join(row))

def main():
    startPos, sequence, n = [int(i) for i in input.split()]
    sequVals = [int(j) for j in input().split(" ")]
    m = Migration(startPos, sequVals)
    m.generateInitialBoard()
    for i in range(n):
        m.simulate()
    m.outputBoard()

main()