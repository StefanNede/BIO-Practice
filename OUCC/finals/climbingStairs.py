# full marks
# this question is basically just the fibonacci sequence
# using a bottom up iterative approach instead of recursive is used
# due to python's recursion limit
def solve(n):
    p1, p2 = 1,1
    for i in range(n-1):
        n = p1 + p2
        p2 = p1
        p1 = n
    return p1

n = int(input())
res = solve(n)
print(res)