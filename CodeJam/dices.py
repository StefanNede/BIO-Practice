def solve(die):
    die.sort()
    current = 0
    for d in die:
        if current < d:
            current += 1
    return current

t = int(input())
for i in range(t):
    n = int(input())
    die = [int(j) for j in input().split(" ")]

    print(f"Case #{i+1}: {solve(die)}")