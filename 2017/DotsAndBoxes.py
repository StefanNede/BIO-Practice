# BIO round 1 q2 2017 - 24/24
# initially forgot to consider that after winning a square the player gets another turn 

class Game:
    def __init__(self, positionX, positionY, modifierX, modifierY, turns):
        self.outputGrid = [['*', '*', '*', '*', '*'], ['*', '*', '*', '*', '*'], ['*', '*', '*', '*', '*'], ['*', '*', '*', '*', '*'], ['*', '*', '*', '*', '*']]
        self.vEdges = [0]*30
        self.hEdges = [0]*30
        self.positionX = positionX-1
        self.positionY = positionY-1
        self.modifierX = modifierX
        self.modifierY = modifierY
        self.turns = turns
        self.xSquares = 0
        self.ySquares = 0
        self.nextTurn = "X"

    def moveX(self):
        self.positionX += self.modifierX
        self.positionX %= 36
        self.nextTurn = "Y"
        while not self.canMakeEdge("X"):
            self.positionX += 1
            self.positionX %= 36
        self.turns -= 1
    
    def moveY(self):
        self.positionY += self.modifierY
        self.positionY %= 36
        self.nextTurn = "X"
        while not self.canMakeEdge("Y"):
            self.positionY += 1
            self.positionY %= 36
        self.turns -= 1
    
    def isAvailable(self, position, direction:str, player:str):
        # returns true if the position at the coordinate given is empty
        # also update coordinate to state that an edge has been drawn between playerCoor and the direction
        # after each edge grid change, call self.squareCreated() to update resGrid, xSquares and ySquares
        if direction == "up":
            if position < 6: return False
            vEdge = position - 6 
            if self.vEdges[vEdge] == 0:
                # update vertical 
                self.vEdges[vEdge] = 1
                # call self.squareCreated()
                self.squareCreated(position, player)
                return True

        elif direction == "down":
            if position > 29: return False
            vEdge = position
            if self.vEdges[vEdge] == 0:
                # update vertical
                self.vEdges[vEdge] = 1
                self.squareCreated(position, player)
                return True

        elif direction == "right":
            if position in [5,11,17,23,29,35]: return False
            hEdge = position - position//6
            if self.hEdges[hEdge] == 0:
                # update horizontal
                self.hEdges[hEdge] = 1
                self.squareCreated(position, player)
                return True

        elif direction == "left":
            if position in [0,6,12,18,24,30]: return False
            hEdge = position - 1 - position//6
            if self.hEdges[hEdge] == 0:
                # update horizontal
                self.hEdges[hEdge] = 1
                self.squareCreated(position, player)
                return True

    def canMakeEdge(self, player:str):
        # returns True if the player can draw an edge from the coordinate it is at
        # Directions tried:
        # X: 0 - up, 1 - right, 2 - down, 3 - left
        # Y: 0 - up, 1 - left, 2 - down, 3 - right
        if player == "X":
            directionsTried = 0 
            directions = ["up", "right", "down", "left"]
            while directionsTried < 4:
                if self.isAvailable(self.positionX,directions[directionsTried], player):
                    return True
                directionsTried += 1
            return False

        if player == "Y":
            directionsTried = 0
            directions = ["up", "left", "down", "right"]
            while directionsTried < 4:
                if self.isAvailable(self.positionY, directions[directionsTried], player):
                    return True
                directionsTried += 1
            return False

    def getSquareAroundGridSpace(self, gridSpace):
        vEdgeLeft = gridSpace + gridSpace//5
        vEdgeRight = vEdgeLeft + 1
        hEdgeTop = gridSpace
        hEdgeBottom = gridSpace + 5
        return self.vEdges[vEdgeLeft] == 1 and self.vEdges[vEdgeRight] == 1 and self.hEdges[hEdgeTop] == 1 and self.hEdges[hEdgeBottom] == 1
    
    def squareCreated(self, position, player):
        # go through the whole grid and any changes must have been made by the passed in player's last move
        indicator = "X"
        if player == "X": indicator = "X"
        elif player == "Y": indicator = "O"

        posLooking = 0
        # go through each grid space
        while posLooking < 25:
            xCoor = posLooking//5
            yCoor = posLooking%5
            if self.outputGrid[xCoor][yCoor] == "*" and self.getSquareAroundGridSpace(posLooking):
                self.outputGrid[xCoor][yCoor] = indicator
                if player == "X":
                    self.nextTurn = "X" # give X another turn
                    self.xSquares += 1
                else:
                    self.nextTurn = "Y" # give Y another turn
                    self.ySquares += 1
            posLooking += 1

    def outputResGrid(self):
        for row in self.outputGrid:
            print(" ".join(row))


def main():
    positionX, modifierX, positionY, modifierY, turns = [int(i) for i in input().split(" ")]
    g = Game(positionX, positionY, modifierX, modifierY, turns)
    while g.turns > 0:
        if g.nextTurn == "X":
            g.moveX()
        else:
            g.moveY()
    g.outputResGrid()
    print(g.xSquares, end=" ")
    print(g.ySquares)

main()