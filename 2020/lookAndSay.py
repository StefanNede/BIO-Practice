# BIO round 1 2020 q1 - 25/25

def getBiggest(num, nums):
    for n in nums[::-1]:
        if num >= n:
            return n

def getRoman(num):
    '''
    returns roman numeral representation of a number
    we know that it can contain I, V, X, L, C, D, M
    e.g. num = 9
    return "IX"
    '''
    res = ""
    numerals = {1:'I',
                4:'IV',
                5:'V',
                9:'IX',
                10:'X',
                40:'XL',
                50:'L',
                90:'XC',
                100:'C',
                400:'CD',
                500:'D',
                900:'CM',
                1000:'M'}
    while num > 0:
        # get the biggest key that can go into num 
        # then subtract repeat 
        biggest = getBiggest(num, list(numerals.keys()))
        num -= biggest
        res += numerals[biggest] 
    
    return res

def solve(numeral, n):
    if n == 0: return numeral
    inter = ""
    prev = numeral[0]
    counter = 1
    while n > 0:
        if len(numeral) == 1:
            inter += 'I' + prev

        else:
            for i in range(1, len(numeral)):
                if numeral[i] == prev:
                    counter += 1
                if i == len(numeral)-1 and numeral[i] == prev:
                    roman = getRoman(counter)
                    inter += roman + numeral[i]
                elif i == len(numeral)-1 and numeral[i] != prev:
                    # add the thing for prev and add the thing for the current one
                    # of which there is only 1 occurrence
                    # adding prev
                    roman = getRoman(counter)
                    inter += roman + prev
                    # adding current
                    inter += 'I' + numeral[i]
                elif numeral[i] != prev:
                    roman = getRoman(counter)
                    inter += roman + prev
                    prev = numeral[i]
                    counter = 1
        numeral = inter
        inter = ""
        prev = numeral[0]
        counter = 1
        n -= 1
    return numeral

numeral, n = input().split(' ')
n = int(n)
res = solve(numeral, n)
print(res.count('I'), res.count('V'))