# round 1 q1 - overall score of 27
# 1a - 24 marks
# 1b - R, Q - 3 marks
import string
alpha = list(string.ascii_uppercase)
def solve(l1,l2,n):
    if n == 1: return l1
    if n == 2: return l2
    for i in range(n-2): 
        ne = (alpha.index(l1)+1) + (alpha.index(l2)+1)
        ne %= 26
        nex = alpha[ne-1]
        l1 = l2 
        l2 = nex
    return l2

l1, l2, n = input().split(" ")
n = int(n)
print(solve(l1,l2,n))