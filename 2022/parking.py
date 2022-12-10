# BIO round 1 q3 - 25/25
import string
alpha = list(string.ascii_uppercase)

final, n = input().split(" ")
n = int(n)
alpha = alpha[:len(final)]

def getPreferences(final):
    # returns a 2d list of the possible preferences for each of the car
    res = [[] for i in range(len(final))]
    taken = [False for i in range(len(final))]
    for i in range(len(alpha)):
        a = alpha[i]
        interRes = []
        finalPosition = final.index(a.lower())
        interRes.append(alpha[finalPosition])
        taken[finalPosition] = True
        for j in range(finalPosition-1, -1, -1):
            if taken[j]:
                interRes.append(alpha[j])
            if not taken[j]: break
        interRes.sort()
        res[i] = interRes
    return res

def getPsbs(start, preferences): 
    n = 1
    for p in range(len(start), len(preferences)):
        n *= len(preferences[p])
    return n

def solve(final, n): 
    res = ""
    preferences = getPreferences(final)
    # print(preferences)
    res += preferences[0][0] # A will always be in it's desired position
    pointer = 1
    while len(res) < len(final):
        for pref in preferences[pointer]:
            # get the number of possibilities with res + pref
            p = getPsbs(res + pref, preferences)
            if p >= n:
                res += pref
                break
            else:
                n -= p
        pointer += 1
    return res

print(solve(final, n))