# 2010 round 1 q1 - 25/25

def isAnagram(n:int, m:int) -> bool:
    # check if n and m contain the same number of each digit
    n, m = str(n), str(m)

    for el in n:
        if n.count(el) != m.count(el):
            return False
    return True

def solve(n:int):
    gens = []
    for i in range(2,10):
        m = n*i
        if isAnagram(n, m):
            gens.append(i)
    
    if len(gens) > 0:
        res = ' '.join([str(l) for l in gens])
        return res
    else: 
        return "NO"

n = int(input())
print(solve(n))