# BIO round 1 q1 - 24/24
import string

alpha = list(string.ascii_uppercase)

def solve(word):
    if len(word) == 1: return word
    # C + T = W => W-C = T 
    res = ""
    for i in range(len(word)-1, 0, -1):
        later = word[i]
        prev = word[i-1]
        laterIndex = alpha.index(later)+1
        prevIndex = alpha.index(prev)+1
        resIndex = ((laterIndex - prevIndex)%26) - 1
        res += alpha[resIndex]
    res += word[0] # remains unchanged
    return res[::-1]

word = input()
print(solve(word))