# BIO round 1 q3
from math import comb
import string

psbs = list(string.ascii_uppercase) + [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
p = len(psbs)


def getNumChars(n):
    # returns the number of characters the nth password has
    curr = 1  # counter to store how many characters we have tried - 1 means we have tried passwords of length 1
    while True:
        # slightly flawed - there might be a difference as they need to be in alphabetical order
        if comb(p, curr) > n:
            return curr
        curr += 1


def solve(n):
    return getNumChars(n)


n = int(input())
print(solve(n))
