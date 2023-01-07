# given an array of coins with varying denominations and an integer sum representing the total amount of money
# return the fewest coins required to make up that sum
# if sum cannot be constructure, return -1

COINS = [2,5,10,20,50]
best = 100000

def naive(s):
    # recursive brute force solution
    def recurse(s, coinsUsed=0):
        global best
        if s == 0:
            if coinsUsed < best: 
                best = coinsUsed
        elif s > 0:
            for coin in COINS:
                recurse(s-coin, coinsUsed+1)
    recurse(s)
    return best

def solve(s):
    '''
    dp solution
    e.g. s = 78
    50, 20, 2, 2, 2, 2
    return 6
    '''
    memo = [numCoins+1]
    return s

#s = int(input()) # the sum
s = 20 
best = s
print(naive(s))
print(solve(s))