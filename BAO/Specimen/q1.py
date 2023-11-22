# 17/17
import string
alphabet = string.ascii_uppercase
def isPair(char1, char2):
    if alphabet.index(char1) + alphabet.index(char2) == 25:
        return True
    return False

def main(s):
    foundPair = True
    counter = 0
    while foundPair:
        if counter > 1000:
            return "Indefinite"
        counter += 1
        foundPair = False
        for i in range(len(s)-1):
            if isPair(s[i], s[i+1]):
                foundPair = True
                if s[i+1] > s[i]:
                    # teleport to end
                    if i == 0:
                        s = s[0] + s[2:] + s[1]
                    elif i == len(s)-2:
                        s = s[:i-1] + s[i] + s[i-1] + s[i+1]
                    else:
                        s = s[:i-1] + s[i] + s[i+2:] + s[i-1] + s[i+1]
                else:
                    # teleport to start
                    if i==0:
                        s = s[1] + s[0] + s[2:]
                    elif i == len(s)-2:
                        s = s[i-1] + s[i+1] + s[:i-1] + s[i]
                    else:
                        s = s[i-1] + s[i+1] + s[:i-1] + s[i] + s[i+2:]

                break
    return s

s = input()
res = main(s)
print(res)