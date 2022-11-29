# BIO round 1 q2 - 
# failed attempt :(
from collections import defaultdict, deque

class Game:
    def __init__(self, size, rows):
        # 1 will store red, 2 will store green, 0 will store empty
        self.size = size
        self.rows = rows
        self.grid = []
        self.redScore = 0
        self.greenScore = 0
        self.squares = {1:[2,1,2,1], 2:[1,2,1,2], 3:[1,1,2,2], 4:[2,1,1,2], 5:[2,2,1,1], 6:[1,2,2,1]}
    
    def generateGrid(self):
        res = []
        # have a sub array for each of the 4 midpoints of the square of a grid
        for i in range(self.size):
            gridRow = []
            for j in range(self.size):
                # structure:
                #   [leftMid, topMid, rightMid, bottomMid]
                gridRow.append([0,0,0,0])
            res.append(gridRow)
        self.grid = res

    def fillGrid(self):
        # fill in the grid
        for i in range(self.size):
            for j in range(self.size):
                self.grid[i][j] = self.squares[self.rows[i][j]]

    def checkTilesAround(self, coor, midIndex, pIndicator):
        # returns coordinate of tile the line can continue through
        # the midPoint of one tile can only ever be connected to 1 other tile
        # pIndicator = player indicator (1 or 2)
        # midIndex = what midpoint on the square are we looking at
        # check tile above
        x,y = coor
        if midIndex == 0:
            # looking to the left
            if y <= 0:
                return 0
            else:
                if self.grid[x][y-1][2] == pIndicator:
                    return [x, y-1]
        if midIndex == 1:
            # looking up
            if x <= 0:
                return 0
            else:
                if self.grid[x-1][y][3] == pIndicator:
                    return [x-1, y]
        if midIndex == 2:
            # looking to the right
            if y >= self.size-1:
                return 0
            else:
                if self.grid[x][y+1][0] == pIndicator:
                    return [x, y+1]
        if midIndex == 3:
            # looking down
            if x >= self.size-1:
                return 0
            else:
                if self.grid[x+1][y][1] == pIndicator: 
                    return [x+1, y]
        return 0

    def stringJoin(self, arr):
        res = ""
        for el in arr: res += str(el)
        return res

    def followTile(self, pIndicator):
        playerScore = 0

        # stores currentCoordinate, number of squares in loop, starting coordinate to check if loop finished
        tiles = deque([])
        visited = defaultdict(lambda:False)

        # get all the squares added with their own coordiante as the starting coordinate
        # to ensure all the squares have been searched
        for i in range(self.size):
            for j in range(self.size):
                tiles.append(([i,j], 1, [i,j]))
            
        # bfs with no visited :0
        while tiles:
            print(tiles)
            coor, count, startingPos = tiles.popleft()
            # print(coor)
            x,y = coor
            currentTile = self.grid[x][y]
            if coor == startingPos and count != 1:
                playerScore += count
            else:
                for i in range(len(currentTile)):
                    mid = currentTile[i]
                    if mid == pIndicator:
                        nextTile = self.checkTilesAround(coor, i, pIndicator)
                        # print(nextTile)
                        if nextTile != 0 and visited[self.stringJoin(nextTile)+self.stringJoin(startingPos)+str(i)]:
                            playerScore += i
                        elif nextTile != 0 and not visited[self.stringJoin(nextTile)+self.stringJoin(startingPos) + str(i)]:
                            # add to queue
                            tiles.append((nextTile, count+1, startingPos))
                            visited[self.stringJoin(nextTile) + self.stringJoin(startingPos) + str(i)] = True
                            tiles.append((nextTile, 1, nextTile))
                            visited[self.stringJoin(nextTile) + self.stringJoin(nextTile) + str(1)] = True
        
        if pIndicator == 1:
            self.redScore = playerScore
        else:
            self.greenScore = playerScore

    def getRedScore(self):
        # 1 represents red line
        self.followTile(1)

    def getGreenScore(self):
        # 2 represents green line
        self.followTile(2)

def main():
    size = int(input())
    rows = []
    for i in range(size):
        row = [int(i) for i in input().split(' ')]
        rows.append(row)
    g = Game(size, rows)
    g.generateGrid()
    g.fillGrid()
    print(g.grid)
    g.getRedScore()
    g.getGreenScore()
    print(g.redScore, g.greenScore)

main()