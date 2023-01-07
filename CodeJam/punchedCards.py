def solve(r, c):
    res = []
    # add top row
    res.append("..+" + "-+"*(c-1))
    # add first row
    res.append("..|" + ".|"*(c-1))
    res.append("+" + "-+"*(c))
    # add rest of rows
    for i in range(r-1):
        res.append("|" + ".|"*(c))
        res.append("+" + "-+"*(c))

    return res

t = int(input())
for i in range(t):
    r, c = [int(i) for i in input().split(" ")]

    print(f"Case #{i+1}:")
    res = solve(r,c)
    for row in res:
        print(row)