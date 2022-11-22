# BIO round 1 q1 - 25/25

def formatClock(clock):
    hours, minutes = clock
    while minutes >= 60:
        hours += 1
        minutes -= 60
    while hours >=24:
        hours -= 24
    return [hours, minutes]

def solve(f,s):
    firstClock = [0,0]
    secondClock = [0,0]
    while True:
        # increase the hours by one
        firstClock[0] += 1
        secondClock[0] += 1
        # increase the minutes by f and s respectively
        firstClock[1] += f
        secondClock[1] += s
        firstClock = formatClock(firstClock)
        secondClock = formatClock(secondClock)
        if firstClock == secondClock:
            break

    return firstClock

f, s = [int(i) for i in input().split(' ')]
res = solve(f, s)
if res[0] < 10:
    res[0] = "0"+str(res[0])
if res[1] < 10:
    res[1] = "0"+str(res[1])
print(f"{res[0]}:{res[1]}")