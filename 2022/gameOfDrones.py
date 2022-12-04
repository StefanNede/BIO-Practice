# BIO round 1 2022 q2 - 11/27
# skirmishes working
# feud not started

class Game:
    def __init__(self, rJump, bJump):
        self.rJump = rJump
        self.bJump = bJump
        self.rCount = 0
        self.bCount = 0
        self.rEdge = [0,0] # starts facing edge 1 on the first hexagon
        self.bEdge = [5, 24] # starts facing edge 6 on the last hexagon
        self.grid = [["" for i in range(6)] for i in range(25)] # hold who is in charge overall
    
    def controlsHexagon(self):
        interRCount = 0
        interBCount = 0
        # gets the score for red and blue by looping over the hexagons and seeing who has more edges
        for hexagon in self.grid:
            if hexagon.count("r") > hexagon.count("b"):
                interRCount += 1
            elif hexagon.count("b") > hexagon.count("r"):
                interBCount += 1
        return [interRCount, interBCount]

    def takeOwnership(self, drone, edge, hexagon):
        '''changes the edge in the current hexagon and any bordering hexagons'''
        # change current hexagon
        interGrid = self.grid
        interGrid[hexagon][edge] = drone

        # change adjacent coordinate
        # handle no adjacent coordinates
        if (hexagon <= 4) and (edge == 0 or edge == 5): return interGrid
        elif (hexagon == 0 or hexagon == 10 or hexagon == 20) and (edge >= 3): return interGrid
        elif (hexagon == 4) and (edge==5 or edge == 0 or edge == 1): return interGrid
        elif (hexagon == 9 or hexagon == 19) and (edge<=2): return interGrid
        elif (hexagon == 5 or hexagon == 15) and edge == 4: return  interGrid
        elif (hexagon == 14 or hexagon == 24) and edge == 1: return interGrid
        elif (hexagon >= 20) and (edge == 2 or edge == 3): return interGrid
        # handle adjacent coordinates
        # adjacent to the right
        elif edge == 1:
            interGrid[hexagon+1][4] = drone
        # adjacent to the left
        elif edge == 4:
            interGrid[hexagon-1][1] = drone
        # adjacent to the top right
        elif edge == 0:
            resHexa = 0
            if (hexagon >= 5 and hexagon <= 9) or (hexagon >= 15 and hexagon <= 19):
                resHexa = hexagon - 4
            else:
                resHexa = hexagon - 5
            interGrid[resHexa][3] = drone
        # adjacent to the top left
        elif edge == 5:
            resHexa = 0
            if (hexagon >= 5 and hexagon <= 9) or (hexagon >= 15 and hexagon <= 19):
                resHexa = hexagon - 5
            else:
                resHexa = hexagon - 6
            interGrid[resHexa][2] = drone
        # adjacent to the bottom right
        elif edge == 2:
            resHexa = 0
            if (hexagon >= 5 and hexagon <= 9) or (hexagon >= 15 and hexagon <= 19):
                resHexa = hexagon + 6
            else:
                resHexa = hexagon + 5
            interGrid[resHexa][5] = drone
        # adjacent to the bottom left
        elif edge == 3:
            resHexa = 0
            if (hexagon >= 5 and hexagon <= 9) or (hexagon >= 15 and hexagon <= 19):
                resHexa = hexagon + 5
            else:
                resHexa = hexagon + 4
            interGrid[resHexa][0] = drone
        return interGrid

    def skirmish(self, drone):
        if drone == "r":
            # take ownership of edge it is facing 
            edge, hexa = self.rEdge
            self.grid = self.takeOwnership(drone, edge, hexa)
            
            # rotate 60 degree clockwise
            edge += 1
            edge %= 6
            # jump r hexagons along hive
            hexa += self.rJump
            hexa %= 25
            self.rEdge = [edge, hexa]
        else:
            # take ownership of edge it is facing 
            edge, hexa = self.bEdge
            self.grid = self.takeOwnership(drone, edge, hexa)
            # rotate 60 degree anticlockwise
            edge -= 1
            edge %= 6
            # jump b hexagons along hive
            hexa += self.bJump
            hexa %= 25
            self.bEdge = [edge, hexa]
    
    def beforeFeud(self):
        # sets stuff up before feuds take place
        self.rCount, self.bCount = self.controlsHexagon()
        
    def feud(self, drone):
        # might need to modify takeOwnership to give an intermittent grid
        # as we are not always going to choose that grid
        '''
        take ownership of preferred un-owned edge
            - the edge that gains them control over the most hexagons
            - if edges give them the same amount of control choose the one that takes away most control from other colony
            - if still undecided - red choose lowest hexagon number, blue highest
            - if still undecided - red choose lowest direction number, blue highest
        '''
        if drone == "r":
            maxControlNum = 0
            maxControlEdge = 0
            maxControlHexagon = 0
            # at most they can gain control over 2 hexagons from one edge
            for i in range(len(self.grid)):
                cHexagon = self.grid[i]
                # check all the adjacent hexagons where an edge could be placed (loop over edges) and if  
                # u place edges there red count is higher than blue count for both hexagons
                # then set maxControlNum to 2 and store edge and hexagon
                # if this gives control over 1 edge and maxControlNum is 0 then set it to that
                # otherwise a smaller number hexagon gave them the same control so this is preferred
                # if no control then see if number of red edges == blue edges meaning they took away from 
                # other drones, and store this only if maxControlNum is 0
                for edge in range(5):
                    pass

        else:
            # same method as for red but instead of only storing if nothing has been stored previously
            # because trying to get lowest hexagon number
            # continue to store even if a smaller hexagon gives the same outcome
            maxControlNum = 0
            maxControlEdge = 0
            maxControlHexagon = 0
            for i in range(len(self.grid)):
                cHexagon = self.grid[i]
                for edge in range(5):
                    pass

def main():
    rJump, bJump = [int(i) for i in input().split(' ')]
    skirmishes, feuds = [int(i) for i in input().split(' ')] 
    g = Game(rJump, bJump)
    for i in range(skirmishes): 
        g.skirmish("r")
        g.skirmish("b")
    g.beforeFeud()
    for j in range(feuds): 
        g.feud("r")
        g.feud("b")
    print(g.rCount)
    print(g.bCount)

main()