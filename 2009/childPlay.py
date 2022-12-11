# BIO round 1 q3 - 17/23
# similar technique to modern art (2015)
from functools import lru_cache

# dfs solution - 17/23
res = []
def solveDFS(s, nums):
    global res
    if s == 0:
        res.append(nums)
        return
    else:
        for i in range(1, min(s, 9)+1):
            solve(s-i, nums+str(i))

# s, n = [int(i) for i in input().split(' ')]
# solveDFS(s, '')
# print(' '.join(res[n-1]))

# fast solution - 23/23
@lru_cache(maxsize=None)
def getPsbs(s, cur=0):
    # number of ways to get 4 is 1 + getPsbs(3)
    # 3 is 2 + getPsbs(2) ...
    # returns the number of ways s-cur can be made- e.g. 4 can be made in 8 ways, so get this with s = 4, cur = 0
    if cur > s: return 0
    if cur == s: return 1
    res = 0
    # the blocks only go from 1 to 9 so we need the min statement here
    for i in range(1, min((s-cur)+1, 10)):
        res += getPsbs(s, cur+i)
    return res

def solve(s, n):
    res = []
    options = [i for i in range(1, s+1)]
    pointer = 0
    while sum(res) < s:
        nex = options[pointer]
        psbs = getPsbs(s-(sum(res)+nex))
        if psbs >= n:
            res.append(nex)
            pointer = 0
        else:
            n -= psbs
            pointer += 1

    return res

s, n = [int(i) for i in input().split(' ')]
print(*solve(s, n))