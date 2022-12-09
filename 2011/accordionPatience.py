# round 1 q2 - overall score of 26
# 2a - 24 marks
# 2b - ['2C'], ['KC'], ['3H'], ['KH'], ['4S'], ['KS'], ['2D'], ['KD'], ['4C'], ['2H'], ['7H'], ['5S'] - 2 marks
def createDeck():
    res = []
    cards = ["A"]
    c = [str(i) for i in range(2,10)]
    cards += c
    cards += ["T", "J", "Q", "K"]
    suits = ["C", "H", "S", "D"]
    for suit in suits:
        for c in cards:
            res.append(c + suit)
    return res

class Game:
    def __init__(self, a,b,c,d,e,f):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.e = e
        self.f = f
        self.unDeck = ['AC', '2C', '3C', '4C', '5C', '6C', '7C', '8C', '9C', 'TC', 'JC', 'QC', 'KC', 'AH', '2H', '3H', '4H', '5H', '6H', '7H', '8H', '9H', 'TH', 'JH', 'QH', 'KH', 'AS', '2S', '3S', '4S', '5S', '6S', '7S', '8S', '9S', 'TS', 'JS', 'QS', 'KS', 'AD', '2D', '3D', '4D', '5D', '6D', '7D', '8D', '9D', 'TD', 'JD', 'QD', 'KD']
        self.deck = []

    def shuffleDeck(self):
        current = [self.a, self.b, self.c, self.d, self.e, self.f]
        pointer = 0
        count = 1
        while len(self.unDeck) > 0:
            card = self.unDeck.pop(0)
            if current[pointer] == count:
                self.deck.append([card])
                count = 1
                pointer += 1
                pointer %= len(current)
            else:
                self.unDeck.append(card)
                count += 1
        self.unDeck = ['AC', '2C', '3C', '4C', '5C', '6C', '7C', '8C', '9C', 'TC', 'JC', 'QC', 'KC', 'AH', '2H', '3H', '4H', '5H', '6H', '7H', '8H', '9H', 'TH', 'JH', 'QH', 'KH', 'AS', '2S', '3S', '4S', '5S', '6S', '7S', '8S', '9S', 'TS', 'JS', 'QS', 'KS', 'AD', '2D', '3D', '4D', '5D', '6D', '7D', '8D', '9D', 'TD', 'JD', 'QD', 'KD']
    
    def canMerge(self, card1, card2):
        # if number or suits are the same return true
        return (card1[0] == card2[0]) or (card1[1] == card2[1])

    def getValid(self, customDeck = []):
        # returns the valid moves possible
        # res = [[move this pile, to this pile]...]
        if len(customDeck) > 0:
            res = []
            for i in range(1, len(customDeck)):
                pile = customDeck[i]
                leftPile = customDeck[i-1]
                if self.canMerge(pile[0], leftPile[0]):
                    res.append([i, i-1])
                # can it be moved to a pile 3 to the left
                if i > 2:
                    secondLeftPile = customDeck[i-3]
                    if self.canMerge(pile[0], secondLeftPile[0]):
                        res.append([i, i-3])
            return res
        else:
            res = []
            for i in range(1, len(self.deck)):
                pile = self.deck[i]
                leftPile = self.deck[i-1]
                if self.canMerge(pile[0], leftPile[0]):
                    res.append([i, i-1])
                # can it be moved to a pile 3 to the left
                if i > 2:
                    secondLeftPile = self.deck[i-3]
                    if self.canMerge(pile[0], secondLeftPile[0]):
                        res.append([i, i-3])
            return res
    
    def isOver(self):
        return len(self.getValid()) == 0 or len(self.deck) == 1
    
    def transferPile(self, fro, to):
        # moves pile from index fro to index to 
        interDeck = []
        for i in range(len(self.deck)):
            iiD = []
            for j in range(len(self.deck[i])):
                iiD.append(self.deck[i][j])
            interDeck.append(iiD)
        froData = interDeck[fro]
        toData = interDeck[to]
        interDeck[to] = froData + toData
        interDeck.pop(fro) # this pile will be empty
        return interDeck

    def move(self, strat:int):
        '''
        take pile and put it on top of another pile to its left
        - top cards of the 2 piles have same value or same suit
        - 2 piles are either next to each other or separated by 2 other piles

        strat 1 : - WORKING
        - use right most pile possible - adjacent pile preferred over separated pile
        strat 2 : - WORKING
        - make move that will create largest pile possible
            - multiple of these -> move right most pile psb
        strat 3 : - WORKING
        - make move that will leave the largest num valid moves available next time
            - maximies len(self.getValid())
        '''
        available = self.getValid()

        if strat == 1:
            chosenMove = []
            rightMost1 = available[-1]
            if len(available) > 1:
                rightMost2 = available[-2]
                if rightMost2[0] == rightMost1[0]:
                    # rightMost2 will be the one that swaps with an adjacent because it's added
                    # first to the array in my algorithm
                    chosenMove = rightMost2 
                else:
                    chosenMove = rightMost1
            else: 
                chosenMove = rightMost1
            # perform the move
            self.deck = self.transferPile(chosenMove[0], chosenMove[1])

        elif strat == 2:
            biggest = 0
            chosenMove = []
            chosenMoveIndex = 0
            for i in range(len(available)):
                m = available[i]
                # check how big the piles will become by adding their current sizes
                s = len(self.deck[m[0]]) + len(self.deck[m[1]])
                if s >= biggest:
                    biggest = s
                    chosenMove = m
                    chosenMoveIndex = i

            if len(available) > 1:
                psbAdj = available[chosenMoveIndex-1]
                if psbAdj[0] == chosenMove[0]:
                    chosenMove = psbAdj 
                    chosenMoveIndex -= 1
            
            # perform the move
            self.deck = self.transferPile(chosenMove[0], chosenMove[1])

        elif strat == 3:
            chosenMove = []
            chosenMoveIndex = 0
            bestMovesLeft = 0 
            for i in range(len(available)):
                m = available[i]
                interDeck = self.transferPile(m[0], m[1])
                interMoves = len(self.getValid(interDeck))
                if interMoves >= bestMovesLeft:
                    bestMovesLeft = interMoves
                    chosenMove = m
                    chosenMoveIndex = i

            if len(available) > 1:
                psbAdj = available[chosenMoveIndex-1]
                if psbAdj[0] == chosenMove[0]:
                    chosenMove = psbAdj 
                    chosenMoveIndex -= 1
            
            # perform the move
            self.deck = self.transferPile(chosenMove[0], chosenMove[1])

def main():
    a,b,c,d,e,f = [int(i) for i in input().split(" ")]
    g = Game(a,b,c,d,e,f)
    g.shuffleDeck()
    # print(g.deck[:12])
    print(g.deck[0][0], g.deck[-1][0])
    # strat 1
    while not g.isOver():
        g.move(1)
    print(len(g.deck), g.deck[0][0])
    # reset game
    g.deck = []
    g.shuffleDeck()

    # strat 2
    while not g.isOver():
        g.move(2)
    print(len(g.deck), g.deck[0][0])
    g.deck = []
    g.shuffleDeck()

    # strat 3
    while not g.isOver():
        g.move(3)

    print(len(g.deck), g.deck[0][0])
    g.deck = []
    g.shuffleDeck()

main()
# print(createDeck())