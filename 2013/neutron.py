# bio round 1 q2 - 26/26
class Game:
    def __init__(self, firstOrder, secondOrder):
        # first player = "xw", second player = "xb", neutron = "n"
        self.board = [["" for i in range(5)] for i in range(5)]
        self.board[0] = ["1b","2b","3b","4b","5b"]
        self.board[2][2] = "n"
        self.board[4] = ["1w","2w","3w","4w","5w"]
        
        self.firstOrder = firstOrder
        self.firstPointer = 0
        self.secondOrder = secondOrder
        self.secondPointer = 0
        
        self.neutron = [2,2] # holds position of neutron
    
    def isFinished(self, customBoard=[]):
        if len(customBoard) == 0:
            if self.neutron[0] == 0 or self.neutron[0] == 4:
                return True
        else:
            if "n" in customBoard[0] or "n" in customBoard[4]:
                return True
        return False
    
    def getCopyOfBoard(self):
        res = []
        for i in range(5):
            inter = []
            for j in range(5):
                inter.append(self.board[i][j])
            res.append(inter)
        return res
        
    def movePiece(self, pieceCoor, direction, marker):
        # returns resulting board if piece moved like that
        tempBoard = self.getCopyOfBoard()
        oX, oY = pieceCoor
        x, y = pieceCoor
        
        # move until you can't no more
        if direction == 1:
            while self.containsMarker(x, y, tempBoard, "") or self.containsMarker(x,y, tempBoard, marker):
                x -= 1
            x += 1
            
        elif direction == 2:
            while self.containsMarker(x, y, tempBoard, "") or self.containsMarker(x,y, tempBoard, marker):
                x -= 1
                y += 1
            x += 1
            y -= 1
                
        elif direction == 3:
            while self.containsMarker(x, y, tempBoard, "") or self.containsMarker(x,y, tempBoard, marker):
                y += 1
            y -= 1
                
        elif direction == 4:
            while self.containsMarker(x, y, tempBoard, "") or self.containsMarker(x,y, tempBoard, marker):
                x += 1
                y += 1
            x -= 1
            y -= 1
                
        elif direction == 5:
            while self.containsMarker(x, y, tempBoard, "") or self.containsMarker(x,y, tempBoard, marker):
                x += 1
            x -= 1
                
        elif direction == 6:
            while self.containsMarker(x, y, tempBoard, "") or self.containsMarker(x,y, tempBoard, marker):
                x += 1
                y -= 1
            x -= 1
            y += 1
                
        elif direction == 7:
            while self.containsMarker(x, y, tempBoard, "") or self.containsMarker(x,y, tempBoard, marker):
                y -= 1
            y += 1
                
        elif direction == 8:
            while self.containsMarker(x, y, tempBoard, "") or self.containsMarker(x,y, tempBoard, marker):
                x -= 1
                y -= 1
            x += 1
            y += 1
                
        
        # perform the swap
        tempBoard[oX][oY] = ""
        tempBoard[x][y] = marker
        
        return tempBoard
    
    def containsMarker(self, x, y, board, marker):
        if x < 0 or x > 4 or y < 0 or y > 4:
            return False
        elif board[x][y] == marker:
            return True
        return False
    
    def getPosDirections(self, pieceCoor, board):
        # returns a list of the directions a piece can move in
        res = []
        x,y = pieceCoor
        if self.containsMarker(x-1, y, board, ""): res.append(1)
        if self.containsMarker(x-1, y+1, board, ""): res.append(2)
        if self.containsMarker(x, y+1, board, ""): res.append(3)
        if self.containsMarker(x+1, y+1, board, ""): res.append(4)
        if self.containsMarker(x+1, y, board, ""): res.append(5)
        if self.containsMarker(x+1, y-1, board, ""): res.append(6)
        if self.containsMarker(x, y-1, board, ""): res.append(7)
        if self.containsMarker(x-1, y-1, board, ""): res.append(8)
        return res
    
    def winsPlayer(self, player, board):
        if "n" in board[4] and player == 1:
            return True
        elif "n" in board[0] and player == 2:
            return True
        else:
            return False
    
    def play(self, player:int):
        # return -1 if the game is over
        otherPlayer = 1 if player == 2 else 2
        
        neutronMoves = self.getPosDirections(self.neutron, self.board)
        
        # see if can move neutron and win the game
        for nDir in neutronMoves:
            tempBoard = self.movePiece(self.neutron, nDir, "n")
            if self.winsPlayer(player, tempBoard) and self.isFinished(tempBoard):
                self.board = tempBoard
                return -1
               
        # see if other player wins the game for all the possible moves of the neutron
        alwaysWin = True
        for nDir in neutronMoves:
            tempBoard = self.movePiece(self.neutron, nDir, "n")
            if not (self.winsPlayer(otherPlayer, tempBoard) and self.isFinished(tempBoard)):
                alwaysWin = False
        if alwaysWin:
            for nDir in neutronMoves:
                tempBoard = self.movePiece(self.neutron, nDir, "n")
                if self.winsPlayer(otherPlayer, tempBoard) and self.isFinished(tempBoard):
                    self.board = tempBoard
                    return -1
            
        if player == 1:
            # handle movement of white pieces
            pieceCoor = []
            currentPiece = self.firstOrder[self.firstPointer]
            currentPieceMarker = str(currentPiece) + "w"
            
            # get piece coordinate
            for i in range(5):
                for j in range(5):
                    el = self.board[i][j]
                    if el == currentPieceMarker:
                        pieceCoor = [i,j]
                        break
            
            self.firstPointer += 1
            self.firstPointer %= 5
        
        else:
            # handle movement of black pieces
            # handle movement of white pieces
            pieceCoor = []
            currentPiece = self.secondOrder[self.secondPointer]
            currentPieceMarker = str(currentPiece) + "b"
            
            self.secondPointer += 1
            self.secondPointer %= 5
        
            # get piece coordinate
            for i in range(5):
                for j in range(5):
                    el = self.board[i][j]
                    if el == currentPieceMarker:
                        pieceCoor = [i,j]
                        break
            
        # print(pieceCoor, currentPieceMarker)
        possibleDirections = []
        
        found = False
        # print(neutronMoves)
        # move the neutron in a direction such that it doesn't obstruct the current piece moving
        for nDir in neutronMoves:
            tempBoard = self.movePiece(self.neutron, nDir, "n")
            if not self.isFinished(tempBoard): 
                possibleMoves = self.getPosDirections(pieceCoor, tempBoard)
                if len(possibleMoves) > 0:
                    self.board = tempBoard
                    # print(nDir)
                    
                    # update coordinate of neutron
                    self.neutron = []
                    for i in range(5):
                        for j in range(5):
                            if self.board[i][j] == "n":
                                self.neutron = [i,j]
                    
                    found = True
                    possibleDirections = possibleMoves
                    break
        
        # no way to move the neutron without preventing the desired piece from moving
        if not found: return -1
        
        self.board = self.movePiece(pieceCoor, possibleDirections[0], currentPieceMarker)
        
    
    def outputBoard(self):
        for row in self.board:
            sub = []
            for piece in row:
                if "b" in piece:
                    sub.append("S")
                elif "w" in piece:
                    sub.append("F")
                elif piece == "n":
                    sub.append("*")
                else:
                    sub.append(".")
            print("".join(sub))
        return 
    
def main():
    firstOrder = [int(i) for i in input().split(" ")]
    secondOrder = [int(i) for i in input().split(" ")]
    #firstOrder = [1,2,3,4,5]
    #secondOrder = [1,2,3,4,5]
    g = Game(firstOrder, secondOrder)
    
    g.play(1)
    g.outputBoard()
    print()
    g.play(2)
    g.outputBoard()
    print()
    
    # bug in this bit
    while True:
        if g.play(1) == -1: break
        if g.isFinished(): break
        if g.play(2) == -1: break
        if g.isFinished(): break
    g.outputBoard()
    
main()