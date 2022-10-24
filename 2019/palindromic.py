# 2019 bio round 1 q1 - full marks
# q1b -> 11,000,000,000
def isPal(num):
    return str(num)  == str(num)[::-1]

def getFirstHalf(num):
    num = str(num)
    length = len(num)
    return num[:length//2]
    
def getSecondHalf(num):
    num = str(num)
    length = len(num)
    if length%2 == 1: return num[(length//2)+1 : ]
    return num[length//2 : ]


def getNextPal(num):
    '''
    fH: string
    sH: string
    middle: char
    '''
    if isPal(num):
        return num

    length = len(str(num))
    fH = getFirstHalf(num)
    sH = getSecondHalf(num)
    middle = ''
    if len(str(num))%2 == 1:
        middle = int(str(num)[length//2])
        if int(fH[::-1]) < int(sH):
            if middle == 9:
                middle = 0
                fH = list(fH)
                index = -1
                # continue the proccess until adjancent numbers are no longer 9
                while fH[index] == '9':
                    fH[index] = '0'
                    index -= 1
                fH[index] = str(int(fH[index]) + 1)
                fH = str(int(''.join(fH)))
            else:
                middle += 1
            sH = fH[::-1]
        else:
            sH = fH[::-1]
    else:
        if int(fH[::-1]) < int(sH):
            fH = str(int(fH) + 1)
            sH = fH[::-1]
        else:
            sH = fH[::-1]

    # print(fH, middle, sH)
    return int(fH + str(middle) + sH)

tests = {5:6,
        9:11,
        33:44,
        84:88,
        45653:45654,
        36460000:36466463,
        24355343:24366342,
        123450000:123454321,
        234567890:234575432,
        678999876:679000976,
        99999999999999:100000000000001,
        999999999999999:1000000000000001,
        123456789000000000:123456789987654321,
        987654321123456789:987654322223456789,
        1234567890000000000:1234567890987654321,
        9876543210123456789:9876543211123456789,
        9876543219123456789:9876543220223456789}

#num = int(input()) 
count = 0
for test in tests:
    test += 1 # next palindromic num so increment 
    res = getNextPal(test)
    if res == tests[test-1]:
        count += 1
    print(test-1, res, res == tests[test-1])
if count == len(tests): print("All tests passed")
else: print("some tests not passed")
