# BIO round 1 2020 q3 - 27/27
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
    use a technique similar to modern art or parking 
    because again the plans will be in alphabetical order
    '''
    res = ""
    counter = 0
    adjs = 1
    while len(res) != numLetters:
        currentLetter = alphabet[counter]
        if len(res)>=1 and currentLetter == res[-1]:
            adjs += 1
        if len(res)>= 1 and currentLetter != res[-1]:
            adjs = 1
        numWays = getWays(numLetters-(len(res)+1), maxAdj, currentLetter, adjs) 
        if adjs > maxAdj:
            adjs = 1
            counter += 1
            counter %= len(alphabet)
        elif numWays >= n:
            res += currentLetter
            # reset counter
            counter = 0
        else:
            n -= numWays
            counter += 1
            counter %= len(alphabet)
    return res

# print(getWays(numLetters-1, maxAdj, "A"))
print(solve(numLetters, maxAdj, n))