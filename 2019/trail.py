# 2019 bio round 1 q2 - full marks 
# # first q2 attempted

# didn't realise the grid can change size 
# need to store:
# - grid (with corresponding coordinates for the normal index notation we're gonna use in the program) -> this won't change
# - current coordinates
# - last t coordinates (trail)
# - position facing after last move  - UP, LEFT, RIGHT, DOWN

class Game:
    def __init__(self, trailLength:int):
        self.visitedCoors = [[2,2]] # will store the visited coors and be popped when exceeded trailLength
        self.maxTrailLength = trailLength
        self.x = 2 # starting index position
        self.y = 2 # starting index position
        self.positionFacing = "UP" # starting facing position

    def move(self, direction:str):
        '''
        calls all the functions needed to change the state of the game upon a move
        if the move cannot be fulfilled then returns -1 (telling the main game loop to stop running), and to use the current
        self.x, self.y as the result
        '''
        tried:int = 0 # keep track of how many adjacent boxes we've tried

        # to get the explorer to try the other adjacent squares because they move
        # in a clockwise direction we can just feed the direction as R after the 
        # initial desired direction is tried
        while tried < 4:
            direction = direction if tried == 0 else 'R'
            self.getPositionFacing(direction) # update position facing
            newPos:list = self.getNewPos() 
            # print(direction,self.positionFacing, newPos, self.visitedCoors)
            if self.isTrailSpaceEmpty(newPos):
                # print(direction,self.positionFacing, newPos)
                self.x, self.y = newPos[0], newPos[1] # update x and y index coordinates
                self.changeTrail() # add these new indexes to the trail
                return 0
            tried += 1

        # all the adjacent squares are occupied or move puts us off the map
        return -1

    def getCoordinate(self):
        '''
        take in coding index coordinates (self.x, self.y) and return the corresponding grid coordinate
 
        e.g. 0,0 => -2,2 and 0,1 => -1,2  and so on
        ''' 
        xCoor = self.y - 2
        yCoor = 2 - self.x 
        return xCoor, yCoor 
       
    def getNewPos(self) -> list:
        '''
        change self.positionFacing 
        change self.x and self.y
        '''
        direction = self.positionFacing
        previousPosition = self.visitedCoors[-1]
        newPos = []
        
        if direction == 'UP':
            newPos = [self.x-1, self.y]
        if direction == 'DOWN':
            newPos = [self.x+1, self.y]
        if direction == 'LEFT':
            newPos = [self.x, self.y-1]
        if direction == 'RIGHT':
            newPos = [self.x, self.y+1]

        return newPos
    
    def getPositionFacing(self, direction):
        '''
        direction can be one of F, L, R
        takes in direction and looks at current position and updates position facing to be one of
        UP DOWN LEFT RIGHT 
        '''
        if direction == 'F':
            # the position facing will stay the same
            return 

        if self.positionFacing == "UP":
            if direction == 'R':
                self.positionFacing = "RIGHT"
            if direction == 'L':
                self.positionFacing = "LEFT"
            return

        if self.positionFacing == "LEFT":
            if direction == 'R':
                self.positionFacing = "UP"
            if direction == 'L':
                self.positionFacing = "DOWN"
            return

        if self.positionFacing == "RIGHT":
            if direction == 'R':
                self.positionFacing = "DOWN"
            if direction == 'L':
                self.positionFacing = "UP"
            return

        if self.positionFacing == "DOWN":
            if direction == 'R':
                self.positionFacing = "LEFT"
            if direction == 'L':
                self.positionFacing = "RIGHT"
            return     

    def changeTrail(self):
        '''
        append the trail so that the last move is at the end, and 
        so that if the length of it is over the required length the first element 
        is removed - queue data structure 
        '''
        self.visitedCoors.append([self.x, self.y])
        if len(self.visitedCoors) > self.maxTrailLength:
            removedCoors = self.visitedCoors.pop(0)

    def isTrailSpaceEmpty(self, coor):
        return (coor not in self.visitedCoors)

# main game loop
def main():
    '''
    t - number of moves for trail to dissapear
    i - explorer's instructions
    m - number of moves explorer makes
    '''
    t, i, m = input().split(" ")
    t, m = int(t), int(m)
    game = Game(t)
    for j in range(m):
        directionMoving = i[j % (len(i))]
        res = game.move(directionMoving)
        # print(game.getCoordinate())
        if res == -1:
            break

    xCoor, yCoor = game.getCoordinate()

    print((xCoor, yCoor))

if __name__ == '__main__':
    main()