# BIO round 1 q1 - 24/24

def solve(w1, w2):
    remaining = list(w2)
    for letter in w1:
        try:
            remaining.remove(letter)
        except ValueError:
            return "Not anagrams"
    if len(remaining) > 0:
        return "Not anagrams"
    else: return "Anagrams"
    

w1, w2= input(), input()
print(solve(w1, w2))