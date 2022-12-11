# BIO round 1 q3 - 17/23 -> just 2 sub test case that doesn't work, very weird
# 256 361 and 66 71 not working
from collections import defaultdict, deque

digits = ["ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]

def getWordRep(num):
    res = ""
    for digit in str(num):
        res += digits[int(digit)]
    return res

def getDifferences(str1, str2):
    # returns the number of different letters between str1 and str2
    cstr1 = list(str1)
    cstr2 = list(str2)
    for letter in str1:
        if letter in cstr2:
            cstr1.remove(letter)
            cstr2.remove(letter)
    return len(cstr1) + len(cstr2)

# print(getDifferences(getWordRep(610), getWordRep(90)))
def solve(start, stop):
    possibleRes = [i for i in range(1, 1000)] # number ladder only uses numbers between 1 and 999 inclusive
    # uses bi-bfs
    if getDifferences(getWordRep(start), getWordRep(stop)) <= 5:
        return 1

    forwardQueue = deque([(start, 0)])
    visitedForward = defaultdict(lambda:False)
    visitedForward[start] = [True, 0]
    backwardQueue = deque([(stop, 0)])
    visitedBackward = defaultdict(lambda:False)
    visitedBackward[stop] = [True, 0]

    while forwardQueue and backwardQueue:
        # handle forward action
        number, steps = forwardQueue.popleft()
        # can either remove a letter or add a letter 5 times 
        for p in possibleRes:
            if getDifferences(getWordRep(p), getWordRep(number)) <= 5:
                if not visitedForward[p]:
                    visitedForward[p] = [True, steps+1]
                    forwardQueue.append((p, steps+1))
                    if visitedBackward[p]:
                        return visitedForward[p][1] + visitedBackward[p][1]

        # handle backward action
        number, steps = backwardQueue.popleft()
        for p in possibleRes:
            if getDifferences(getWordRep(p), getWordRep(number)) <= 5:
                if not visitedBackward[p]:
                    visitedBackward[p] = [True, steps+1]
                    backwardQueue.append((p, steps+1))
                    if visitedForward[p]:
                        return visitedBackward[p][1] + visitedForward[p][1]

for i in range(3):
    start, stop = [int(i) for i in input().split(' ')]
    print(solve(start, stop))