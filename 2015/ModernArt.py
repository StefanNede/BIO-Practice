# Modern Art - Bio round 1 2015 q3
# 11 mark solution
from itertools import permutations

inp = input().split(' ')
a, b, c, d, n = int(inp[0]), int(inp[1]), int(inp[2]), int(inp[3]), int(inp[4])

lst = ['A']*a + ['B']*b + ['C']*c + ['D']*d
perms = list(permutations(''.join(lst), len(lst))) # has repeats
perms2 = list(dict.fromkeys(perms))
print(''.join(perms2[n-1]))