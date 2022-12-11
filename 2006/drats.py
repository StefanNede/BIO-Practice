# bio round 1 q3 - 25/25
from functools import lru_cache

segments = [i for i in range(1, 21)]

@lru_cache(maxsize=None)
def getPsbs(target, dratsLeft):
    if target == 0 and dratsLeft == 0: return 1
    elif target < 0 or dratsLeft < 0: return 0

    res = 0
    for i in segments:
        res += getPsbs(target-i, dratsLeft-1)
    return res

def solve(target, drats):
    res = 0
    # the number of possibilities depending on where the first drat hits
    for i in segments:
        first = i*2
        if first <= target:
            res += getPsbs(target-first, drats-1)
    return res

target, drats = [int(i) for i in input().split(" ")]
print(solve(target, drats))