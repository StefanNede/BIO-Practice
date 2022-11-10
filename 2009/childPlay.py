# BIO round 1 q3 - 17/23
import time

res = []

def solve(s, nums):
    # dfs solution
    global res
    if s == 0:
        res.append(nums)
        return
    else:
        for i in range(1, min(s, 9)+1):
            solve(s-i, nums+str(i))

s, n = [int(i) for i in input().split(' ')]
start = time.time()
solve(s, '')
end = time.time()
print(' '.join(res[n-1]))
print(end-start)