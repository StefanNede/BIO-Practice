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
    
class Map:
    def __init__(self, plan):
        self.plan = list(plan)
        self.roomsLeft = ALPHA[:len(plan)+2]
        self.map = defaultdict(lambda:[]) # this will be a sort of tree 
    
    def getRoomsNotInPlan(self) -> list:
        res = []
        for room in self.roomsLeft:
            if room not in self.plan:
                res.append(room)
        return res

    def makeMap(self):
        # update self.map
        roomsNotPlan = self.getRoomsNotInPlan()
        while len(self.plan) > 0:
            r = roomsNotPlan.pop(0)
            self.roomsLeft.remove(r)
            firstPlanRoom = self.plan.pop(0) # get first room in plan and remove it from plan
            # create connections
            if len(self.map[r]) == 0:
                self.map[r] = firstPlanRoom 
            else:
                self.map[r] = self.map[r] + [firstPlanRoom]
            
            # add to roomsNotPlan if they have not already been chosen and are no longer in the plan
            if len(self.map[firstPlanRoom]) == 0 and firstPlanRoom not in self.plan:
                roomsNotPlan.append(firstPlanRoom)
                roomsNotPlan.sort()
        
        # rooms never chosen - self.roomsLeft
        room1, room2 = self.roomsLeft[0], self.roomsLeft[1]
        # create connection
        if len(self.map[room1]) == 0:
            self.map[room1] = room2 
        else:
            self.map[room1] = self.map[room2] + [firstPlanRoom]
    
    def getMap(self) -> dict:
        self.makeMap()
        return self.map

# at start they have visited their starting room an odd number of times, each other even 
class Game:
    def __init__(self, plan, move1, move2):
        self.rooms = self.createRooms()
        self.move1 = move1
        self.move2 = move2
        self.map = Map(plan)
        self.map = self.map.getMap() # will be a defaultdict
    
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
    plan, p, q = [i for i in input().split()]
    p, q = int(p), int(q)
    game = Game(plan, p, q)

if __name__ == "__main__":
    main()