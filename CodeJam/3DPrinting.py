def solve(printers):
    used = []
    for current in range(4):
        used.append(min(printers[0][current], printers[1][current], printers[2][current]))
    total = sum(used)
    if total == 10**6:
        return used
    elif total > 10**6:
        diff = total - (10**6)
        for a in range(len(used)):
            used[a] = max(1, used[a]-diff)
            diff = sum(used) - (10**6)
        return used
    else:
        return "IMPOSSIBLE"

t = int(input())
for i in range(t):
    printers = []
    for j in range(3):
        c,m,y,k = [int(k) for k in input().split(" ")]
        printers.append([c,m,y,k])

    print(f"Case #{i+1}: ", end="")
    res = solve(printers)
    if len(res) == 4:
        print(*res)
    else:
        print(res)
