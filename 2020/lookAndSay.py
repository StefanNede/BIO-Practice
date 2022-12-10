# round 1 q1 - 25/25
def getRoman(num):
    lookup = {1:"I", 4:"IV", 5:"V", 9:"IX", 10:"X", 40:"XL", 50:"L", 90:"XC", 100:"C", 400:"CD", 500:"D", 900:"CM", 1000:"M"}
    res = ""
    while num > 0:
        biggestFit = 0
        for n in list(lookup.keys())[::-1]:
            if num >= n:
                biggestFit = n
                break
        res += lookup[biggestFit]
        num -= biggestFit
    return res

def solve(word, n):
    for i in range(n):
        count = 1
        previous = word[0]
        inter = ""
        for j in range(1, len(word)):
            if word[j] == previous:
                count += 1
            else:
                inter += getRoman(count) + previous
                previous = word[j]
                count = 1
        # handle the last character or string of characters
        inter += getRoman(count) + previous
        # to allow the process to repeat
        word = inter
    return word

word, n = input().split(' ')
n = int(n)
res = solve(word, n)
print(res.count("I"), res.count("V"))