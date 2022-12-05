# BIO round 1 2022 q2 - 27/27

class Game:
    def __init__(self, rJump, bJump):
        self.rJump = rJump
        self.bJump = bJump
        self.rCount = 0
        self.bCount = 0
        self.rEdge = [0,0] # starts facing edge 1 on the first hexagon
        self.bEdge = [5, 24] # starts facing edge 6 on the last hexagon
        self.grid = [["" for i in range(6)] for i in range(25)] # hold who is in charge overall
    
    def controlsHexagon(self, interGrid):
        interRCount = 0
        interBCount = 0
        # gets the score for red and blue by looping over the hexagons and seeing who has more edges
        for hexagon in interGrid:
            if hexagon.count("r") > hexagon.count("b"):
                interRCount += 1
            elif hexagon.count("b") > hexagon.count("r"):
                interBCount += 1
        return [interRCount, interBCount]

    def takeOwnership(self, drone, edge, hexagon):
        '''changes the edge in the current hexagon and any bordering hexagons'''
        # change current hexagon
        interGrid = []
        # if i just write interGrid = self.grid when changing interGrid self.grid is also changed
        for hexa in range(len(self.grid)):
            smaller = []
            for ed in range(6):
                smaller.append(self.grid[hexa][ed])
            interGrid.append(smaller)
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
        self.rCount, self.bCount = self.controlsHexagon(self.grid)

    def feud(self, drone):
        # print(self.grid)
        '''
        take ownership of preferred un-owned edge
            - the edge that gains them control over the most hexagons
            - if edges give them the same amount of control choose the one that takes away most control from other colony
            - if still undecided - red choose lowest hexagon number, blue highest
            - if still undecided - red choose lowest direction number, blue highest
        '''
        if drone == "r":
            # stores stuff to do with gaining stuff for this drone
            maxControlNum = -1 # so that when hexagon 0 and edge 0 is not valid it gets overriden
            maxControlEdge = 0
            maxControlHexagon = 0

            # stores stuff to do with taking away from other drone
            maxRemovedNum = 0
            maxRemovedEdge = 0
            maxRemovedHexagon = 0

            for i in range(len(self.grid)):
                cHexagon = i
                for edge in range(6):
                    # can't override a blue edge and can't retake an edge
                    if self.grid[cHexagon][edge] != "b" and self.grid[cHexagon][edge] != "r":
                        interGrid = self.takeOwnership("r", edge, cHexagon)
                        interRCount, interBCount = self.controlsHexagon(interGrid)

                        # check the differences between the inter r and b counts with the actual self. r and b counts
                        if interRCount - self.rCount > maxControlNum:
                            maxControlNum = interRCount-self.rCount
                            maxControlEdge = edge
                            maxControlHexagon = cHexagon

                            # to allow for comparisons later on if something else gives the same amount of control
                            maxRemovedNum = abs(interBCount - self.bCount)
                            maxRemovedEdge = edge
                            maxRemovedHexagon = cHexagon
                        elif interRCount - self.rCount == maxControlNum:
                            if abs(interBCount - self.bCount) > maxRemovedNum:
                                maxControlNum = interRCount-self.rCount
                                maxControlEdge = edge
                                maxControlHexagon = cHexagon

                                maxRemovedNum = abs(interBCount - self.bCount)
                                maxRemovedEdge = edge
                                maxRemovedHexagon = cHexagon

            # print("RED")
            # print(maxControlNum, maxControlHexagon, maxControlEdge)
            # go through preferences in order
            interGrid = self.takeOwnership("r", maxControlEdge, maxControlHexagon)
            self.grid = interGrid
            interRCount, interBCount = self.controlsHexagon(self.grid)
            self.rCount, self.bCount = interRCount, interBCount

        else:
            # stores stuff to do with gaining stuff for this drone
            maxControlNum = -1
            maxControlEdge = 0
            maxControlHexagon = 0

            # stores stuff to do with taking away from other drone
            maxRemovedNum = 0
            maxRemovedEdge = 0
            maxRemovedHexagon = 0

            # DIFFERENCE - continue to store even if a smaller hexagon gives the same outcome
            for i in range(len(self.grid)):
                cHexagon = i
                for edge in range(6):
                    if self.grid[cHexagon][edge] != "r" and self.grid[cHexagon][edge] != "b":
                        interGrid = self.takeOwnership("b", edge, cHexagon)
                        interRCount, interBCount = self.controlsHexagon(interGrid)
                        # check the differences between the inter r and b counts with the actual self. r and b counts
                        if interBCount - self.bCount > maxControlNum:
                            maxControlNum = interBCount-self.bCount
                            maxControlEdge = edge
                            maxControlHexagon = cHexagon

                            maxRemovedNum = abs(interRCount - self.rCount)
                            maxRemovedEdge = edge
                            maxRemovedHexagon = cHexagon

                        elif interBCount - self.bCount == maxControlNum:
                            if abs(interRCount - self.rCount) >= maxRemovedNum:
                                maxControlNum = interBCount-self.bCount
                                maxControlEdge = edge
                                maxControlHexagon = cHexagon

                                maxRemovedNum = abs(interRCount - self.rCount)
                                maxRemovedEdge = edge
                                maxRemovedHexagon = cHexagon

            # print("BLUE")
            # print(maxControlNum, maxControlHexagon, maxControlEdge)
            # go through preferences in order
            interGrid = self.takeOwnership("b", maxControlEdge, maxControlHexagon)
            self.grid = interGrid
            interRCount, interBCount = self.controlsHexagon(self.grid)
            self.rCount, self.bCount = interRCount, interBCount

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