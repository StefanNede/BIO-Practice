# BIO round 1 2020 q3
import string, math
from functools import lru_cache

p, maxAdj, numLetters = [int(i) for i in input().split(' ')]
n = int(input())
alphabet = string.ascii_uppercase
alphabet = list(alphabet[:p])

@lru_cache(maxsize = None)
def getWays(lettersLeft, maxAdj, lastLetter="", curAdj = 1):
    if lettersLeft < 0 or curAdj > maxAdj:
        return 0
    # have reached the end of a successful run
    elif lettersLeft == 0: 
        return 1
    
    total = 0
    for l in alphabet:
        if l == lastLetter:
            total += getWays(lettersLeft-1, maxAdj, l, curAdj+1)
        else:
            total += getWays(lettersLeft-1, maxAdj, l, 1)
    return total

def solve(numLetters, maxAdj, n):
    '''
    permute letters in modified alphabet for a res of length
    where there can only be maxAdj adjacent letters

    possibly use a technique similar to modern art or parking (?)
    because again the plans will be in alphabetical order

    goal: output nth plan 
    '''
    numWays = getWays(numLetters, maxAdj)
    res = ""
    while len(res) != n:

        pass
    return res

# print(getWays(numLetters, maxAdj))
print(solve(numLetters, maxAdj, n))