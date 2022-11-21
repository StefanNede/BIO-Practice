def getInversions(arr):
    # for each 1 count the number of 0s that appear in the array after it and that is the result
    count = 0
    for i in range(len(arr)):
        if arr[i] == 1:
            count += arr[i:].count(0)
    return count

def solve(arr):
    if len(arr) == 2:
        return 1
    # consider if the optimum amount of inversions is before any operations are performed
    # if the array starts with a 1 the most 1s will benefit if the final 1 is turned to a 0
    if arr[0] == 1:
        prevInversions = getInversions(arr)
        for i in range(len(arr)-1, 0, -1):
            if arr[i] == 1:
                arr[i] = 0
                break
        newInversions = getInversions(arr)
        if prevInversions > newInversions:
            return prevInversions
        else:
            return newInversions
            
    # if the array doesn't start with a 1 
    else:
        return getInversions(arr)

t = int(input())
for i in range(t):
    n = int(input())
    arr = [int(i) for i in input().split(' ')]
    print(solve(arr))