# BIO round 1 q2
class Game:
    def __init__(self, a, c, m):
        # bottom left corner of board is 0,0 in format x,y
        self.board = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
                      for i in range(10)]  # 10x10 grid
        self.r = 0  # initial value is 0
        self.a = a
        self.c = c
        self.m = m
        self.shipInfo = []

    def convertCoors(self, x, y):
        newX = x
        newY = len(self.board)-y-1
        return [newX, newY]

    def isValid(self, coor):
        x, y = coor
        if self.board[x][y] == 0:
            return False
        return True

    def setShip(self, x, y, shipSize):
        pass

    def place4(self):
        while True:
            # places a 4 ship
            self.r = (self.a * self.r + self.c) % self.m
            self.r = (self.a * self.r + self.c) % self.m
            x = str(self.r)[:-1]  # units digit
            y = str(self.r)[:-2]  # tens digit
            shipSize = 4
            # check if the calculated coordinates are valid
            if self.r % 2 == 0:
                # go horizontally to the right
                x, y = self.convertCoors(x, y)
                for i in range(shipSize):
                    if not isValid([x, y]):
                        break
                    self.setShip(x, y, shipSize)
                    y += 1

            else:
                # go vertically upwards
                pass

    def place3(self):
        # places a 3 ship
        pass

    def place2(self):
        # places a 2 ship
        pass

    def place1(self):
        # places a 1 ship
        pass

    def outputShipInfo(self):
        # outputs the info of the last added ship
        # then reset ship info
        self.shipInfo = []


def main():
    a, c, m = [int(i) for i input().split(' ')]
    g = Game(a, c, m)

    # place ships
    g.place4()
    g.outputShipInfo()
    for i in range(2):
        g.place3()
        g.outputShipInfo()
    for i in range(3):
        g.place2()
        g.outputShipInfo()
    for i in range(4):
        g.place1()
        g.outputShipInfo()


main()
