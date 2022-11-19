# BIO round 1 2020 q2
import string
from collections import defaultdict

ALPHA  = list(string.ascii_uppercase)
# each room identifiede by a single letter
# each exit form a room marked with the letter identifying the room to which it is connected
class Room:
    def __init__(self, letter):
        self.letter = letter

# for each room they keep track of whether they have visited it an even or odd number of times
# visited room odd num times => leave through the exit which is marked with the first letter alphabetically
# even num times => find first exit alphabetically that have left through odd num times
#                       WHILE LOOP
#                       if is last exit alphabetically in this room they will leave through it
#                       otherwise leave through next exit alphabetically
class Spy:
    def __init__(self):
        self.roomsVisited = []
    
# to make map:
#       - choose first room alphabetically which has noy yet been chosen and which is not in the plan
#               chosen room connected to the first room in the plan
#               then first room removed from the plan
#       - above step repeated until plan is empty
#       - there will be 2 rooms which have not yet been chosen => connect them together so each room has an exit to the other room
class Map:
    def __init__(self, plan):
        self.plan = plan

    def makeMap(self):
        pass

# at start they have visited their starting room an odd number of times, each other even 
class Game:
    def __init__(self, roomsId, move1, move2):
        self.roomsId = roomsId
        self.rooms = self.createRooms()
        self.move1 = move1
        self.move2 = move2
        self.map = Map(roomsId)
    
    def createRooms(self):
        lst = []
        for roomId in self.roomsId:
            room = Room(room)
            lst.append(room)
        lst.sort()
        return lst
    
    def getNextAlphabetical(self, currentPtr):
        ptr = currentPtr
        room = ''
        while True:
            if ptr > len(self.rooms): break
            room = self.rooms[ptr]
            # do stuff with the room and break out if the room works
            # otherwise continue
            ptr += 1
        return room
        

def main():
    rooms, p, q = [i for i in input().split()]
    p, q = int(p), int(q)
    game = Game(rooms, p, q)

if __name__ == "__main__":
    main()