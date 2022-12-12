# full marks
from functools import lru_cache

@lru_cache(maxsize=None)
def getPsbs(total, curr=0):
    if curr == total: return 1
    elif curr > total: return 0

    res = 0
    # blocks go from 1 to 10
    for i in range(1, 10):
        res += getPsbs(total, curr+i)
    return res

def solve(n, s):
    res = []
    while sum(res) < s:
        # print(res)
        for i in range(1, 9):
            p = getPsbs((s-sum(res))-i)
            # print(i, p, n)
            if p >= n:
                res.append(i)
                break
            else:
                n -= p
    return res

n,s = [int(i) for i in input().split(" ")]
print(*solve(n,s))