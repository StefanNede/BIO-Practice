# Bio round 1 q3 - 24/24
from collections import defaultdict, deque

def getNext(serialNum):
    # returns a list of all the possible serial number following the one passed in
    nexts = []
    serialNum = list(str(serialNum))
    for i in range(len(serialNum)-1):
        # check if there are adjacent numbers in between i and i+1
        num1 = serialNum[i]
        num2 = serialNum[i+1]
        if i-1 >= 0 and ((serialNum[i-1] < num1 and serialNum[i-1] > num2) or (serialNum[i-1] > num1 and serialNum[i-1] < num2)):
            # can swap them
            nexts.append("".join(serialNum[:i] + [serialNum[i+1]] + [serialNum[i]] + serialNum[i+2:]))

        elif i+2 < len(serialNum):
            if (serialNum[i+2] < num1 and serialNum[i+2] > num2) or (serialNum[i+2] > num1 and serialNum[i+2] < num2):
                # can swap them
                nexts.append("".join(serialNum[:i] + [serialNum[i+1]] + [serialNum[i]] + serialNum[i+2:]))
    
    return nexts

def getLongest(serialNum, numDigits):
    if len(str(serialNum)) == 1 or len(getNext(str(serialNum))) == 0: return 0
    queue = deque([(serialNum, 0)])
    visited = defaultdict(lambda:False)
    visited[str(serialNum)] = True
    highest = 0
    while queue:
        sNum, count = queue.popleft()
        if count > highest:
            highest = count
        nexts = getNext(sNum)
        # print(sNum, nexts)
        for n in nexts:
            if not visited[n]:
                queue.append((n, count+1))
                visited[n] = True
    return highest

numDigits = int(input())
serialNum = int(input())
print(getLongest(serialNum, numDigits))