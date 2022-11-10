# Bio round 1 q1 - 24/24
from collections import defaultdict
digits = ['ONE', 'TWO', 'THREE', 'FOUR', 'FIVE', 'SIX', 'SEVEN', 'EIGHT','NINE']

def findIndexes(word, letter) -> list:
    res = []
    for i in range(len(word)):
        if word[i] == letter:
            res.append(i)
    return res
    
def exists(word:str, digit:str) -> bool:
    if word == digit: return True
    positions = defaultdict(lambda:False)
    for letter in digit:
        indexes = findIndexes(word, letter)
        positions[letter] = indexes     
    
    minIndex = -1 # this will store the minimum index that the next letter has to be after 
    flag = False # has the min index been changed
    for letter,indexes in positions.items():
        flag = False
        for index in indexes:
            if index > minIndex:
                minIndex = index
                flag = True
                break
        if not flag:
            break
    
    return flag 

def solve(word:str):
    for digit in digits:
        if exists(word, digit):
            return digits.index(digit)+1
    return "NO"

word = input()
res = solve(word)
print(res)