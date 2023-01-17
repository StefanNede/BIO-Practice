# 7/8 - idk why
# basic greedy

n = int(input())
res = 0
leftOver = 0
for i in range(n):
    x = int(input())
    x += leftOver
    leftOver = 0
    res += x//2
    leftOver = x%2

print(res + leftOver)