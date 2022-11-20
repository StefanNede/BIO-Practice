# BIO round 1 q3 - 27/27
from collections import defaultdict, deque

def getPossibleDiffsForward(current, maxValue):
    # a diff is 2^n
    diffs = []
    n = 0
    while (current+2**n)<=maxValue:
        diffs.append(2**n) 
        n += 1
    return diffs

def getPossibleDiffsBackwards(current, minValue=2):
    # minValue set to 2 because that is the smallest prime
    diffs = []
    n = 0
    while (current-2**n)>minValue:
        diffs.append(2**n)
        n += 1
    return diffs

def isPrime(num):
    if num == 1: return False
    if num == 2 or num == 3: return True
    for i in range(2, int(num**(1/2))+1):
        if num%i == 0: return False
    return True

def solve(maxValue, p, q):
    # 15 marks with normal bfs
    # 27 marks with bi-directional bfs

    # have separate queues and visited for both directions
    # if when getting next node for one of the queue it is in the visited of the
    # other direction it means they have intersected 
    # therefore we need to hold num moves it took us to get there in visited dictionary
    forwardQueue = deque([(p, 1)])
    backwardQueue = deque([(q, 1)])
    visitedForward = defaultdict(lambda:False)
    visitedBackward = defaultdict(lambda:False)
    visitedForward[p] = [True, 1] 
    visitedBackward[q] = [True, 1]
    while forwardQueue and backwardQueue:
        # perform an iteration of the forward queue
        currPrime, length = forwardQueue.popleft()
        diffsForward = getPossibleDiffsForward(currPrime, maxValue)
        diffsBackward = getPossibleDiffsBackwards(currPrime)
        for d in diffsForward:
            newPrime = currPrime + d
            if isPrime(newPrime) and visitedForward[newPrime] == False:
                visitedForward[newPrime] = [True, length+1]
                # check if it's the end point
                if visitedBackward[newPrime] != False:
                    return length+visitedBackward[newPrime][1]
                else:
                    forwardQueue.append((newPrime, length+1))
        for d in diffsBackward:
            newPrime = currPrime - d
            if isPrime(newPrime) and visitedForward[newPrime] == False:
                visitedForward[newPrime] = [True, length+1] 
                if visitedBackward[newPrime] != False:
                    return length+visitedBackward[newPrime][1]
                else:
                    forwardQueue.append((newPrime, length+1))
        
        # perform an iteration of the backward queue
        currPrime, length = backwardQueue.popleft()
        diffsForward = getPossibleDiffsForward(currPrime, maxValue)
        diffsBackward = getPossibleDiffsBackwards(currPrime)
        for d in diffsForward:
            newPrime = currPrime + d
            if isPrime(newPrime) and visitedBackward[newPrime] == False:
                visitedBackward[newPrime] = [True, length+1]
                # check if it's the end point
                if visitedForward[newPrime] != False:
                    return length+visitedForward[newPrime][1]
                else:
                    backwardQueue.append((newPrime, length+1))
        for d in diffsBackward:
            newPrime = currPrime - d
            if isPrime(newPrime) and visitedBackward[newPrime] == False:
                visitedBackward[newPrime] = [True, length+1] 
                if visitedForward[newPrime] != False:
                    return length+visitedForward[newPrime][1]
                else:
                    backwardQueue.append((newPrime, length+1))

    return -1

maxValue, p, q = [int(i) for i in input().split(' ')]
print(solve(maxValue, p, q))