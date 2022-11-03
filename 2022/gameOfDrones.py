# BIO round 1 2022 q2

# Expected difficulties:
# - changing who owns an edge depending on what hexagons share that edge
#   e.g. red takes ownershiop of edge 3 of hexagon 19 which was previously owned by blue as that is edge 6 of hexagon 25 
#       - do this sort of cleaning by, when setting an edge, also look at all touching edges

class Game:
    hexagon = ['','','','','','']
    def __init__(self, rJump, bJump):
        self.rJump = rJump
        self.bJump = bJump
        self.rCount = 0
        self.bCount = 0
        self.hexGrid = [[self.hexagon] * 25]

    def changeHexGrid(self, colony:str, controlled:[int]):
        '''
        colony - (r)ed or (b)lue
        controlled - [hexNum, hexEdge]
        General rules for adjacent hex edges:
        x,1 = y,4        
        x,2 = y,5
        x,3 = y,6
        x,4 = y,1
        x,5 = y,2
        x,6 = y,3

        Now to find link between x and y:

        '''
        # do changes here 
        hexNum, hexEdge = controlled
        self.hexGrid[hexNum][hexEdge] = colony
        if hexEdge <= 3:
            self.hexGrid[y][hexEdge+3] = colony
        elif hexEdge >= 4:
            self.hexGrid[y][hexEdge-3] = colony
    
    def skirmish(self):
        '''
        red drone:
        - takes ownership of edge it's facing
        - rotates 60 degrees clockwise 
        - jumps r hexagons along the hive

        blue drone:
        - takes ownership of edge it's facing
        - rotates 60 degrees anti-clockwise 
        - jumps b hexagons along the hive
        '''
        pass

    def feud(self):
        '''
        red then blue:
        - take ownership of preferred un-owned edge
            - the edge that gains them control over the most hexagons
            - if edges give them the same amount of control choose the one that takes away most control from other colony
            - if still undecided - red choose lowest hexagon number, blue highest
            - if still undecided - red choose lowest direction number, blue highest
        '''
        pass

def main():
    rJump, bJump = [int(i) for i in input().split(' ')]
    skirmishes, feuds = [int(i) for i in input().split(' ')] 
    g = Game(rJump, bJump)
    for i in range(skirmishes): g.skirmish()
    for j in range(feuds): g.feud()
    print(g.rCount)
    print(g.bCount)

if __name__ == "__main__":
    main()