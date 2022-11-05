# 2008 BIO round 1 q3 - 24/24
from collections import defaultdict, deque
GOAL = 1234567

def solve(startOrder):
    # very simple BFS
    startOrder = [int(l) for l in str(startOrder)]
    queue = deque([(startOrder, 0)])
    visited = defaultdict(lambda:False)
    while queue:
        shirtArrangement, steps = queue.popleft()
        # leftmost shirt moved to middle, next 3 pushed left
        leftShirtArrangement = shirtArrangement[1:4] + [shirtArrangement[0]] + shirtArrangement[4:]
        if not visited[''.join([str(l) for l in leftShirtArrangement])] :
            if int(''.join([str(l) for l in leftShirtArrangement])) == GOAL:
                return steps + 1 
            visited[''.join([str(l) for l in leftShirtArrangement])] = True
            queue.append((leftShirtArrangement, steps+1))

        # rightmost shirt moved to middle, next 3 pushed right 
        rightShirtArrangement = shirtArrangement[:3] + [shirtArrangement[-1]] + shirtArrangement[3:-1]
        if not visited[''.join([str(l) for l in rightShirtArrangement])] :
            if int(''.join([str(l) for l in rightShirtArrangement])) == GOAL:
                return steps + 1 
            visited[''.join([str(l) for l in rightShirtArrangement])] = True
            queue.append((rightShirtArrangement, steps+1))

        # middle shirt removed and leftmost 3 pushed right
        middle1 = [shirtArrangement[3]] + shirtArrangement[:3] + shirtArrangement[4:]
        if not visited[''.join([str(l) for l in middle1])] :
            if int(''.join([str(l) for l in middle1])) == GOAL:
                return steps + 1 
            visited[''.join([str(l) for l in middle1])] = True
            queue.append((middle1, steps+1))

        # middle shirt removed and rigthmost 3 pushed left
        middle2 = shirtArrangement[:3] + shirtArrangement[4:] + [shirtArrangement[3]]
        if not visited[''.join([str(l) for l in middle2])] :
            if int(''.join([str(l) for l in middle2])) == GOAL:
                return steps + 1 
            visited[''.join([str(l) for l in middle2])] = True
            queue.append((middle2, steps+1))

    return "error"

startOrder = int(input())
print(solve(startOrder))