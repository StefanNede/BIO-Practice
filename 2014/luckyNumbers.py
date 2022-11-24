# BIO round 1 q1 - 25/25

def solve(n):
    odds = [1]
    for i in range(n+50): odds.append(odds[-1] + 2)

    previousLucky = 0
    index = 1 # to ignore the 1
    while True:
        curr = odds[index]

        if curr > n:
            return previousLucky, curr

        inter = [i for i in odds]
        for i in range(len(inter)):
            if (i+1)%curr == 0:
                odds.remove(inter[i])
        
        if curr != n:
            previousLucky = curr
        index += 1
                
n = int(input())
res = solve(n)
print(f"{res[0]} {res[1]}")