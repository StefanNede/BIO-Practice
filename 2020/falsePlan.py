# BIO round 1 2020 q3
import string, math

p, q, r = [int(i) for i in input().split(' ')]
n = int(input())
alphabet = string.ascii_uppercase
alphabet = list(alphabet[:p])

def getTotalPsbs(maxAdj,length):
    base = math.factorial(length)
    # now we need to figure out a way to modify the base
    # where length is 4 and maxAdj is 2 and alphabet is length 2
    # the answer is 4C3 + 4C2 because you can either have 3As or 3Bs or 2As or 2Bs
    # but i don't know how to continue from there to a formula 
    return base

def getPsbsStarting(start, length):
    return 

def solve(maxAdj,length,n):
    '''
    permute letters in modified alphabet for a res of length
    where there can only be maxAdj adjacent letters

    possibly use a technique similar to modern art or parking (?)
    because again the plans will be in alphabetical order

    goal: output nth plan 
    '''
    return

print(solve(q,r,n))