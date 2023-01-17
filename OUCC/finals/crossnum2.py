# full marks
from copy import deepcopy
def solve(grid):
    starts = []
    res = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] != "X":
                # check left and right
                if grid[i][j-1] == "X" and grid[i][j+1] != "X":
                    starts.append([i,j])
                # check top and bottom
                elif grid[i-1][j] == "X" and grid[i+1][j] != "X":
                    starts.append([i,j])
    
    # check the lengths of the things that go from start
    for start in starts:
        cStart = deepcopy(start)
        # horizontal length
        hLength = 0
        while grid[start[0]][start[1]] != "X":
            hLength += 1
            start[1] += 1
        
        start = cStart
        cStart = deepcopy(start)
        # vertical length
        vLength = 0
        while grid[start[0]][start[1]] != "X":
            vLength += 1
            start[0] += 1
        
        start = cStart
    
        if max(hLength, vLength) > res:
            res = max(hLength, vLength)

    return res

n = [int(i) for i in input().split(" ")]
grid = []
grid.append("X" * (n[0] + 2))
for i in range(n[1]):
    grid.append("X" + input() + "X")
grid.append("X" * (n[0] + 2))
res = solve(grid)
print(res)