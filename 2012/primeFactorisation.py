# BIO round 1 q1 - 24/24

def isPrime(num):
    if num == 1: return False
    for i in range(2,int(num**0.5)+1):
        if num%i == 0:
            return False
    return True

def getFactors(n):
    # gets the distinct prime factors
    factors = []
    if n <2: return []
    if n == 2: return [2]
    for i in range(2, int(n**0.5)+1):
        if n%i == 0 and isPrime(i):
            factors.append(i)
    if isPrime(n): factors.append(n)
    return factors

def solve(n):
    primeFactors = []
    res = 1

    # get factors
    primeFactors = getFactors(n)

    for prime in primeFactors:
        res *= prime
    
    return res
    

n = int(input())
print(solve(n))