# 2010 BIO round 1 q3 - full marks
# 3b - fill b, pour from b into a, empty a, pour from b into a, left with 2 in b - 2 marks
from collections import defaultdict, deque

def solve(noJ, target, capacities):
    '''
    can either:
    - fill up a jug completely
    - pour as much liquid as possible from one jug to another
    - empty a jug

    have a queue that has:
    ([volume in jug 1, volume in jug 2, volume in jug 3 ...], steps) 
    '''
    volumes = [0] * noJ 
    queue = deque([(volumes, 0)])
    visited = defaultdict(lambda:False)

    while queue:
        jugs, steps = queue.popleft()
        for i in range(len(jugs)):
            capacity = capacities[i]
            jug = jugs[i]
            if jug == target:
                return steps
            # fill up a jug
            if jug != capacity:
                filledJug = capacity
                newJugs = jugs[:i] + [filledJug] + jugs[i+1:]
                if visited[''.join([str(l) for l in newJugs])] == False:
                    # print(f"Filled jug {i}", jugs, newJugs)
                    queue.append((newJugs, steps+1))
                    visited[''.join([str(l) for l in newJugs])] = True

            # NOT WORKING
            # pour as much liquid from one jug to another - need another for loop to go through all other jug
            # but we need to maintain the order of the jugs  
            leftJugs = jugs[:i]
            rightJugs = jugs[i+1:]
            
            if jug > 0: 
                # go through other jugs to the left:
                for j in range(i):
                    if leftJugs[j] < capacities[j]:
                        difference = capacities[j] - leftJugs[j]
                        addedAmount = min(jug, difference)
                        newLeftJug = leftJugs[j] + addedAmount
                        newJug = jug - addedAmount
                        newJugs = jugs[:j] + [newLeftJug] + jugs[j+1:i] + [newJug] + rightJugs 
                        if visited[''.join([str(l) for l in newJugs])] == False:
                            # print(f"Moved water from {i} to {j}", jugs, newJugs)
                            queue.append((newJugs, steps+1))
                            visited[''.join([str(l) for l in newJugs])] = True
                
                # go through other jugs to the right
                for k in range(i+1, len(jugs)):
                    if jugs[k] < capacities[k]:
                        difference = capacities[k] - jugs[k]
                        addedAmount = min(jug, difference)
                        newRightJug = jugs[k] + addedAmount
                        newJug = jug - addedAmount
                        newJugs = leftJugs + [newJug] + jugs[i+1:k] + [newRightJug] + jugs[k+1:]
                        if visited[''.join([str(l) for l in newJugs])] == False:
                            # print(f"Moved water from {i} to {k}", jugs, newJugs)
                            queue.append((newJugs, steps+1))
                            visited[''.join([str(l) for l in newJugs])] = True

            # empty a jug
            if jug != 0:
                emptyJug = 0
                newJugs = jugs[:i] + [emptyJug] + jugs[i+1:]
                if visited[''.join([str(l) for l in newJugs])] == False:
                    # print(f"Emptied jug {i}", jugs, newJugs)
                    queue.append((newJugs, steps+1))
                    visited[''.join([str(l) for l in newJugs])] = True

    return "Impossible"

noJ, target = [int(i) for i in input().split(' ')]
capacities = [int(i) for i in input().split(' ')]
print(solve(noJ, target, capacities))