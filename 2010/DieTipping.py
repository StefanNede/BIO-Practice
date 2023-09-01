# 2010 BIO round 1 q2 - 24/24

class Game:
    def __init__(self, top3, mid3, bot3):
        self.grid = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
                    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
                    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
                    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
                    [1, 1, 1, 1, top3[0], top3[1], top3[2], 1, 1, 1, 1], 
                    [1, 1, 1, 1, mid3[0], mid3[1], mid3[2], 1, 1, 1, 1], 
                    [1, 1, 1, 1, bot3[0], bot3[1], bot3[2], 1, 1, 1, 1], 
                    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
                    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
                    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
                    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

        # die starting config
        self.uppermost = 1
        self.opposite = 6
        self.above = 2
        self.below = 5
        self.left = 3
        self.right = 4

        # headign - holds the direction on the grid the die last moved
        self.heading = 'u' 
        self.headingTranslations = {'u':(-1,0), 'd':(1,0), 'r':(0,1), 'l':(0,-1)}

        # die positions
        self.dieX = 5 # first index
        self.dieY = 5 # second index

    def updatePosition(self):
        # updates the dieX and dieY based on self.heading
        movement = self.headingTranslations[self.heading]
        self.dieX += movement[0]
        self.dieY += movement[1]
        if self.dieX < 0:
            self.dieX = 10
        elif self.dieX > 10:
            self.dieX = 0
        
        if self.dieY < 0:
            self.dieY = 10
        elif self.dieY > 10:
            self.dieY = 0

    def updateUppermost(self):
        # updates uppermost based on self.heading
        if self.heading == 'u':
            self.opposite, self.above, self.uppermost, self.below = self.above, self.uppermost, self.below, self.opposite
        elif self.heading == 'd':
            self.opposite, self.above, self.uppermost, self.below = self.below, self.opposite, self.above, self.uppermost
        elif self.heading == 'r':
            self.opposite, self.right, self.uppermost, self.left = self.right, self.uppermost, self.left, self.opposite
        elif self.heading == 'l':
            self.opposite, self.left, self.uppermost, self.right = self.left, self.uppermost, self.right, self.opposite
        else:
            print("ERROR")

    def performMove(self):
        newValue = self.uppermost + self.grid[self.dieX][self.dieY]
        if newValue > 6: newValue -= 6
        self.grid[self.dieX][self.dieY] = newValue

        if newValue == 2:
            # move 1 square in the direction 90 clockwise to the heading
            if self.heading == 'u': self.heading = 'r'
            elif self.heading == 'd': self.heading = 'l'
            elif self.heading == 'r': self.heading = 'd'
            elif self.heading == 'l': self.heading = 'u'
        elif newValue == 3 or newValue == 4:
            # move 1 square in opposite direction to the heading
            if self.heading == 'u': self.heading = 'd'
            elif self.heading == 'd': self.heading = 'u'
            elif self.heading == 'r': self.heading = 'l'
            elif self.heading == 'l': self.heading = 'r'
        elif newValue == 5:
            # move 1 square in the direction 90 anti clockwise to the heading
            if self.heading == 'u': self.heading = 'l'
            elif self.heading == 'd': self.heading = 'r'
            elif self.heading == 'r': self.heading = 'u'
            elif self.heading == 'l': self.heading = 'd'
        self.updatePosition()
        self.updateUppermost()

    def outputGrid(self):
        for i in range(self.dieX-1, self.dieX+2):
            innerGrid = []
            for j in range(self.dieY-1, self.dieY+2):
                if i < 0 or j < 0 or i > 10 or j > 10:
                    innerGrid.append('x')
                else:
                    innerGrid.append(str(self.grid[i][j]))
            print("".join(innerGrid))

def main():
    top3 = [int(i) for i in input().split(" ")]
    mid3 = [int(i) for i in input().split(" ")]
    bot3 = [int(i) for i in input().split(" ")]
    g = Game(top3,mid3,bot3)

    while True:
        n = int(input())
        if n == 0:
            break
        else:
            # perform n moves
            for i in range(n):
                g.performMove()
            g.outputGrid()

main()