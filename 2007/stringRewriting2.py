# BIO round 1 q3 -
from collections import defaultdict
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
    count = fib(steps)
    if count <= p:
        if steps == 1:
            return count, [0, 1]
        return count, [fib(steps-1), fib(steps)]

    # else cases more complicated
    return p, []


def getB(steps, p):
    count = fib(steps+1)
    if count <= p:
        return count, [fib(steps), fib(steps+1)]
    # else cases more complicated
    return p, []


def getC(steps, p):
    count = 2**(steps)
    if count <= p:
        return count, [int(count/2), int(count/2)]
    elif p == 1:
        return p, [1, 0]
    elif p % 2 == 0:
        return p, [int(p/2), int(p/2)]
    # p being odd is confusing
    return p, [int((p-1)/2), int((p-1)/2)]


def getD(steps, p):
    count = 2**(steps)
    if count <= p:
        return count, [int(count/2), int(count/2)]
    elif p == 1:
        return p, [0, 1]
    elif p % 2 == 0:
        return p, [int(p/2), int(p/2)]
    # p being odd is confusing
    return p, [int((p-1)/2), int((p-1)/2)]


def getE(steps, p):
    count = 2**(steps)
    if count <= p:
        return count, [count]
    return p, [p]


def solve(string, steps, p):
    res = [0, 0, 0, 0, 0]
    for letter in string:
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
