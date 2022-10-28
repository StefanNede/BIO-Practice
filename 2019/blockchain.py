# BIO round 1 2019 q3 - 
# not necessarily adjacent - ffs 
import string

alpha:str = string.ascii_uppercase # string of lowercase alphabet 

def getLettersLeftToPermute(l:int, p:str) -> str:
    res = [i for i in alpha[:l] if i not in p]
    return ''.join(res)

# ERROR HERE - CADB should return 2 but returns 3 because D and B are after A
def getIncreasingLetterCount(string:str) -> int:
    '''
    a string can have more than one set of increasing alphabetical letters e.g. BCAD has BC and AD and BCD
    we can stop if one of the counts is 3 because the rest of the algorithm wouldn't continue anyway

    count initialised to 1

    e.g. BCAD => {B:3, C:2, A:2, D:0}
    '''
    count = 1
    counts = [] # int array
    for i in range(len(string)):
        for j in range(i, len(string)):
            if string[i] < string[j]:
                count += 1
            if count == 3:
                # the algorithm wouldn't continue anyway 
                return 3
                break
        counts.append(count)
        count = 1

    return max(counts)

def getPermutations(l:int, p:str, lettersLeft:str) -> int:
    # print(p)
    if len(p) == l:
        return 1
    
    perms = 0

    for letter in lettersLeft:
        lettersLeft = lettersLeft.replace(letter, '') 
        # print(f"Letters left: {lettersLeft}")
        increasingLetterCount = getIncreasingLetterCount(p + letter)
        # print(f"Increasing letter count: {increasingLetterCount}")
        # we can add the letter to the string if adding doesn't put the increasing letter count at 3
        if increasingLetterCount <=2:
            perms += getPermutations(l, p + letter, lettersLeft)
        lettersLeft += letter # need to start again with the original lettersLeft

    return perms

inp:list = input().split(" ")
l, p = int(inp[0]), inp[1]
lettersLeft:str = getLettersLeftToPermute(l,p)
# print(getIncreasingLetterCount('CABD'))

print(getPermutations(l, p, lettersLeft))