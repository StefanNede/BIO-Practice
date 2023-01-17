n = int(input())
necklaces = []
for i in range(n):
    neck = [int(i) for i in input().split(" ")]
    necklaces.append(neck)

def c1(el): return el[0]
def c2(el): return el[1]

d = [0,0]
l = [0,0]
current = 'd'

while len(necklaces) > 0:
    if current == 'd':
        necklaces.sort(key=c1, reverse=True)
        neck = necklaces.pop(0)
        d[0] += neck[0]
        d[1] += neck[1]
        current = 'l'
    else:
        necklaces.sort(key=c2, reverse=True)
        neck = necklaces.pop(0)
        l[0] += neck[0]
        l[1] += neck[1]
        current = 'd'

print(l[1])