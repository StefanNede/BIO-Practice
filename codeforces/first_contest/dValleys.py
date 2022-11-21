# TLE exceeded on test 3
def allSame(arr, l, r):
    if len(arr[l:r+1]) == 1:
        return True
    el = arr[l]
    for e in arr[l:r+1]:
        if e != el: return False
    return True

def solve(arr):
    if len(arr) == 1: return "YES"
    l = 0
    r = 0
    count = 0
    for l in range(len(arr)):
        for r in range(l, len(arr)):
                if ((l <= r and r <= len(arr)-1) and allSame(arr, l, r)) and (l == 0 or arr[l-1]>arr[l]) and (r == len(arr)-1 or arr[r] < arr[r+1]):
                    # if count is 1 then return "NO"
                    if count == 1: return "NO"
                    else: 
                        count += 1

    if count == 0: return "NO"
    else: return "YES"

t = int(input())
for i in range(t):
    n = int(input())
    arr = [int(j) for j in input().split(' ')]
    print(solve(arr))