# round 1 q3 - overall score of 32
# 3a - 24 marks
# similar technique to modern art (2015)
def getNumDigits(n):
    if n == 1: return 1, [0,1]
    if n <= 10: return 2, [0,1,9]
    elif n <= 19: return 3, [0,1,9,9]
    # [0 with 0 digits, 1 with 1 digit, 9 with 2 digits, 9 with 3 digits]
    digits = 4 # must be at least 4 digits
    num = [0, 1, 9, 9]
    while sum(num) < n:
        nex = 9 * num[digits-2]
        num.append(nex)
        digits += 1
    return digits-1, num

def getUnfilled(arr):
    for i in range(len(arr)):
        if arr[i] == '':
            return i

def solve(n):
    numDigits, num = getNumDigits(n)
    res = ['' for i in range(numDigits)]
    filled = 0
    n -= sum(num[:-1])
    # now n represents the nth number of numDigits digits - which is what we want
    # build it up from the outside
    options = [i for i in range(1, 10)]
    currentIndex = 0
    while filled < numDigits:
        digitsInside = numDigits-(filled+2)
        if digitsInside <= 0:
            # we are either at the inner 2 or the inner 1
            # inner 1 will always be 1
            if (numDigits - filled) == 1:
                res[len(res)//2] = '5'
                break
            else:
                innerOptions = ["19", "28", "37", "46", "55", "64", "73", "82", "91"]
                inner = innerOptions[n-1]
                res[(len(res)//2)-1] = inner[0]
                res[(len(res)//2)] = inner[1]
                break
        else:
            interN = (num[digitsInside])
            # print(n, res, digitsInside, interN)
            # break
            if interN >= n:
                firstUnfilled = getUnfilled(res)
                res[firstUnfilled] = str(options[currentIndex])
                res[len(res)-firstUnfilled-1] = str(10 - options[currentIndex])
                currentIndex = 0
                filled += 2
            else:
                n -= interN
                currentIndex += 1
    return "".join(res)

n = int(input())
print(solve(n))

# b - 384 - 2 marks
def isUpDown(num):
    for i in range((len(num)//2)):
        if int(num[i]) + int(num[-(i+1)]) != 10:
            return False
    return True
from itertools import permutations
def partB():
    options = "123456789"
    count = 0
    for perm in permutations(options, len(options)):
        if isUpDown("".join(perm)): count += 1
    return count # ---> 384

# c - 38 digits - 3 marks
# print(getNumDigits(1000000000000000000))

# d - 1001 because it is odd so all of the upside down numbers will contain a 5 in the middle
# whilst for 1000 they won't all have that  - 3 marks