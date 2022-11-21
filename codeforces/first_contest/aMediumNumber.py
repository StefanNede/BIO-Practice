# success
n = int(input())
for i in range(n):
    l = [int(i) for i in input().split(' ')]
    l.sort()
    print(l[1])