# BIO round 1 q1 - 24/24
import string

alpha = list(string.ascii_uppercase)

def solve(prev1, prev2, n):
    for i in range(n-2):
        val1 = alpha.index(prev1) + 1
        val2 = alpha.index(prev2) + 1
        newVal = alpha[(val1+val2)%26 - 1]
        prev2 = prev1
        prev1 = newVal
    return prev1

l1, l2, n = input().split(" ")
print(solve(l2, l1, int(n)))