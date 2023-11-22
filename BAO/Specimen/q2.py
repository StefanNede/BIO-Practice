# 18/18
from collections import defaultdict

def getGradientPairings(pairings):
    gp = defaultdict(lambda:[])
    for i in range(len(pairings)):
        for j in range(i+1, len(pairings)):
            p1 = pairings[i]
            p2 = pairings[j]
            gradient = 0
            if p1[0] == p2[0]:
                gradient = None
            else: 
                gradient = (p2[1]-p1[1])/(p2[0]-p1[0])
            gp[gradient] += [(p1, p2)]
    return gp

def getPairings(s):
    pairings = [s[i:i+2] for i in range(0, len(s)-1, 2)]
    return pairings

def solve(s):
    pairings = getPairings(s)
    gp = getGradientPairings(pairings)
    # print(pairings)
    # print(gp)
    best = 0

    # go through each pairs of gradient pairs with same gradient (for the parallel sides) and find value of Z
    for gradient, pairs in gp.items():
        for i in range(len(pairs)):
            for j in range(i, len(pairs)):
                p1 = pairs[i]
                p2 = pairs[j]
                baseLength = ((p1[0][0]-p1[1][0])**2 + (p1[0][1]-p1[1][1])**2)**0.5
                topLength = ((p2[0][0]-p2[1][0])**2 + (p2[0][1]-p2[1][1])**2)**0.5
                if gradient == None:
                    height = abs(p2[0][0] - p1[0][0])
                    size = ((baseLength + topLength)/2)*height
                    best = max(best, size)
                if gradient != None:
                    c1 = p1[0][1] - gradient*p1[0][0]
                    c2 = p2[0][1] - gradient*p2[0][0]
                    height = (abs(c2-c1))/((gradient**2 + 1)**0.5)
                    size = ((baseLength + topLength)/2)*height
                    best = max(best, size)

    return best

n = int(input())
s = [int(i) for i in input().split(" ")]
res = solve(s)
print(f"{res:.1f}")