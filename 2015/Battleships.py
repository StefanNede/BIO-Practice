# BIO round 1 q2 - 27/27
# q2b - 3,0 4,0 7,0 8,0 - 2/2
class Game:
    def __init__(self, a, c, m):
        # bottom left corner of board is 0,0 in format x,y
        self.board = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
                      for i in range(10)]  # 10x10 grid
        self.a = a
        self.c = c
        self.m = m
        self.r = 0  # initial value is 0
        self.shipInfo = []

    def convertCoors(self, x, y):
        newX = len(self.board)-y-1
        newY = x
        return [newX, newY]
    
    def checkCoor(self, x, y, diagonal = False):
        # returns true if coordinate is occupied
        if not diagonal: 
            try:
                if self.board[x][y] != 0: return True

            except: return True 
            return False
        else:
            # if it goes out of bounds we don't want to return True
            try:
                if self.board[x][y] != 0: return True
            except: return False
            return False
    
    def areTouching(self, coor):
        # returns true if the coordinate is touching another ship 
        x, y = coor
        # CHECK DIAGONALS
        # check top right 
        if self.checkCoor(x-1, y+1, True): return True

        # check top left
        elif self.checkCoor(x-1, y-1, True): return True

        # check bottom right
        elif self.checkCoor(x+1, y+1, True): return True

        # check bottom left
        elif self.checkCoor(x+1, y-1, True): return True

        # CHECK HORIZONTAL + VERTICALLY
        elif self.checkCoor(x, y+1, True) or self.checkCoor(x, y-1, True) or self.checkCoor(x-1, y, True) or self.checkCoor(x+1, y, True): return True

        else: return False

    def isValid(self, coordinatesToPlace):
        for coor in coordinatesToPlace:
            x, y = coor
            if self.checkCoor(x, y):
                return False
            elif self.areTouching(coor): return False
        return True

    def setShip(self, coordinatesToPlace):
        for coor in coordinatesToPlace:
            x, y = coor
            self.board[x][y] = 1

    def placeShip(self, size):
        while True:
            # places a 4 ship
            self.r = ((self.a * self.r) + self.c) % self.m
            initialR = self.r
            x = int(str(initialR)[-1])  # units digit
            if len(str(initialR)) <= 1:
                y = 0
            else:
                y = int(str(initialR)[-2])  # tens digit
            self.r = ((self.a * self.r) + self.c) % self.m
            placeR = self.r
            # print(initialR, placeR, [x,y])
            shipSize = size
            # check if the calculated coordinates are valid
            if placeR % 2 == 0:
                # go horizontally to the right
                originalCoordinates = [x,y]
                x, y = self.convertCoors(x, y)
                coordinatesToPlace = [[x,y]]
                orientation = "H"
                for i in range(shipSize-1):
                    y += 1
                    coordinatesToPlace.append([x,y])
                if self.isValid(coordinatesToPlace):
                    # set the ship info
                    xStart, yStart = originalCoordinates
                    self.shipInfo = [xStart, yStart, orientation]
                    self.setShip(coordinatesToPlace)
                    break

            else:
                # go vertically upwards
                originalCoordinates = [x,y]
                x, y = self.convertCoors(x, y)
                coordinatesToPlace = [[x,y]]
                orientation = "V"
                for i in range(shipSize-1):
                    x -= 1
                    coordinatesToPlace.append([x,y])
                if self.isValid(coordinatesToPlace):
                    # set the ship info
                    xStart, yStart = originalCoordinates
                    self.shipInfo = [xStart, yStart, orientation]
                    self.setShip(coordinatesToPlace)
                    break

    def outputShipInfo(self):
        # outputs the info of the last added ship
        for inf in self.shipInfo:
            print(str(inf), end = " ")
        print()
        # then reset ship info
        self.shipInfo = []


def main():
    a, c, m = [int(i) for i in input().split(' ')]
    g = Game(a,c,m)
    g.placeShip(4)
    g.outputShipInfo()
    for i in range(2):
        g.placeShip(3)
        g.outputShipInfo()
    for i in range(3):
        g.placeShip(2)
        g.outputShipInfo()
    for i in range(4):
        g.placeShip(1)
        g.outputShipInfo()

main()