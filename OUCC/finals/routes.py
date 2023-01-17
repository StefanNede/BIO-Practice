# 7/8 - idk why
# basic dfs
from collections import defaultdict

tree = defaultdict(lambda: [])
els = input()
n = int(input())
for i in range(n):
    pair = input().split(",")
    tree[pair[0]].append(pair[1])

count = 0
target = els[-1]

# dfs on the tree
def solve(current = 'a', visited = []):
    global count
    if current == target and tree[current] != target:
        count += 1
    else:
        for el in tree[current]:
            if el not in visited:
                solve(el, visited + [el])

solve()
print(count)