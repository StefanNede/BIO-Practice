# BIO round 1 q2 - 24/24

class Migration:
    def __init__(self, startPos, sequVals):
        self.position:int = startPos-1 # convert to 0 indexed
        self.sequVals:list = sequVals
        self.currentSequValIndex = 0
        self.firstMove = True
        self.board = [[0, 0, 0, 0, 0] for i in range(5)] # to start have a 5x5 board - as startPos is in range 1 to 25
    
    def getCoor(self, pos):
        # gets the coordinate within a 5x5 grid
        # outputs the indexes need to access a 2d array from self.position
        xCoor = pos//5
        yCoor = pos - xCoor*5
        return [xCoor, yCoor]

    def addArr(self):
        # add above, below, left and right to keep the board a square
        subArrayLength = len(self.board[0])
        subArray = [0]*subArrayLength
        # first add vertical
        self.board = [subArray] + self.board
        self.board.append(subArray)
        # then horizontal
        for i in range(len(self.board)):
            sub = [0] + self.board[i] + [0]
            self.board[i] = sub
        
    def migrate(self, coor):
        # moves people out of the current square
        # run checks to enlarge grid
        if coor[1]-1 < 0:
            coor[0] += 1
            coor[1] += 1
            self.addArr()
        if coor[1]+1 >= len(self.board[0]):
            coor[0] += 1
            coor[1] += 1
            self.addArr()
        if coor[0]-1 < 0:
            coor[0] += 1
            coor[1] += 1
            self.addArr()
        if coor[0]+1 >= len(self.board):
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
            self.position %= 25
        # moves will only be within the 5x5 grid so we need to do this
        currentX, currentY = self.getCoor(self.position)
        self.board[(len(self.board)-5)//2 + currentX][(len(self.board)-5)//2 + currentY] += 1

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
        outputBoard = []
        for i in range((len(self.board)-5)//2, len(self.board) - (len(self.board)-5)//2):
            b = self.board[i]
            outputBoard.append(b[(len(self.board)-5)//2: len(self.board) - (len(self.board)-5)//2])
        
        for row in outputBoard:
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