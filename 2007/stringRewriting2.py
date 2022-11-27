# BIO round 1 q3 - 25/25
# lots of repeated code so can be made shorter but works
from collections import deque
from functools import lru_cache
import string

ALPHA = list(string.ascii_uppercase)[:5]
LOOKUP = {"A": "B", "B": "AB", "C": "CD", "D": "DC", "E": "EE"}

@lru_cache(maxsize=None)
def fib(n):
    if n <= 2:
        return 1
    return fib(n-2) + fib(n-1)

def getA(steps, p):
    count = fib(steps) + fib(steps-1)
    if count <= p:
        if steps == 1:
            return count, [0, 1]
        return count, [fib(steps-1), fib(steps)]
    elif p == 1:
        return p, [0, 1]

    # A -> B
    # uses technique explained in getD()
    d = deque([("B", steps-1)])
    resCounts = [0, 0]
    while d and p > 0:
        curr, s = d.popleft()
        if curr == 'A':
            totalCount, counts = getA(s, p)
            if totalCount <= p:
                resCounts[0] += counts[0]
                resCounts[1] += counts[1]
                p -= totalCount
            else:
                if steps - 1 > 0:
                    d.appendleft(("B", steps-1))

        elif curr == 'B':
            totalCount, counts = getB(s, p)
            if totalCount <= p:
                resCounts[0] += counts[0]
                resCounts[1] += counts[1]
                p -= totalCount
            else:
                if steps-1 > 0:
                    d.appendleft(("A", steps-1))

    return sum(resCounts), resCounts

def getB(steps, p):
    count = fib(steps+1) + fib(steps)
    if count <= p:
        return count, [fib(steps), fib(steps+1)]
    elif p == 1:
        return p, [1, 1]

    # B -> AB
    # uses technique explained in getD()
    d = deque([("A", steps-1), ("B", steps-1)])
    resCounts = [0, 0]
    while d and p > 0:
        curr, s = d.popleft()
        if curr == 'A':
            totalCount, counts = getA(s, p)
            if totalCount <= p:
                resCounts[0] += counts[0]
                resCounts[1] += counts[1]
                p -= totalCount
            else:
                if steps - 1 > 0:
                    d.appendleft(("B", steps-1))

        elif curr == 'B':
            totalCount, counts = getB(s, p)
            if totalCount <= p:
                resCounts[0] += counts[0]
                resCounts[1] += counts[1]
                p -= totalCount
            else:
                if steps-1 > 0:
                    d.appendleft(("A", steps-1))

    return sum(resCounts), resCounts

def getC(steps, p):
    count = 2**(steps)
    if count <= p:
        return count, [int(count/2), int(count/2)]
    elif p == 1:
        return p, [1, 0]
    elif p % 2 == 0:
        return p, [int(p/2), int(p/2)]

    # C -> CD
    # uses technique explained in getD()
    d = deque([("C", steps-1), ("D", steps-1)])
    resCounts = [0, 0]
    while d and p > 0:
        curr, s = d.popleft()
        if curr == 'D':
            totalCount, counts = getD(s, p)
            if totalCount <= p:
                resCounts[0] += counts[0]
                resCounts[1] += counts[1]
                p -= totalCount
            else:
                if steps - 1 > 0:
                    d.appendleft(("D", steps-1))
        elif curr == 'C':
            totalCount, counts = getC(s, p)
            if totalCount <= p:
                resCounts[0] += counts[0]
                resCounts[1] += counts[1]
                p -= totalCount
            else:
                if steps-1 > 0:
                    d.appendleft(("C", steps-1))

    return sum(resCounts), resCounts

def getD(steps, p):
    count = 2**(steps)
    if count <= p:
        return count, [int(count/2), int(count/2)]
    elif p == 1:
        return p, [0, 1]
    elif p % 2 == 0:
        return p, [int(p/2), int(p/2)]

    # so D goes to DC - we can cut off some steps if they only impact characters later than p
    # so we look at D and if count is too big then we look at D with one less step and so on until count is less than p
    # then if p is still not 0 we look at C after steps-1 (steps being the original steps) and do the same as we did with D
    # we look at D before C because that is what happens in the lookup
    # store these in a deque and go over them
    # items in deque store D or C and the number of steps we have gotten to that we need to try
    d = deque([("D", steps-1), ("C", steps-1)])
    resCounts = [0, 0]
    while d and p > 0:
        curr, s = d.popleft()
        if curr == 'D':
            totalCount, counts = getD(s, p)
            if totalCount <= p:
                resCounts[0] += counts[0]
                resCounts[1] += counts[1]
                p -= totalCount
            else:
                if steps - 1 > 0:
                    d.appendleft(("D", steps-1))
        elif curr == 'C':
            totalCount, counts = getC(s, p)
            if totalCount <= p:
                resCounts[0] += counts[0]
                resCounts[1] += counts[1]
                p -= totalCount
            else:
                if steps-1 > 0:
                    d.appendleft(("C", steps-1))

    return sum(resCounts), resCounts

def getE(steps, p):
    count = 2**(steps)
    if count <= p:
        return count, [count]
    return p, [p]

def solve(string, steps, p):
    res = [0, 0, 0, 0, 0]
    for letter in string:
        if p == 0:
            break
        if letter == 'A':
            characters, letterCount = getA(steps, p)
            res[0] += letterCount[0]
            res[1] += letterCount[1]
            p -= characters
        elif letter == 'B':
            characters, letterCount = getB(steps, p)
            res[0] += letterCount[0]
            res[1] += letterCount[1]
            p -= characters
        elif letter == 'C':
            characters, letterCount = getC(steps, p)
            res[2] += letterCount[0]
            res[3] += letterCount[1]
            p -= characters
        elif letter == 'D':
            characters, letterCount = getD(steps, p)
            res[2] += letterCount[0]
            res[3] += letterCount[1]
            p -= characters
        elif letter == 'E':
            characters, letterCount = getE(steps, p)
            res[4] += letterCount[0]
            p -= characters
    return res

string = input()
steps, p = [int(i) for i in input().split(' ')]
res = solve(string, steps, p)
for r in res:
    print(r, end=" ")