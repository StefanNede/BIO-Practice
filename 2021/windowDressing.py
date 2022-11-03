# 2021 round 1 q3 - 24/24 
from collections import deque, defaultdict 
import string

ALPHA = string.ascii_lowercase

def solve(target):
    '''
    add - next box from warehouse can be added at end of boxes on display
    swap - first 2 boxes swapped
    rotate - first box moved to end of display

    the number of moves will be the layer of the tree we are in
    use bfs to search through possibilities until target found
        - need a queue - hold the next nodes to visit, and the depth we are currently in
        - neeed a visited array
    hold the current display in a list because swap and rotate are easier to do
    '''
    warehouse = ALPHA[:len(target)]
    target = list(target)
    queue = deque([(list(),0)])
    visited = defaultdict(lambda:False)
    
    # if the target is in alphabetical order the shortest number of steps is just to add n times where n is length of target
    if sorted(target) == target:
        return len(target)

    while queue:
        # print(queue)
        currentDisplay, steps = queue.popleft()
        
        if currentDisplay == target:
            return steps

        # visited.append(currentDisplay)
        # now perform 3 operations on currentDisplay and add them to queue with step being 1 higher
        # add - can only do this if all the boxes from the warehouse haven't been added
        if len(currentDisplay) < len(warehouse):
            addedDisplay = currentDisplay + [warehouse[len(currentDisplay) - len(warehouse)]] 
            if addedDisplay == target: return steps+1
            if visited[''.join(addedDisplay)] == False:
                queue.append((addedDisplay, steps+1))
                visited[''.join(addedDisplay)] = True
        
        # swap - can only do this if the length is 2+
        if len(currentDisplay) >= 2:
            swappedDisplay = [currentDisplay[1], currentDisplay[0]] + currentDisplay[2:]
            if swappedDisplay == target: return steps+1
            if visited[''.join(swappedDisplay)] == False:
                queue.append((swappedDisplay, steps+1))
                visited[''.join(swappedDisplay)] = True

        # rotate - can only do this if the length is 3+ because swapping and rotating at length 2 is the same  
        if len(currentDisplay) >= 3:
            rotatedDisplay = currentDisplay[1:] + [currentDisplay[0]]
            if rotatedDisplay == target: return steps+1
            if visited[''.join(rotatedDisplay)] == False:
                queue.append((rotatedDisplay, steps+1))
                visited[''.join(rotatedDisplay)] = True

    return "Impossible" 

target = input().lower()
print(solve(target))