# BIO round 1 q3 - 25/25
# similar technique to modern art (2015) and parking (2022)
from math import comb
from collections import defaultdict
import string

psbs = list(string.ascii_uppercase) + ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
p = len(psbs)

def getNumChars(n):
    # returns the number of characters the nth password has and the modified n
    # modified n is the nth password 
    curr = 1  # counter to store how many characters we have tried - 1 means we have tried passwords of length 1
    while True:
        if comb(p, curr) >= n:
            return curr, n
        n -= comb(p, curr)
        curr += 1

def getNumStarting(start, numChars):
    # returns the number of passwords starting with 'start' in a password with 'numChars' characters
    res = 0
    lettersRemaining = p - (psbs.index(start[-1])+1) # password needs to be in alphabetical order
    # to get the number looking for it's the number of characters - how many have already been found
    #   this is given by numChars-(start.index(start[-1])+1)
    # therefore for combinations do comb(lettersRemaining, numChars-(start.index(start[-1])+1)
    return comb(lettersRemaining, numChars-(start.index(start[-1])+1))

def getNextChar(current, used):
    # get next character that can be added
    while True:
        current = psbs[psbs.index(current)+1]
        if not used[current]:
            return current

def solve(n):
    # the technique here is documented more extensively in modern art(2015)
    numChars, modifiedN = getNumChars(n)
    res = ""
    current = "A" # start by looking at A
    used = defaultdict(lambda:False)
    while len(res) != numChars and modifiedN > 0:
        numStarting = getNumStarting(res+current, numChars)
        if numStarting < modifiedN:
            modifiedN -= numStarting
            current = getNextChar(current, used)
        else:
            if not used[current]:
                used[current] = True
                res += current
            current = getNextChar(current, used)
    return res


n = int(input())
print(solve(n))