# Round 1 2015 q3 (similar to 2022 q3) - 25/25
# 3b - 2/2
import math

LETTERS = 'ABCD'

def getNumPossibilities(a,b,c,d) -> int:
    numerator = math.factorial(a+b+c+d) 
    denominator = 1
    if a > 1: denominator *= math.factorial(a)
    if b > 1: denominator *= math.factorial(b)
    if c > 1: denominator *= math.factorial(c)
    if d > 1: denominator *= math.factorial(d)
    return int(numerator/denominator)

def getPsbsStartingWith(start:str,a,b,c,d) -> int:
    '''
    returns the number of possibilities starting with a string
    e.g. BA when you have A,B,C,D to choose from gives 2
    '''
    for el in start:
        if el == 'A': a -= 1
        if el == 'B': b -= 1
        if el == 'C': c -= 1
        if el == 'D': d -= 1
    return getNumPossibilities(a, b, c, d)

def solve(letterCount:list, n:int, total_psbs:int) -> str:
    '''
    for each empty space in our resPerm string we want to figure out
    how many perms there are that start with each of ABCD and see if this is 
    greater than the modified n - if it is then that means there are more perms 
    that start with that letter than the perm we are looking for, so the perm we 
    are looking for has to start with that letter

    e.g. we have ABC and are looking for the 5th perm (n = 5)
    at the start we are searching for term 1 to go into our resPerm 
    so we look at how many perms start with A then B then C
    2 start with A but this is less than n so the 5th perm can't start with A
    we then modify n by subtracting 2 from it because those perms that start with A
    can't be right so we discard them - now n = 3 and our modified perm list that we are searching through would be:
    1 - BAC
    2 - BCA
    3 - CAB (the goal)
    4 - CBA
    next get number of perms starting with B - 2. this is less than modified n 
    so again change n -> 3-2 = 1
    now get number of perms starting with C which is 2. this is more than n meaning
    that our goal perm has to be in this chain of perms that start with C, so we add C to resPerm

    now resPerm = C, and n = 1, and we repeat the process
    how many perms start with CA - 1 -> this is equal to n so our nth perm must start with CA

    now resPerm = CA, and n = 1, and we repeat the process one last time
    how many perms start with CAB (because we have no more As left to use) - 1 -> equal to n so add B to resPerm to get answer

    ans => CAB (which is correct)
    '''
    resPerm:str = ''
    while len(resPerm) != sum(letterCount):
        termSearchingFor = len(resPerm) + 1 
        # go through ABCD
        for i in range(4):
            # check if there are any of that letter to start with or if all of that letter have been used up
            if letterCount[i] > 0 and resPerm.count(LETTERS[i]) < letterCount[i]:
                letter = LETTERS[i] # grab the letter
                psbsStartingWithLetter = getPsbsStartingWith(resPerm+letter, a, b, c, d) # get psbs starting with resPerm+letter
                if psbsStartingWithLetter < n:
                    n -= psbsStartingWithLetter
                elif psbsStartingWithLetter >= n:
                    resPerm += letter
                    break # move onto next term
    return resPerm 

a,b,c,d,n = [int(i) for i in input().split(' ')]
letterCount = [a,b,c,d]

total_psbs = getNumPossibilities(a, b, c, d)
res = solve(letterCount, n, total_psbs)
print(res)