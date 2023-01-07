def solve(arr):
    if len(arr) == 1: return "YES"
    for i in range(len(arr)-1):
        if arr[i] < arr[i+1]:
            while (arr[i+1] >= arr[i]) and (i < len(arr)-2):
                i += 1
            if i == len(arr)-2:
                return "YES"
            else:
                return "NO"

t = int(input())
for i in range(t):
    n = int(input())
    arr = [int(j) for j in input().split(' ')]
    print(solve(arr))