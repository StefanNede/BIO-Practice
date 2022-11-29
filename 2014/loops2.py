# BIO round 1 q2 - 
from collections import defaultdict, deque
# i overcomplicated it in the previous attempt 

class Game:
    def __init__(self, size, rows):
        self.size = size
        self.rows = rows
        self.redScore = 0
        self.greenScore = 0

    def getRedScore(self):
        # looking to left of current tile:
        #   1 connect to 3, 6
        #   4 connect to 1, 3, 6
        #   5 connect to 1, 3, 6
        #   2,3,6 connect to none
        # looking to right of current tile:
        # 

        pass

    def getGreenScore(self):
        # looking to left of current tile:
        # 
        pass

def main():
    size = int(input())
    rows = []
    for i in range(size):
        row = [int(i) for i in input().split(' ')]
        rows.append(row)
    g = Game(size, rows)
    g.getRedScore()
    g.getGreenScore()
    print(g.redScore, g.greenScore)

main()