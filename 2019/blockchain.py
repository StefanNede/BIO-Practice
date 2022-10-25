# BIO round 1 2019 q3 - 
# not necessarily adjacent 
import string

alpha = string.ascii_lowercase
perms = 0

def getLettersLeftToPermute(l, p):
    res = [i for i in alpha[:l] if i not in p]
    return ''.join(res)

def isLastGreater(last, letters):
    '''
    is the last char in the leftmost letters greater than at least one of the letters left to permute
    '''
    for l in letters:
        if l < last:
            return True
    return False

def getLettersBefore(p, letters):
    '''
    p: string
    letters: string

    returns the letters that come before p alphabetically
    p = A, letters = BD => ''
    p = B, letters = AD => 'A'
    '''
    res = ''
    for l in letters:
        if l < p:
            res += l
    return res

def getAdjacentLetterCount(string):
    res = 0
    previous = string[0]
    for l in string:
        if l > previous:
            res += 1
        else:
            res = 0
        prevous = l
    return res

def getPermutations(l, p, lettersLeft):
    global perms
    adjacentLetterCount = getAdjacentLetterCount(p)
    
    if len(p) == l:
        return 1
    elif adjacentLetterCount >= 3:
        return 0 
    elif len(lettersLeft) < 3 and isLastGreater(p[-1], lettersLeft):
        return 2
    
    elif len(lettersLeft) < 3 and not isLastGreater(p[-1],lettersLeft):
        lettersBefore = getLettersBefore(p[-1], lettersLeft)
        if p[-2] < p[-1]:
            print("Im crying rn")
        else:
            if lettersBefore == '':
                # if both the letters are later then one has to be later than the other so we can return 1
                return 1
            else:
                # otherwise there will be 2 permutations possible
                return 2
    else:
        for letter in lettersLeft:
            p = p+letter
            adjacentLeterCount = getAdjacentLetterCount(p)
            return perms + getPermutations(l, p, lettersLeft.replace(letter,''))

inp = input().split(" ")
l, p = int(inp[0]), inp[1]
lettersLeft = getLettersLeftToPermute(l,p)

print(getPermutations(l, p, lettersLeft))
