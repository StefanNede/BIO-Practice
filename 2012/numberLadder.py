# BIO round 1 q3 -
# bi bfs (?)
from collections import defaultdict, deque

digits = ["ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]
lettersPossible = ["O", "N", "E", "T", "W", "H", "R", "F", "U", "I", "V", "S", "X", "G", "Z"]

def getWordRep(num):
    res = ""
    for digit in str(num):
        res += digits[int(digit)]
    return res

def getDifferences(str1, str2):
    # returns the number of different letters between str1 and str2
    str1 = list(str1)
    str2 = list(str2)
    found = 0
    for letter in str1:
        if letter in str2:
            found += 2 # found in 2 places
    return len(str1) + len(str2) - found

def solve(start, stop):
    if getDifferences(getWordRep(start), getWordRep(stop)) <= 5:
        return 1

    forwardQueue = deque([(start, 0)])
    visitedForward = defaultdict(lambda:False)
    backwardQueue = deque([(start, 0)])
    visitedBackward = defaultdict(lambda:False)
    while forwardQueue and backwardQueue:
        # handle forward action
        number, steps = forwardQueue.popleft()
        number = getWordRep(number)
        # can either remove a letter or add a letter 5 times 
        # need a way to tell me if another number is 5 transformations away

        # handle backward action
        number, steps = backwardQueue.popleft()
        number = getWordRep(number)

    

for i in range(3):
    start, stop = [int(i) for i in input().split(' ')]
    print(solve(start, stop))