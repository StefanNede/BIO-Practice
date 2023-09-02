# BIO round 1 q2

class Game:
    def __init__(self, grid, lC, lmC, rmC, rC):
        self.score = 0
        self.lC = lC
        self.lmC = lmC
        self.rmC = rmC
        self.rC = rC
        self.grid = grid
    
    def hasAdjacents(self, i, j):
        # checks to see if any of the adjacents to element at [i][j] are the same
        return False
        
    def updateGrid(self, interGrid):
        # moves elements down and refills the grid
        pass

    def playRound(self):
        # returns False if no blocks to be removed
        interGrid = ['****', '****', '****', '****']
        redFound = 0
        blueFound = 0
        greenFound = 0

        # go through the grid
        # if an element has no adjacents add it to interGrid in its current position
        # if element has adjacents update the found counter for the colour it is and dont add it to interGrid
        # at end call function on interGrid that moves elements down and refills the grid
        for i in range(4):
            for j in range(4):
                if not self.hasAdjacents(i, j):
                    interGrid[i][j] = self.grid[i][j]
                else:
                    if self.grid[i][j] == 'R': redFound += 1
                    if self.grid[i][j] == 'B': blueFound += 1
                    if self.grid[i][j] == 'G': greenFound += 1

        self.updateGrid(interGrid)

        # no more possible moves
        if redFound == 0 and blueFound == 0 and greenFound == 0:
            return False

        redFound = 1 if redFound == 0 else redFound
        blueFound = 1 if blueFound == 0 else blueFound
        greenFound = 1 if greenFound == 0 else greenFound
        self.score += redFound * blueFound * greenFound

        return True
    
    def outputBoard(self):
        for row in self.grid:
            print(row)

def main():
    grid = []
    lC = [] # left column
    lmC = [] # left middle column
    rmC = [] # right middle column
    rC = [] # right column
    for i in range(4):
        row = input()
        grid.append(row)
        lC.append(row[0])
        lmC.append(row[1])
        rmC.append(row[2])
        rC.append(row[3])

    g = Game(grid,lC,lmC,rmC,rC)
    while True:
        n = int(input())
        if n == 0:
            break
        else:
            for i in range(n):
                if not g.playRound():
                    print("GAME OVER")
                    print(g.score)
                    return
        
        g.outputBoard()
        print(g.score)
    
main()