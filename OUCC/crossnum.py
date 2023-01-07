# given a crossnumber return how many hints will be needed
def solve(n):
    grid = []
    starts = []
    counter = 0
    # pad with "X"s to avoid handling edge cases manually
    grid.append("X" * (n[0]+2))
    for i in range(n[0]):
        grid.append("X" + input() + "X")
    grid.append("X" * (n[0]+2))

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            found = False
            if grid[i][j] != "X":
                    if grid[i-1][j] == "X" and grid[i+1][j]!='X':
                        counter += 1
                    elif grid[i][j-1] == 'X' and grid[i][j+1]!='X':
                        counter += 1
    return counter

n = [int(i) for i in input().split(" ")]
print(solve(n))