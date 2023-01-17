# full marks
s = input()
letters = set(s)
hCount = 0
greatest = []
for l in letters: 
    if s.count(l) == hCount:
        greatest.append(l)
    elif s.count(l) > hCount:
        greatest = [l]
        hCount = s.count(l)

greatest.sort()
print(*greatest)