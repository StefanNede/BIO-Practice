# success
t = int(input())
for i in range(t):
    n = int(input())
    strengths = [int(j) for j in input().split(' ')]
    greatest = sorted(strengths)[-1]
    sGreatest = sorted(strengths)[-2]
    for s in strengths:
        if s == greatest:
            print(s-sGreatest, end=" ")
        else:
            print(s-greatest, end=" ")
    print()