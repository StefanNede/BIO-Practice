# BIO round 1 2020 q2 - 24/24
import string
from collections import defaultdict

ALPHA  = list(string.ascii_uppercase)

class Map:
    def __init__(self, plan):
        self.planLen = len(plan) # for use later
        self.plan = list(plan)
        self.roomsLeft = ALPHA[:self.planLen+2]
        self.map = defaultdict(lambda:"")
        self.invertedMap = defaultdict(lambda:"")
        self.resMap = defaultdict(lambda:[]) 
    
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
                self.map[r] = self.map[r] + firstPlanRoom
            
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
            self.map[room1] = self.map[room2] + firstPlanRoom
    
    def getInvertedMap(self):
        for key, val in dict(self.map).items():
            for v in val:
                if len(self.invertedMap[v]) == 0:
                    self.invertedMap[v] = key 
                else:
                    self.invertedMap[v] = self.invertedMap[v] + key 
    
    def getMap(self) -> dict:
        self.makeMap()
        self.getInvertedMap() # the keys are the values and values are the keys
        # format the map -> if C is connected to A and A is connected to E then A is connected to C and E
        # compile map and invertedMap
        for room in ALPHA[:self.planLen+2]:
            self.resMap[room] = sorted(self.map[room] + self.invertedMap[room])

        return self.resMap 

# at start they have visited their starting room an odd number of times, each other even 
class Game:
    def __init__(self, plan):
        self.visitedRooms = defaultdict(lambda:0)
        self.visitedRooms['A'] = 1 # visited starting room odd num times
        # for each room keep track of the exits used
        self.visitedExits = defaultdict(lambda:defaultdict(lambda:0))
        self.currentRoom = "A"
        self.map = Map(plan)
        self.map = self.map.getMap() # will be a defaultdict
    
    def move(self):
       self.getNextExit() 
    
    def getNextExit(self):
        exits = self.map[self.currentRoom]
        if len(exits) == 1:
            self.visitedExits[self.currentRoom][exits[0]] += 1
            self.currentRoom = exits[0]
            self.visitedRooms[self.currentRoom] += 1
        elif self.visitedRooms[self.currentRoom]%2 == 1:
            # leave through first exit alphabetically
            self.visitedExits[self.currentRoom][exits[0]] += 1
            self.currentRoom = exits[0]
            self.visitedRooms[self.currentRoom] += 1
        else:
            for e in exits:
                if self.visitedExits[self.currentRoom][e]%2 == 1:
                    if e == exits[-1]:
                        self.visitedExits[self.currentRoom][e] += 1
                        self.currentRoom = e
                        self.visitedRooms[self.currentRoom] += 1
                    else:
                        # leave through next exit alphabetically
                        eIndex = exits.index(e)+1
                        e = exits[eIndex]
                        self.visitedExits[self.currentRoom][e] += 1
                        self.currentRoom = e
                        self.visitedRooms[self.currentRoom] += 1
                    break

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
    game = Game(plan)

    # outputs
    for room in game.map:
        print("".join(game.map[room]))
    for i in range(p): game.move()
    print(game.currentRoom, end="")
    for j in range(q-p): game.move()
    print(game.currentRoom)

if __name__ == "__main__":
    main()