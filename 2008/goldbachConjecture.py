# BIO round 1 q1 - 25/25
from collections import defaultdict

def isPrime(n):
    for i in range(2, int(n**0.5)+1):
        if n%i == 0: return False
    return True

def getPrimes(n):
    # gets primes up to n
    primes = []
    for i in range(2, n+1):
        if isPrime(i):
            primes.append(i)
    return primes

def solve(n):
    primesBelow = getPrimes(n)
    primesC = defaultdict(lambda:False)
    count = 0
    for p in primesBelow:
        primesC[n-p] = True
    for p2 in primesBelow:
        # otherwise doubles will only be counted once as a dictionary is used to store
        if p2*2 == n: count += 1
        if primesC[p2]:
            count += 1
    return count//2

n = int(input())
print(solve(n))