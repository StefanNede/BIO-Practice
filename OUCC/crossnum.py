def solve(grid):
    res = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] != "X":
                # check left and right
                if grid[i][j-1] == "X" and grid[i][j+1] != "X":
                    res += 1
                # check top and bottom
                elif grid[i-1][j] == "X" and grid[i+1][j] != "X":
                    res += 1
    return res

n = [int(i) for i in input().split(" ")]
grid = []
grid.append("X" * (n[0] + 2))
for i in range(n[1]):
    grid.append("X" + input() + "X")
grid.append("X" * (n[0] + 2))
res = solve(grid)
print(res)