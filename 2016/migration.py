# BIO round 1 q2 - 11/24
# need to do:
# - get central 5x5 board for output
# - fix addArr

class Migration:
    def __init__(self, startPos, sequVals):
        self.position:int = startPos-1 # convert to 0 indexed
        self.sequVals:list = sequVals
        self.currentSequValIndex = 0
        self.firstMove = True
        self.board = [[0, 0, 0, 0, 0] for i in range(5)] # to start have a 5x5 board - as startPos is in range 1 to 25
    
    def getCoor(self, pos):
        # outputs the indexes need to access a 2d array from self.position
        boardLength = len(self.board)
        xCoor = pos//boardLength
        yCoor = pos - xCoor*boardLength
        return [xCoor, yCoor]

    def addArr(self):
        # add above, below, left and right to keep the board a square
        subArrayLength = len(self.board[0])
        subArray = [0] * subArrayLength
        # first add vertical
        self.board = [subArray] + self.board
        self.board.append(subArray)
        # then horizontal
        for subArray in self.board:
            subArray.insert(0,0)
            subArray.append(0)
        
        # update self.position
        positionX, positionY = self.getCoor(self.position)
        positionX += 1
        positionY += 1
        self.position = len(self.board[0])*positionX + positionY
    
    def migrate(self, coor):
        # moves people out of the current square
        # run checks to enlarge grid
        if coor[1]-1 < 0:
            coor[0] += 1
            coor[1] += 1
            self.addArr()
        if coor[1]+1 > len(self.board[0]):
            coor[0] += 1
            coor[1] += 1
            self.addArr()
        if coor[0]-1 < 0:
            coor[0] += 1
            coor[1] += 1
            self.addArr()
        if coor[0]+1 > len(self.board):
            coor[0] += 1
            coor[1] += 1
            self.addArr()

        coordinateLeft = [coor[0], coor[1]-1]
        coordinateRight = [coor[0], coor[1]+1]
        coordinateUp = [coor[0]-1, coor[1]]
        coordinateDown = [coor[0]+1, coor[1]]

        while self.board[coor[0]][coor[1]] >= 4:
            self.board[coordinateLeft[0]][coordinateLeft[1]] += 1
            self.board[coordinateRight[0]][coordinateRight[1]] += 1
            self.board[coordinateUp[0]][coordinateUp[1]] += 1
            self.board[coordinateDown[0]][coordinateDown[1]] += 1
            self.board[coor[0]][coor[1]] -= 4
    
    def getTotalBoardSize(self): return len(self.board)**2

    def simulate(self):
        # simulate next move
        if not self.firstMove:
            self.position += self.sequVals[self.currentSequValIndex]
            self.position %= self.getTotalBoardSize()
        currentX, currentY = self.getCoor(self.position)
        self.board[currentX][currentY] += 1

        # migrate people out
        # could optimise by checking if the squares people migrate will exceed 3 after the migration
        # and hold a flag for that
        while True:
            switched = False # continue until no migrations have happpened - might become an issue later on
            for i in range(len(self.board)):
                for j in range(len(self.board[i])):
                    square = self.board[i][j]
                    if square >= 4:
                        switched = True
                        self.migrate([i, j])
            if not switched: break
        
        if not self.firstMove:
            self.currentSequValIndex += 1
            self.currentSequValIndex %= len(self.sequVals)
        elif self.firstMove:
            self.firstMove = False

    def outputBoard(self):
        # make sure to only output the central 5x5 board
        for row in self.board:
            for number in row:
                print(number, end=" ")
            print()

def main():
    startPos, sequence, n = [int(i) for i in input().split()]
    sequVals = [int(j) for j in input().split(" ")]
    m = Migration(startPos, sequVals)
    for i in range(n):
        m.simulate()
    m.outputBoard()

main()