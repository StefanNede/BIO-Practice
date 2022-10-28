# BIO round 1 2019 q3 - 18/24 marks - takes too long for 3 cases with most perms
# 3b - 2/2 marks ez
import string, time

alpha:str = string.ascii_uppercase # string of lowercase alphabet 

def getLettersLeftToPermute(l:int, p:str) -> str:
    res = [i for i in alpha[:l] if i not in p]
    return ''.join(res)

def getCanBeAdded(string:str, letter:str, leftToAdd:str) -> int:
    # the key to this question is this function working efficiently 
    '''
    get the smallest char that appears in the original string, and if 
    when iterating a later char is after this and the letter to be added is 
    also after this and alphabetically before the later char then a string of 
    3 increasing chars will exist so return false
    '''    
    smallest = None
    for char in string:
        if smallest is None or char < smallest:
            smallest = char
        elif smallest < char and char < letter:
            return False

    # further optimisation allows us to stop extra recursions when we know 
    # they are 'doomed' - if the smallest is less than the letter and one of the
    # letters left to be added is greater than the letter that was just added then we know 
    # no blockchains can start with string+letter (the params in this function) because that future letter must be added at some point
    # this allows us to get some of the 2 markers
    if smallest < letter:
        for char in leftToAdd:
            if letter < char:
                return False

    return True

def getPermutations(l:int, p:str, lettersLeft:str) -> int:
    '''
    uses DFS but cuts out some branches by anticipating them failing later on - not good but meh
    '''
    # print(p)
    if len(p) == l:
        return 1
    
    perms = 0

    for letter in lettersLeft:
        lettersLeft = lettersLeft.replace(letter, '') 
        # print(f"Letters left: {lettersLeft}")
        canBeAdded = getCanBeAdded(p, letter, lettersLeft)
        # print(f"Increasing letter count: {increasingLetterCount}")
        # we can add the letter to the string if adding doesn't put the increasing letter count at 3
        if canBeAdded:
            perms += getPermutations(l, p + letter, lettersLeft)
        lettersLeft += letter # need to start again with the original lettersLeft

    return perms

inp:list = input().split(" ")
l, p = int(inp[0]), inp[1]
lettersLeft:str = getLettersLeftToPermute(l,p)
# print(getCanBeAdded('CAD', 'B', ''))

start = time.time()
res = (getPermutations(l, p, lettersLeft))
end = time.time()

print(res, end-start)