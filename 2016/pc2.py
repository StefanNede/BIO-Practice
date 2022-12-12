# full marks
from collections import defaultdict, deque

def isPrime(n):
    for i in range(2, int((n**0.5))+1):
        if n%i == 0: return False
    return True

def getPrimes(p, maxPrime, differences):
    primes = []
    for i in differences:
        if p+i > maxPrime: break
        elif isPrime(p+i): primes.append(p+i)
    for i in differences:
        if p - i < 1: break
        elif isPrime(p-i): primes.append(p-i)
    return primes

def solve(maxPrime, p, q):
    differences = [2**i for i in range(0, int(maxPrime**(0.5)))]

    fQueue = deque([(p, 1)])
    bQueue = deque([(q,1)])
    fVis = defaultdict(lambda:False)
    bVis = defaultdict(lambda:False)
    
    fVis[p] = 1
    bVis[q] = 1

    while fQueue and bQueue:
        # handle forward action
        cPrime, steps = fQueue.popleft()
        nextPrimes = getPrimes(cPrime, maxPrime, differences)
        for prime in nextPrimes:
            if not fVis[prime]:
                fVis[prime] = steps+1
                if bVis[prime]:
                    return steps + bVis[prime]
                else:
                    fQueue.append((prime, steps+1))

        # handle backward action
        cPrime, steps = bQueue.popleft()
        nextPrimes = getPrimes(cPrime, maxPrime, differences)
        for prime in nextPrimes:
            if not bVis[prime]:
                bVis[prime] = steps+1
                if fVis[prime]:
                    return fVis[prime] + steps
                else:
                    bQueue.append((prime, steps+1))
    return -1

maxPrime, p, q = [int(i) for i in input().split(" ")]
print(solve(maxPrime, p, q))